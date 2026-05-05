from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 459167654 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1150738494 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 1150738494 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1993485646 % 2147481317
}
