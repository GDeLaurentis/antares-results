from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 1192620489 % 2147481317,
    PentagonMonomial({'F[1,3]': 1}): 1275162018 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1676222103 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 1107318907 % 2147481317,
    PentagonMonomial({'F[1,8]': 1}): 1911851710 % 2147481317,
    PentagonMonomial({'F[1,9]': 1}): 1911851710 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 969963281 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1413777642 % 2147481317
}
