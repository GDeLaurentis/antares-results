"""
Phase space point of arXiv:2110.07541 written in terms of four momenta (parsed from Mathematica).
Mandelstams are given in arXiv:2110.07541, eq. C.1.
"""


import mpmath
import numpy
import re

from fractions import Fraction as Q
from lips import Particles


mpmath.mp.dps = 300

oPs = Particles(6)

# 
string = """{
{-1.547843350404465913384627373230021512490359482045328048605385476723365048997890367083923854137625`70.,0.170606317783005262530418699838904611635997862746868979012283089933254302252118398150648840081459`70.,1.249321854631455859474719612993553455287228443736914570719868296361625992869843388032310403746115`70.,-0.897723468148218761157431977880753422379335561770435991599901955389876954398844045796133111485775`70.},
{-2.028158032459967161814294145623065084956620513370652173432789863067039349916819449774110253529433`70.,0.201344686003876801802311056831318154847021350535546654238206892174347138093637659786263798471953`70.,1.474413842390593902961805376796266803210471307071325893240412674977502664780181288198624665975723`70.,1.378038150203720009587098750273796994845596593095760116427306341733551255317773128486319510877583`70.},
{1.716617118772343700009342454812543201245371275809472205119779038593411035515251516039765865149305`70.,-0.670063380133598004470410077122799702031289207943541340882000398522401479786816674214142762161674`70.,-1.234655719696509112136241767856891986014172474533593197552309732987053630443997019728614062708599`70.,-0.98661778459892725460094332540199829286685673931218487290565754335608286681600437364552028096801`70.},
{0.824997803458607854638766304762458020461777978378894871574938165211207528919202865493604292965783`70.,-0.233694126241285291267777319267363722469887810540635020709275451315743025098806274593033143745944`70.,-0.780622041979255851423601568594990952416678641955990316619732321839787108122239649784011726911358`70.,0.12898704837303194490943117378097845862560263944111762356933798372927823544948620589263330779443`70.},
{0.940577624481963440307716244505708713516427034989858213884914897879472366398908080464332723099415`70.,0.582003840264901929789865335854797010708878591898458363027636733638571557173912241625926571725177`70.,-0.629743236352375659805373918319225575807061324169900003325902129006939668208490308858713314880448`70.,0.386498711332231841126887524893097518625338322991033272061422004281034505499700245790246854421018`70.},
{0.093808836151518080243096514772376662223403706237754931458543238106313468081347354860331226448418`70.,-0.050197337676900698384407696134856352690720786696697634686850865908028492634045350755663304370715`70.,-0.078714698993909139071307735018711744259787310148756946462336787505348250875297697859595965221746`70.,-0.009182657161837779865042145665121256850345254445290147552506830997904175052111160727546280638917`70.}
}"""

string = string.replace("`70.", "").replace("{", "[").replace("}", "]").replace("\n", "")
string = re.sub(r"([\d\+\-\.]+)", r"mpmath.mpc('\1')", string)

four_momenta = eval(string)

for i, oP in enumerate(oPs):
    oP.four_mom = four_momenta[i]

# check phase space point satisfies momentum conservation and is on-shell
assert numpy.max(abs(oPs.total_mom)) < 10 ** - 80
assert numpy.max(abs(numpy.array(oPs.masses))) < 10 ** - 80

# check mandelstams as given in arXiv:2110.07541, eq. C.1
assert Q(str(oPs("s12").real)).limit_denominator(10 ** 9) == Q('5')
assert Q(str(oPs("s23").real)).limit_denominator(10 ** 9) == Q('-1/3')
assert Q(str(oPs("s34").real)).limit_denominator(10 ** 9) == Q('11/13')
assert Q(str(oPs("s456").real)).limit_denominator(10 ** 9) == Q('17/19')
assert Q(str(oPs("s156").real)).limit_denominator(10 ** 9) == Q('-23/29')
assert Q(str(oPs("s56").real)).limit_denominator(10 ** 9) == Q('1/7')
assert Q(str(oPs("s345").real)).limit_denominator(10 ** 9) == Q('4304788/896077')
assert Q(str(oPs("s45").real)).limit_denominator(10 ** 9) == Q('2911673/3928953')
assert Q(str(oPs("s16").real)).limit_denominator(10 ** 9) == Q('-186065/1998941')
assert oPs("tr5(1|2|3|4)").imag < 0
