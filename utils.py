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
from scipy import signal 

def show_code(demo):
    """Showing the code of the demo."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        # Showing the code of the demo.
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))

def gauss1d(sigma):

    # determine filter length by finding next odd number after sigma * 6
    filter_len = int(np.ceil(sigma * 6) // 2 * 2 + 1)

    # gaussian function
    gaussian = lambda x: np.exp(-(x*x) / (2*sigma*sigma))

    # 1d gaussian array
    gauss_array = gaussian(np.array(range(-(filter_len // 2), filter_len // 2 + 1)))

    # normalize the array
    normalized_gaussian = gauss_array / sum(gauss_array)

    return normalized_gaussian

def gauss2d(sigma):

    def gauss1d(sigma):
        # determine filter length by finding next odd number after sigma * 6 (to prevent early truncation of array)
        filter_len = int(np.ceil(sigma * 6) // 2 * 2 + 1)

        # gaussian function
        gaussian = lambda x: np.exp(-(x*x) / (2*sigma*sigma))

        # 1d gaussian array
        gauss_array = gaussian(np.array(range(-(filter_len // 2), filter_len // 2 + 1)))

        # normalize the array
        normalized_gaussian = gauss_array / sum(gauss_array)

        return normalized_gaussian

    # Get 1D gauss array and add a new axis
    gauss1D = gauss1d(sigma)[np.newaxis]

    # Get 2D gauss matrix by convolving the gauss array with the transpose of itself
    gauss2D = signal.convolve2d(gauss1D, gauss1D.T)

    return gauss2D
