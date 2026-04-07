from pentagon_functions import PentagonMonomial

target_values = {
    PentagonMonomial({}): 937212209 % 2147481317,
    PentagonMonomial({'F[1,2]': 1}): 1954981925 % 2147481317,
    PentagonMonomial({'F[1,3]': 1}): 1086647708 % 2147481317,
    PentagonMonomial({'F[1,4]': 1}): 945732834 % 2147481317,
    PentagonMonomial({'F[1,5]': 1}): 1345181666 % 2147481317,
    PentagonMonomial({'F[1,6]': 1}): 543661591 % 2147481317,
    PentagonMonomial({'F[1,7]': 1}): 1136011766 % 2147481317,
    PentagonMonomial({'F[1,10]': 1}): 425266916 % 2147481317,
    PentagonMonomial({'F[1,11]': 1}): 225991054 % 2147481317,
    PentagonMonomial({'im[1,1]': 1}): 894204753 % 2147481317,
    PentagonMonomial({'F[1,2]': 2}): 1840001269 % 2147481317,
    PentagonMonomial({'F[1,2]': 1, 'F[1,5]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,2]': 1, 'F[1,6]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,2]': 1, 'F[1,7]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,2]': 1, 'im[1,1]': 1}): 1125800503 % 2147481317,
    PentagonMonomial({'F[1,5]': 2}): 1840001269 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'F[1,6]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'F[1,7]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,5]': 1, 'im[1,1]': 1}): 104119689 % 2147481317,
    PentagonMonomial({'F[1,6]': 2}): 1840001269 % 2147481317,
    PentagonMonomial({'F[1,6]': 1, 'F[1,7]': 1}): 510840407 % 2147481317,
    PentagonMonomial({'F[1,6]': 1, 'im[1,1]': 1}): 104119689 % 2147481317,
    PentagonMonomial({'F[1,7]': 2}): 1840001269 % 2147481317,
    PentagonMonomial({'F[1,7]': 1, 'im[1,1]': 1}): 1125800503 % 2147481317,
    PentagonMonomial({'im[1,1]': 2}): 441427281 % 2147481317
}
