from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 709299581 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1719943311 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 1719943311 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 855076012 % 2147481317
}
