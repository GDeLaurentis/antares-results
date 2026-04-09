import numpy
from importlib import import_module
from pathlib import Path

from pentagon_functions import evaluate_pentagon_functions, PentagonMonomial
from linac.sparse_matrix_tools import matrix_from_plain_txt_coo

this_script_path = Path(__file__).resolve().parent


def remainder(channel, partial, phase_space_point, semi_numerical=False, as_dict=False, mu2=1):
    """
    Evaluate the finite remainder for a given channel, helicity configuration, and phase-space point.

    The remainder is reconstructed as a linear combination of transcendental basis functions,
    using precomputed rational matrices and helicity-dependent rational prefactors.

    Parameters
    ----------
    channel : str
        Scattering channel ('ggggH', 'uubggH', 'uubddbH').
    partial : str
        Identifier of the partial amplitude ('helicity_#L_#Nc_#Nf').
    phase_space_point : lips.Particles object
        Phase-space point with spinor-helicity data.
    semi_numerical : bool, optional
        If True, return numerical coefficients multiplying pentagon monomials, which are
        kept symbolic. Automatically enabled for finite-field and p-adic phase-space points.
    as_dict : bool, optional
        If True and semi_numerical=True, return a dictionary {pentagon monomial: coefficient}.
    mu2 : float, optional
        Renormalisation scale entering the evaluation of pentagon functions.

    Returns
    -------
    float or list of (number, PentagonMonomial) or dict
        - Numerical value of the remainder if semi_numerical=False.
        - List of (coefficient, pentagon monomial) pairs if semi_numerical=True.
        - Dictionary mapping pentagon monomials to coefficients if as_dict=True.
    """
    oPs = phase_space_point
    helicity = partial.split("_")[0]

    if len(oPs) == 6:
        oPs5pt = oPs.cluster([[1, ], [2, ], [3, ], [4, ], [5, 6]])
        oPs5pt[5]._r_sp_d = oPs5pt[5]._l_sp_d = oPs5pt[5]._r_sp_u = oPs5pt[5]._l_sp_u = None
    else:
        oPs5pt = oPs
    if oPs.field in ['finite field', 'padic', 'Fp', 'Qp']:
        semi_numerical = True

    representative_helicity = helicity
    if channel == 'ggggH' and helicity == 'pmpm':
        representative_helicity = 'ppmm'
    elif channel == 'uubggH' and helicity == 'pmmp':
        representative_helicity = 'pmpm'
    elif channel == 'uubddbH' and helicity == 'pmmp':
        representative_helicity = 'pmpm'

    module = import_module(f".HTL.{channel}.{representative_helicity}", package=__package__)
    lTerms = module.lTerms

    with open(this_script_path / "HTL" / channel / "basis_transcendental.txt", "r") as f:
        basis_transcendental = f.readlines()
    basis_transcendental = [PentagonMonomial(entry.replace("\n", "")) for entry in basis_transcendental]

    if not semi_numerical:
        pentagon_functions = basis_transcendental
        pentagon_monomials = list(set([pentagon for pentagon_monomial in pentagon_functions
                                       for pentagon in pentagon_monomial.distinct_elements()]))

        evaluated_pentagon_monomials = evaluate_pentagon_functions(
            pentagon_monomials, oPs.image(("654321", False)), mu2=mu2,
            pentagon_function_set='m1', precision="d", number_of_cores=4)

        pentagon_basis = basis_transcendental
        numerical_pentagon_basis = [entry.subs(evaluated_pentagon_monomials) for entry in pentagon_basis]

    rref = matrix_from_plain_txt_coo(this_script_path / "HTL" / channel / representative_helicity / f"matrix_{partial}")

    permutation = ('12345', False)
    if channel == 'ggggH' and helicity == 'pmpm':
        permutation = ('13245', False)
    elif channel == 'uubggH' and helicity == 'pmmp':
        permutation = ('12435', False)
    elif channel == 'uubddbH' and helicity == 'pmmp':
        permutation = ('12435', False)

    oPs5ptPerm = oPs5pt.image(permutation)

    if not semi_numerical:
        num_eval = lTerms(oPs5ptPerm) @ rref @ numpy.array(numerical_pentagon_basis)
        return num_eval

    semi_num_result = [(a, b) for a, b in zip(lTerms(oPs5ptPerm) @ rref, basis_transcendental) if a != 0]
    if as_dict:
        return dict([(b, a) for a, b in semi_num_result])
    else:
        return semi_num_result
