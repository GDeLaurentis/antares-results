from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 1510723598 % 2147481317,
    PentagonMonomial({'F[1,2]': 1}): 1532521221 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1532521221 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 1532521221 % 2147481317,
    PentagonMonomial({'F[1,7]': 1}): 1532521221 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1229920192 % 2147481317
}
