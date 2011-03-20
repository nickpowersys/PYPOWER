# Copyright (C) 2008-2011 Power System Engineering Research Center (PSERC)
# Copyright (C) 2010-2011 Richard Lincoln <r.w.lincoln@gmail.com>
#
# PYPOWER is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# PYPOWER is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PYPOWER. If not, see <http://www.gnu.org/licenses/>.

from scipy.sparse import csr_matrix

from d2Ibr_dV2 import d2Ibr_dV2

def d2AIbr_dV2(dIbr_dVa, dIbr_dVm, Ibr, Ybr, V, lam):
    """Computes 2nd derivatives of |complex current|^2 w.r.t. V.

    Returns 4 matrices containing the partial derivatives w.r.t. voltage
    angle and magnitude of the product of a vector LAM with the 1st partial
    derivatives of the square of the magnitude of the branch currents.
    Takes sparse first derivative matrices of complex flow, complex flow
    vector, sparse branch admittance matrix YBR, voltage vector V and
    nl x 1 vector of multipliers LAM. Output matrices are sparse.

    For more details on the derivations behind the derivative code used
    in PYPOWER information, see:

    [TN2]  R. D. Zimmerman, "AC Power Flows, Generalized OPF Costs and
           their Derivatives using Complex Matrix Notation", MATPOWER
           Technical Note 2, February 2010.
              http://www.pserc.cornell.edu/matpower/TN2-OPF-Derivatives.pdf

    @return: The 2nd derivatives of |complex current|**2 w.r.t. V.
    @see: L{dIbr_dV}.
    @see: U{http://www.pserc.cornell.edu/matpower/}
    """
    # define
    il = range(len(lam))

    diaglam = csr_matrix((lam, (il, il)))
    diagIbr_conj = csr_matrix((Ibr.conj(), (il, il)))

    Iaa, Iav, Iva, Ivv = d2Ibr_dV2(Ybr, V, diagIbr_conj * lam)

    Haa = 2 * ( Iaa + dIbr_dVa.T * diaglam * dIbr_dVa.conj() ).real
    Hva = 2 * ( Iva + dIbr_dVm.T * diaglam * dIbr_dVa.conj() ).real
    Hav = 2 * ( Iav + dIbr_dVa.T * diaglam * dIbr_dVm.conj() ).real
    Hvv = 2 * ( Ivv + dIbr_dVm.T * diaglam * dIbr_dVm.conj() ).real

    return Haa, Hav, Hva, Hvv
