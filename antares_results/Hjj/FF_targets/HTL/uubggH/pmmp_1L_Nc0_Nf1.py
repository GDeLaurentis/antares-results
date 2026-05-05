from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 233027855 % 2147481317,
    PentagonMonomial({'F[1,3]': 1}): 1772256540 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1146996384 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 267638523 % 2147481317,
    PentagonMonomial({'F[1,8]': 1}): 573498192 % 2147481317,
    PentagonMonomial({'F[1,9]': 1}): 573498192 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 254097705 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 853973482 % 2147481317
}
