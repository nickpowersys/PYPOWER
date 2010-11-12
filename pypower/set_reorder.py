# Copyright (C) 1996-2010 Power System Engineering Research Center
# Copyright (C) 2010 Richard Lincoln <r.w.lincoln@gmail.com>
#
# Licensed under the Apache License, Version 2.0 [the "License"]
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from numpy import ndim

def set_reorder(A, B, idx, dim=1):
    """ Assigns B to A with one of the dimensions of A indexed.

    @return: A after doing A(:, ..., :, IDX, :, ..., :) = B
    where DIM determines in which dimension to place the IDX.

    @see: L{get_reorder}
    @see: U{http://www.pserc.cornell.edu/matpower/}
    """
    ndims = ndim(A)
    if ndims ==  1:
        A[idx] = B
    elif ndims == 2:
        if dim == 1:
            A[idx, :] = B
        elif dim == 2:
            A[:, idx] = B
        else:
            raise ValueError
    else:
        raise ValueError

    return A