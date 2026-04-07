from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 1313226560 % 2147481317,
    PentagonMonomial({'F[1,2]': 1}): 2036742359 % 2147481317,
    PentagonMonomial({'F[1,4]': 1}): 1108976300 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1389168122 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 2036742359 % 2147481317,
    PentagonMonomial({'F[1,7]': 1}): 1610302599 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 458718537 % 2147481317,
    PentagonMonomial({'F[1,11]': 1}): 1653800477 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 410333616 % 2147481317,
    PentagonMonomial({'F[1,5]': 2}): 1181548157 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'F[1,7]': 1}): 1931866320 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'im[1,1]': 1}): 1931866320 % 2147481317,
    PentagonMonomial({'F[1,7]': 1, 'F[1,11]': 1}): 215614997 % 2147481317,
    PentagonMonomial({'F[1,7]': 1, 'im[1,1]': 1}): 215614997 % 2147481317,
    PentagonMonomial({'F[1,11]': 2}): 965933160 % 2147481317,
    PentagonMonomial({'F[2,12]': 1}): 1931866320 % 2147481317,
    PentagonMonomial({'F[2,14]': 1}): 1931866320 % 2147481317,
    PentagonMonomial({'im[1,1]': 2}): 1825503597 % 2147481317
}
