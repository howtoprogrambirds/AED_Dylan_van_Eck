# WEEK 1 in de les

#  0            99
# [25, 25,..... 25]
#
# hoe maak je een lijst van 100 25 ints in python
# a = [25] * 100
# b = [25 for i in range(100)]
#             |
#             dummy
#
# hoe maak je honderd kwadraten in een lijst
# c = [i*i for i in range(1, 101)]
#
# hoe maak je honderd kwadraten in een lijst met alleen even
# d = [i*i for i in range(1, 101, 2)]
# e = [i*i for i in range(1, 101) if i%2 == 0]


# ZEEF VAN ERATOSTHENES:
#         [0, 1, 2, 3, 4..... 1000]
# mark     f  f  t  t  f
#
# je kijkt zet alle nummers of false, vervolgens ga je elk cijfer langs en
# alle kwadraten ofschrijven en die cijfers op true zetten. Zodat je alle
# priemgetallen over krijgt


# TUPLE:
# (3)     = 3 int
# (3,)    = tuple
#
# 3 * (3)     = 9 int
# 3 * (3,)    = (3,3,3) tuple
#
#
# van tuple naar list
# t= 3*(3,)
# type van t is nu een tuple
#
# a = list(t)
# type van a is nu een list geworden
#
# s = tuple(a)
# type van s is nu weer een tuple geworden
#
# je kan alle uniek elementen uit een lijst halen door deze manier
 print(set([2,2,2,3,3,3,4,3,2])) # -> {2, 3, 4}
#
# ik wil nu alle unieke lijsten in één lijst
# a = [[1,2],[1,2],[1,2,3],[1,2]]
# s = set(a) -> kan niet


# SLICING:
#      0   1   2  3  4  5   6  7
# a = [22, 14, 2, 7, 8, 16, 7, 9]
#      \__________/
# ik wil deze selectie
#
#                   ____exclusief
#                  /
#          b = a[0:4] <------nieuwe lijst
#                \______niet verplicht
#
# dus als je nu b verandert wordt a niet verandert
# Bij slicing maak je kan je dus niet de huidige lijst veranderen


# STRING:
# s = "kees"
# s.replace(ee,oo)
#
# s = "kees"
# s =s.replace(ee,oo)
#
# bij de eerste wijst s niet meer naar koos
# en bij de tweede wijst de s wel naar koos
