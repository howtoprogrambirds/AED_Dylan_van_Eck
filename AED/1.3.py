# Opgave 1.3 Dylan van Eck
# 1702786
#
# Dit programma bevat een list met alleen die volledig bestaat uit 1000-2 true's.
# vervolgens wordt de methoede van de zeef van eratosthenes maakt hij de locaties van de all_true_list
# false. Als eind kijkt hij welke true en nog staan en geeft de locatie plus 2 terug voor de priemgetallen
#
# PARAMETER:
# -----------
# max : int
# maximale cijfer waarbij je alle priemgetallen eruit wilt filteren
#
# RETURN:
# list: list
# list die alle priemgetallen bevat


def find_prim(max):
    all_true_list = [True for i in range(2,max+1)]
    list = []
    first_number = 2
    multi = 1
    while (first_number < max):
        current_number = first_number * multi
        multi = multi + 1
        if (current_number > max):
            first_number = first_number + 1
            multi = 1
            current_number = 0
        else:
            if(current_number != first_number and  all_true_list[current_number-2] != False):
                all_true_list[current_number-2] = False

    for i in range(max-1):
        if (all_true_list[i] == True):
            list.append(i+2)
    return list


print(find_prim(1000))


