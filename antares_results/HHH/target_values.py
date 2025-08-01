from pyadic import ModP

target_values_red_C = {
    # adjacent
    'ered_1x2x3x4_1': (-0.04506530270624152 + 0j),
    'ered_1x2x3x4_2': (-0.20524437792025566 + 0j),
    'ered_1x2x3x4_4': (-0.01719670235391843 + 0j),
    # non adjacent
    'ered_1x3x2x4_1': (-0.05409375557846232 + 0j),
    'ered_1x3x2x4_2': (0.01813388664558044 + 0j),
    'ered_1x3x2x4_5': (0.05413954634454883 + 0j),
}

target_values_red_FF = {
    # adjacent
    'ered_1x2x3x4_1': ModP("1384078911 % 2147483629"),
    'ered_1x2x3x4_2': ModP("1073263483 % 2147483629"),
    'ered_1x2x3x4_4': ModP("1250293197 % 2147483629"),
    # non adjacent
    'ered_1x3x2x4_1': ModP("594539899 % 2147483629"),
    'ered_1x3x2x4_2': ModP("635879207 % 2147483629"),
    'ered_1x3x2x4_5': ModP("1604062102 % 2147483629"),
}

target_values_pp_C = {
    # effective pentagons
    'e_1x2x3x4': (-14.50009611985968 + 18.819750627558946j),
    'e_1x3x2x4': (35.34057152090142 - 41.55442146499347j),
    # effective boxes
    'd_1x2x3': (-1.2326135768748212 + 1.05537838669824j),
    'd_1x3x2': (-10.085217633244733 + 11.200457394308154j),
    'd_1x3x24': (-92.8507393227681 + 56.81348794315807j),
    'd_1x23x4': (27.936041214724053 - 33.54924957016864j),
    'd_12x3x4': (85.7015062988589 - 40.92494404717289j),
    # triangles
    'c_1x23': (34.13737251074167 - 31.730169711798787j),
    'c_1x3': (-39.99705096654001 + 37.17665191544665j),
    'c_3x12': 0,
    'c_1x2': 0,
}

target_values_pp_FF = {
    # effective pentagons
    'e_1x2x3x4': ModP("1767987987 % 2147483629"),
    'e_1x3x2x4': ModP("1613363934 % 2147483629"),
    # effective boxes
    'd_1x2x3': ModP("2126846350 % 2147483629"),
    'd_1x3x2': ModP("430604011 % 2147483629"),
    'd_1x3x24': ModP("635671079 % 2147483629"),
    'd_1x23x4': ModP("410642131 % 2147483629"),
    'd_12x3x4': ModP("1344689792 % 2147483629"),
    # triangles
    'c_1x23': ModP('465279123 % 2147483629'),
    'c_1x3': ModP('80034263 % 2147483629'),
    'c_3x12': 0,
    'c_1x2': 0,
}

target_values_pm_C = {
    # effective pentagons
    'e_1x2x3x4': (7.523045180058341 + 8.474563572135906j),
    'e_1x3x2x4': (7.032461726585953 + 8.3210979776325j),
    # effective boxes
    'd_1x2x3': (1.3164248355227215 + 2.55545321622744j),
    'd_1x3x2': (3.293047846839623 + 3.5582280868535165j),
    'd_1x3x24': (216.0636554909965 + 124.57717092833963j),
    'd_1x23x4': (-18.93675496286851 - 13.897548269844993j),
    'd_12x3x4': (-213.76280265495694 - 105.78858356013824j),
    # triangles
    'c_1x23': (1.7042104258056312 + 3.1732193891969382j),
    'c_1x3': (-109.34404123048252 - 203.59729436679874j),
    'c_3x12': (110.97572974551987 + 206.63547882726456j),
    'c_1x2': (147.86303178595549 - 28.4298233383368j),
}

target_values_pm_FF = {
    # effective pentagons
    'e_1x2x3x4': ModP("1983805603 % 2147483629"),
    'e_1x3x2x4': ModP("885906902 % 2147483629"),
    # effective boxes
    'd_1x2x3': ModP("1287159176 % 2147483629"),
    'd_1x3x2': ModP("168496218 % 2147483629"),
    'd_1x3x24': ModP("1497608307 % 2147483629"),
    'd_1x23x4': ModP("605344672 % 2147483629"),
    'd_12x3x4': ModP("851850539 % 2147483629"),
    # triangles
    'c_1x23': ModP('966056998 % 2147483629'),
    'c_1x3': ModP('200352517 % 2147483629'),
    'c_3x12': ModP('2059152025 % 2147483629'),
    'c_1x2': ModP('554280909 % 2147483629'),
}

# Result for the pentagon subamplitude (A5 in the paper) for all helicities:
#
# h1 = -1, h2 = +1
#            0+1,res      -1.738447456741164       0.058505359249947       1.739431641919506
# h1 = +1, h2 = +1
#            0+1,res       3.207821962681104      -3.487653212553105       4.738549005264296
# h1 = +1, h2 = -1
#            0+1,res      -1.341029848029631       0.833458607125174       1.578928213408517
#  h1 = -1, h2 = +1
#            0+1,res       3.585123238826661       3.168515811948611       4.784621310839901
#
# The format is (Re, Im, |Re+j*Im|).
