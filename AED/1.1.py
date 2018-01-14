# Opgave 1.1 Dylan van Eck
# 1702786
#
# Deze functie gaat via een for loop door de meegegeven list heen.
# Hierbij kijkt hij wat het grootste getal is in de lijst. Ook bevat hij twee
# assert error, zodat hij kan aangeven wanneer de lijst geen int of float bevat
# en wanneer de lijst geen elementen bevat.
#
# PARAMETERS:
# ------------
# a : array
# a is een array met int en doubles
#
# RETURN:
# max : int
# het grootste int waarde in de lijst


def mymax(a):
    size = len(a)
    assert size != 0, "size is zero"
    m = a[0]
    for i in range(1,size):
        assert type(a[i]) == int or type(a[i]) == float, "value is not a integer or float: %r" %a[i]
        if a[i] > m:
            m = a[i]
    return m


a = [9.0]
print(mymax(a))
print((type(3.0) == int or type(3.0) == float) == True)