# Copyright 2018-2022 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import inspect
import textwrap
import numpy as np
from scipy import signal, ndimage
from PIL import Image, ImageDraw
import math


def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


def gauss2d(sigma):

    def gauss1d(sigma):
        # determine filter length by finding next odd number after sigma * 6 (to prevent early truncation of array)
        filter_len = int(np.ceil(sigma * 6) // 2 * 2 + 1)

        # gaussian function
        def gaussian(x): return np.exp(-(x*x) / (2*sigma*sigma))

        # 1d gaussian array
        gauss_array = gaussian(
            np.array(range(-(filter_len // 2), filter_len // 2 + 1)))

        # normalize the array
        normalized_gaussian = gauss_array / sum(gauss_array)

        return normalized_gaussian

    # Get 1D gauss array and add a new axis
    gauss1D = gauss1d(sigma)[np.newaxis]

    # Get 2D gauss matrix by convolving the gauss array with the transpose of itself
    gauss2D = signal.convolve2d(gauss1D, gauss1D.T)

    return gauss2D


def MakeGaussianPyramid(image, scale, minsize):
    """
    Build a scaled representation of an input image as a gaussian pyramid

    Inputs:
    ~~~~~~~~~~~~~~~~~~~~~~
    image         PIL Image to build the scaled representation of
    scale         float value to scale each layer of the pyramid by
    minscale      int value to specify the limit of the largest dimension of the lowest resolution layer

    Output:
    ~~~~~~~~~~~~~~~~~~~
    pyramid       list of nparrays of float32 values. 
                  Each nparray is a layer of a pyramid represented as a floating point numpy array.
    """

    # initalize the output. first element of list is the original image
    pyramid = [np.asarray(image, np.float32)]

    # keep scaling unless the next layer's largest dimension is less than minsize
    while int(max(image.size) * scale) >= minsize:

        width, height = image.size
        arr = np.asarray(image, np.float32)

        # if the image has colour channels (array will have a 3rd dimension)
        # apply gaussian seperately to each channel
        if len(arr.shape) == 3:
            for channel in range(0, 3):
                arr[:, :, channel] == ndimage.gaussian_filter(
                    input=arr[:, :, channel], sigma=1/(2 * scale))

        # else I can just apply filter directly to the array
        else:
            arr = ndimage.gaussian_filter(input=arr, sigma=1/(2 * scale))

        # turn array into PIL image to use the resize function
        output = arr.astype('uint8')
        output = np.clip(output, 0, 255)
        image = Image.fromarray(output)
        image = image.resize(
            (int(width * scale), int(height * scale)), Image.BICUBIC)

        # save new layer to the output
        pyramid.append(np.asarray(image, np.float32))

    return pyramid


def ShowGaussianPyramid(pyramid):
    """
    Construct a horizontal image that joins all the images in a gaussian pyramid

    Inputs:
    ~~~~~~~~~~~~~~~~~~~~~~
    pyramid       list of numpy arrays where each numpy array represents a 
                  layer of the pyramid in floating point values         

    Output:
    ~~~~~~~~~~~~~~~~~~~
    im            PIL image that is the horizontal image that joins all layers of a gaussian pyramid
    """

    # width of image will be sum of all widths combined
    w = sum([pyramid[x].shape[1] for x in range(0, len(pyramid))])
    # height of image will be height of largest layer (first layer)
    h = pyramid[0].shape[0]

    # if two dimensions, image is greyscale, else RGB
    if len(pyramid[0].shape) == 2:
        im = Image.new("L", (w, h), color=255)
    else:
        im = Image.new("RGB", (w, h), color=(255, 255, 255))

    # offset values as we paste each layer into the final image
    offset_x, offset_y = 0, 0

    for layer in range(0, len(pyramid)):

        # make sure layer has proper dtype and is clamped
        layer_output = pyramid[layer].astype('uint8')
        layer_im = np.clip(layer_output, 0, 255)

        # paste layer into the image
        im.paste(Image.fromarray(layer_im), (offset_x, offset_y))

        # adjust offset for next layer
        offset_x += pyramid[layer].shape[1]

    return im


def FindTemplate(pyramid, template, threshold):
    """
    Match a template to an image 
    using the image pyramid and normal cross correlation 
    of the template and the layers of the pyramid

    Inputs:
    ~~~~~~~~~~~~~~~~~~~~~~
    pyramid       list of numpy arrays where each numpy array represents a 
                  layer of the pyramid in floating point values         
    template      PIL image to find matches of 
    threshold     float value to determine what should be 
                  considered a match in terms of similarity

    Output:
    ~~~~~~~~~~~~~~~~~~~
    ans            RGB PIL image with red lines to represent where 
                   matches are in the first layer of the pyramid
    """

    # resize the template to be 15 pixels in width
    resize_factor = template.size[0] / 15
    template = template.resize(
        (int(template.size[0]/resize_factor), int(template.size[1]/resize_factor)), Image.BICUBIC)

    # convert the first layer of the pyramid into a RGB image to draw red lines on it
    ans = Image.fromarray(
        np.clip(pyramid[0].astype('uint8'), 0, 255)).convert('RGB')

    # record dimensions to help with scaling the boxes later
    ans_w, ans_h = ans.size
    template_w, template_h = template.size

    # do ncc for each layer and scale if necessary
    for layer in pyramid:

        # create PIL image from numpy array of the layer and use ncc
        im = Image.fromarray(np.clip(layer.astype('uint8'), 0, 255))
        corr_arr = normxcorr2D(im, template)

        # calculate the scaling factor if there are matches
        w, h = im.size
        scale = ans_w / w

        # traverse correlation array to look at similarity values
        for i in range(0, h):
            for j in range(0, w):
                # if a similarity value is above the threshold
                if corr_arr[i][j] > threshold:

                    # calculate center point coordinates
                    y_cord = i * scale
                    x_cord = j * scale

                    # calculate corner points of box
                    y1 = max(0, int(y_cord - template_h * scale // 2))
                    y2 = min(ans_h, int(y_cord + template_h * scale // 2))
                    x1 = max(0, int(x_cord - template_w * scale // 2))
                    x2 = min(ans_w, int(x_cord + template_w * scale // 2))

                    # draw box
                    draw = ImageDraw.Draw(ans)
                    draw.line((int(x1), int(y1), int(x2), int(y1)),
                              fill="red", width=2)
                    draw.line((int(x2), int(y1), int(x2), int(y2)),
                              fill="red", width=2)
                    draw.line((int(x2), int(y2), int(x1), int(y2)),
                              fill="red", width=2)
                    draw.line((int(x1), int(y2), int(x1), int(y1)),
                              fill="red", width=2)
                    del draw

    return ans


def normxcorr2D(image, template):
    """
    Normalized cross-correlation for 2D PIL images

    Inputs:
    ----------------
    template    The template. A PIL image.  Elements cannot all be equal.

    image       The PIL image.

    Output:
    ----------------
    nxcorr      Array of cross-correlation coefficients, in the range
                -1.0 to 1.0.

                Wherever the search space has zero variance under the template,
                normalized cross-correlation is undefined.

    Implemented for CPSC 425 Assignment 3

    Bob Woodham
    January, 2013
    """

    # (one-time) normalization of template
    t = np.asarray(template, dtype=np.float64)
    t = t - np.mean(t)
    norm = math.sqrt(np.sum(np.square(t)))
    t = t / norm

    # create filter to sum values under template
    sum_filter = np.ones(np.shape(t))

    # get image
    a = np.asarray(image, dtype=np.float64)
    # also want squared values
    aa = np.square(a)

    # compute sums of values and sums of values squared under template
    a_sum = signal.correlate2d(a, sum_filter, 'same')
    aa_sum = signal.correlate2d(aa, sum_filter, 'same')
    # Note:  The above two lines could be made more efficient by
    #        exploiting the fact that sum_filter is separable.
    #        Even better would be to take advantage of integral images

    # compute correlation, 't' is normalized, 'a' is not (yet)
    numer = signal.correlate2d(a, t, 'same')
    # (each time) normalization of the window under the template
    denom = np.sqrt(aa_sum - np.square(a_sum)/np.size(t))

    # wherever the denominator is near zero, this must be because the image
    # window is near constant (and therefore the normalized cross correlation
    # is undefined). Set nxcorr to zero in these regions
    tol = np.sqrt(np.finfo(denom.dtype).eps)
    nxcorr = np.where(denom < tol, 0, numer/denom)

    # if any of the coefficients are outside the range [-1 1], they will be
    # unstable to small variance in a or t, so set them to zero to reflect
    # the undefined 0/0 condition
    nxcorr = np.where(np.abs(nxcorr-1.) >
                      np.sqrt(np.finfo(nxcorr.dtype).eps), nxcorr, 0)

    return nxcorr
