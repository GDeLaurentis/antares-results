from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 461629563 % 2147481317,
    PentagonMonomial({'F[1,3]': 1}): 1729855897 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 174510483 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 112637747 % 2147481317,
    PentagonMonomial({'F[1,8]': 1}): 1160995900 % 2147481317,
    PentagonMonomial({'F[1,9]': 1}): 1160995900 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 654008639 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1623949868 % 2147481317
}
