# Copyright (C) 1996-2010 Power System Engineering Research Center
# Copyright (C) 2009-2010 Richard Lincoln
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

from ppoption import ppoption
from runopf import runopf

def rundcopf(casedata='case9', ppopt=None, fname='', solvedcase=''):
    """ Runs a DC optimal power flow.

    @see: L{runopf}, L{runduopf}
    @see: U{http://www.pserc.cornell.edu/matpower/}
    """
    ## default arguments
    ppopt = ppoption() if ppopt is None else ppopt

    ppopt = ppoption(ppopt, PF_DC=True)
    return runopf(casedata, ppopt, fname, solvedcase)