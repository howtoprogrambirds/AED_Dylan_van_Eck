# Opgave 1.2 Dylan van Eck
# 1702786
#
# Deze functie maakt van alle characters van de meeegegeven lijst een lijst "s" met ASCII-waardes.Vervolgens
# wordt van elke element van de lijst "s" 48 er van afgetrokken en in "number" gestopt om de cijfers te kunnen ontmantelen.
# Want nu kan je door een makkelijke if statement die checken of number 0 tot en met 9 bevat. Als dat zo is wordt het eventuele
# vorige nummer keer 10 gedaan en plus het huidige nummer. Zo niet wordt de buffer geleegt keer de minflag gedaan(als die true is) en gestopt in de return lijst
#
# PARAMETER:
# -----------
# str1 : string
# De meegeven string waar de nummers en chars in staan
#
# RETURN:
# list : list
# Een lijst met alle nummers uit de meegegeven string


def getNumbers(str1):
    s = [ord(c) for c in str1]
    size = len(s)
    current_number = 0;
    numberflag = False;
    minflag = False
    list = []
    # print(s)
    for i in range(0,size):
        number =  s[i] - 48
        if(number >= 0 and number <= 9):
            tenth = 10 * numberflag
            past_number_mult_ten = current_number * tenth
            current_number =  past_number_mult_ten  + number
            numberflag = True

        elif(s[i] == 45):
            minflag = True

        else:
            if (current_number != 0):
                if(minflag == True):
                    current_number = current_number * -1
                    list.append(current_number)
                    minflag = False
                else:
                    list.append(current_number)
                current_number = 0
                numberflag = False
    if(current_number != 0):
        list.append(current_number)
    return list

str1 = "een1203zin45 6met-632meerdere+7777getallen"
print(getNumbers(str1))