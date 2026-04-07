from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 538640725 % 2147481317,
    PentagonMonomial({'F[1,2]': 1}): 415588488 % 2147481317,
    PentagonMonomial({'F[1,3]': 1}): 874297454 % 2147481317,
    PentagonMonomial({'F[1,4]': 1}): 1325409718 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 467814343 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 467814343 % 2147481317,
    PentagonMonomial({'F[1,7]': 1}): 437178774 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 1076520997 % 2147481317,
    PentagonMonomial({'F[1,11]': 1}): 1101595889 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 1408515497 % 2147481317
}
