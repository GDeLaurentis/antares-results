from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 249488243 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 709299581 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 709299581 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 728882155 % 2147481317,
    PentagonMonomial({'F[1,5]': 2}): 1146628874 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'F[1,6]': 1}): 1146628874 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'im[1,1]': 1}): 855076012 % 2147481317,
    PentagonMonomial({'F[1,6]': 2}): 1146628874 % 2147481317,
    PentagonMonomial({'F[1,6]': 1, 'im[1,1]': 1}): 855076012 % 2147481317,
    PentagonMonomial({'im[1,1]': 2}): 1292405305 % 2147481317
}
