# Opgave 1.4 Dylan van Eck
# 1702786
#
# Deze functie maakt eerst 100 lijsten van 23 elementen met een random getal van 1 tot 365
# vervolgens bekijkt hij of er meerdere element in een lijst gelijk zijn als dat zo is zet hij de nummer van
# klassen met verjaardagen 1 omhoog
#
# RETURN:
# number_of_birthday_class : int
# aantal lijsten met een klas waarbij er meerdere studenten op dezelfde dag jarig is


import random

def birthday_calculator():
    list = []
    number_of_birthday_class = 0
    for j in range(100):
        for i in range(23):
            list.append(random.randint(1, 365))
            if(i == 22):
                multi_list = set(list)
                if(len(multi_list) < len(list)):
                    number_of_birthday_class = number_of_birthday_class + 1
                list = []
    return number_of_birthday_class

print(birthday_calculator())