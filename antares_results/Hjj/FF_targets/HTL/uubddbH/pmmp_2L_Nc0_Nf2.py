from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 666374788 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 459167654 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 459167654 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1229146009 % 2147481317,
    PentagonMonomial({'F[1,5]': 2}): 767158996 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'F[1,6]': 1}): 767158996 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'im[1,1]': 1}): 1993485646 % 2147481317,
    PentagonMonomial({'F[1,6]': 2}): 767158996 % 2147481317,
    PentagonMonomial({'F[1,6]': 1, 'im[1,1]': 1}): 1993485646 % 2147481317,
    PentagonMonomial({'im[1,1]': 2}): 153995671 % 2147481317
}
