"""
Target values for the trees and one-loop scalar-integral ceofficients of the six-gluon amplitudes as in arXiv:1904.04067,
at associated phase space point given in :code:momenta.py. The format is that of a dictionary: (helicity, coefficient).
Import with

.. code-block:: python

    from amplitudes.jjjj.target_values import target_values

"""


target_values = {
    'pmpmpm': {
        'tree': (0.00650218713 + -0.00016520442j),
        'box(1)': (0.50827657317 + 0.03313946567j),
        'box(2)': (-0.06649276534 + 0.07025091191j),
        'box(4)': (-0.11869521602 + 0.10169890469j),
        'box(5)': (-0.00993074888 + -0.00359098501j),
        'box(6)': (-0.00390998049 + -0.00763359323j),
        'triangle(1)': (-0.01230906573 + 0.00075628439j),
        'triangle(3)': (-0.01674345522 + 0.06366127927j),
        'triangle(4)': (0.00491490166 + 0.00971265451j),
        'triangle(6)': (0.07675962497 + -0.54065748109j),
        'triangle(19)': (781.13084891351 + 157.99763888173j),
        'triangle(20)': (0.04033477565 + 0.02040533354j),
        'bubble(1)': (-0.00829879202 + 0.00495365520j),
        'bubble(2)': (0.26291289714 + -0.23359481086j),
        'bubble(5)': (-0.13159543632 + 0.01787013298j),
        'rational': (0.06808720403 + -0.04724680350j)
    },
    'ppmpmm': {
        'tree': (2.55238208392 - 59.2622060022j),
        'box(1)': (21590.1792859 + 2452.17047139j),
        'box(2)': (-25.4103531908 - 28.3226818304j),
        'box(3)': (-8.639646271 - 812.252807072j),
        'box(4)': (261.735725103 - 95.5166292286j),
        'box(5)': (-1.82308714139 - 2.18061524652j),
        'box(6)': (-1367.27933442 - 2968.29837426j),
        'box(7)': (843093.108628 + 473351.884046j),
        'box(8)': (173.365643028 + 84.2985457064j),
        'box(9)': (2396126.46839 - 2951266.89121j),
        'box(12)': (2970204.20451 + 4133453.58433j),
        'box(13)': (480.903506474 + 417.291690203j),
        'box(14)': (380789.224106 + 625892.460272j),
        'box(15)': (229.536638729 - 1262.23979525j),
        'box(16)': (3082755.05961 - 9323687.40712j),
        'box(22)': (245279.425738 + 623993.01368j),
        'box(25)': (79.9208390062 - 116.380054283j),
        'box(28)': (4603202.35255 + 2032551.37179j),
        'triangle(3)': (-1885.17135583 + 5509.38815038j),
        'triangle(5)': (17738.6484944 + 11481.0176745j),
        'triangle(8)': (3107.58744798 - 5573.28197924j),
        'triangle(10)': (-19662.3267599 - 15928.0277053j),
        'triangle(11)': (28714.9828845 - 21744.1683643j),
        'triangle(15)': (-70731.220762 - 17161.5016493j),
        'triangle(16)': (-46654.3346408 - 50224.8500106j),
        'triangle(18)': (-148892.601461 + 89774.3311937j),
        'triangle(24)': (23734.2157012 - 47355.0277398j),
        'triangle(25)': (135.060938408 - 698.995428844j),
        'triangle(30)': (-231668.69862 - 101514.086731j),
        'triangle(31)': (-1741.57219014 + 2027.50571056j),
        'triangle(41)': (-3781.03751395 - 2750.19335663j),
        'triangle(42)': (6656.37726203 + 16211.8695673j),
        'triangle(49)': (-29944.515258 + 11972.3809498j),
        'triangle(50)': (119535.140872 + 59595.451557j),
        'bubble(1)': (3.36965959881 + 56.134069777j),
        'bubble(3)': (114.603613152 + 2.99364320705j),
        'bubble(4)': (102.876236205 + 10.4085965403j),
        'bubble(5)': (-383.353056093 + 137.171400913j),
        'bubble(10)': (-360.707891825 - 129.992444606j),
        'bubble(11)': (-478.240876665 + 3563.09285533j),
        'bubble(13)': (-76.5124662906 - 12.450164844j),
        'bubble(14)': (50.7963957413 - 338.194934828j),
        'bubble(17)': (574.298071423 - 94.0718628167j),
        'bubble(18)': (104.212277031 - 2746.24558667j),
        'rational': (64.4299867569 + 735.319442021j)
    },
    'ppmppm': {
        'tree': (9.37859664389 + 12.9623868815j),
        'box(1)': (-4256.12887346 + 3796.82085291j),
        'box(3)': (-6934.49328454 - 5659.29425171j),
        'box(4)': (51771.5167526 + 75579.8112276j),
        'box(5)': (-474297.366261 - 4335.97107694j),
        'box(8)': (-207420.275907 - 87972.0840106j),
        'triangle(3)': (-101.96689207 - 107.214100873j),
        'triangle(4)': (-632.743831168 + 373.746129779j),
        'triangle(5)': (-4238.51817299 - 8407.80997061j),
        'triangle(6)': (5879.75891564 - 28518.2102654j),
        'triangle(7)': (4112.72928715 + 9281.13341362j),
        'triangle(9)': (-6657.06526878 + 30094.603536j),
        'bubble(1)': (-2258.57218995 + 599.999378482j),
        'bubble(3)': (-1982.84136654 + 1728.95283087j),
        'bubble(4)': (13.8498540036 + 5.27628314692j),
        'bubble(5)': (-4388.2409255 - 18544.1327545j),
        'bubble(6)': (-764.323651491 + 3069.17476404j),
        'rational': (-951.981964887 - 58.9680761785j)
    },
    'pppmmm': {
        'tree': (0.131934423962 - 0.0788880023501j),
        'box(1)': (30.2548518398 + 50.5136566848j),
        'box(2)': (0.719840581603 - 1.35857181197j),
        'box(3)': (0.20924117344 + 0.0418135395086j),
        'box(4)': (0.000271991288873 - 0.000543217748847j),
        'box(5)': (4.57641142214 - 7.57203490681j),
        'box(6)': (-238.520608998 - 179.148602566j),
        'triangle(6)': (-0.91092829785 + 1.55477329882j),
        'triangle(8)': (0.91092829785 - 1.55477329882j),
        'triangle(9)': (13.1319412883 + 4.9254439987j),
        'triangle(12)': (-13.1319412883 - 4.9254439987j),
        'bubble(1)': (-0.0126706539887 + 0.0110741130203j),
        'bubble(3)': (-0.0296373156933 + 0.0222416931182j),
        'bubble(4)': (0.213472857171 + 0.087602974357j),
        'rational': (0.0546980290979 - 0.081743885478j)
    },
    'pppmpm': {
        'tree': (-0.00243664878385 + 0.00145379603536j),
        'box(1)': (-0.604077031481 - 0.81129216839j),
        'box(2)': (-0.083662480871 + 0.142483002728j),
        'box(3)': (3.31143572915 + 1.28147018394j),
        'box(4)': (179.414842014 - 56.7027964724j),
        'box(5)': (72.9652981737 - 298.609483942j),
        'box(6)': (-115378.22552 - 98838.672815j),
        'box(11)': (0.273893846635 + 2.44234157577j),
        'triangle(4)': (2.63271191551 + 2.64967674486j),
        'triangle(5)': (5.95819803058 - 1.38584701352j),
        'triangle(6)': (-2.69268849172 - 2.99452308828j),
        'triangle(8)': (-6.48162212031 + 1.24928850025j),
        'triangle(9)': (-774.421365877 + 3174.60368008j),
        'triangle(11)': (-161.04170732 + 2278.79454921j),
        'triangle(12)': (819.557054489 - 154.312618152j),
        'triangle(14)': (543.049415674 - 192.62734575j),
        'triangle(24)': (7.86498751622 + 1.49560335777j),
        'triangle(25)': (-0.111342533229 + 0.138303529175j),
        'bubble(1)': (-0.666496340071 - 0.48459061731j),
        'bubble(3)': (-0.506160090718 - 0.241319729123j),
        'bubble(4)': (4.12238076608 - 5.14120806122j),
        'bubble(5)': (-1.01107067853 + 0.473439557676j),
        'bubble(9)': (0.00844956589809 - 0.02685902268j),
        'bubble(10)': (0.00204239788095 - 0.00273366541615j),
        'rational': (-0.112172340673 - 0.233454221396j)
    },
    'ppppmm': {
        'tree': (-0.272590356611 + 0.115683709749j),
        'box(1)': (-50.927492799 - 92.4658236082j),
        'box(2)': (-10.6748798857 + 13.5426906173j),
        'box(3)': (324.165397764 + 179.553006429j),
        'box(4)': (74.464236239 + 144.08548646j),
        'box(5)': (1035.10632869 - 737.40532981j),
        'triangle(5)': (2.14887296896 - 2.72616854766j),
        'triangle(7)': (-2.14887296896 + 2.72616854766j),
        'triangle(8)': (-24.2119315191 - 12.6890461247j),
        'triangle(10)': (24.2119315191 + 12.6890461247j),
        'bubble(1)': (0.00274947242032 - 0.000495704963256j),
        'bubble(3)': (0.00816997852345 - 0.00149048804021j),
        'bubble(4)': (0.281206051864 + 0.165405572644j),
        'rational': (0.139507185 - 0.0018007609397j)
    },
    'pppppm': {
        'rational': (-0.0219970948427 + 0.022748498601j)
    },
    'pppppp': {
        'rational': (0.000968961338776 + 0.00062439507549j)
    },
}
