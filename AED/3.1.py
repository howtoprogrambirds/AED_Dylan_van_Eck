def check(a,i):  # ga na of i aan a toegevoegd kan worden
    n = len(a)
    return not (i in a or # niet in dezelfde kolom
                i+n in [a[j]+j for j in range(n)] or # niet op dezelfde diagonaal
                i-n in [a[j]-j for j in range(n)]) # niet op dezelfde diagonaal

def printQueens(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if a[i] == j:
                print("#", end= " ")
            else:
                print("*", end= " ")
        print()
    print()


def queensproblem(buffer, N):
    global solutions
    for i in range(0, N):
        if check(buffer, i):
            buffer.append(i)
            if len(buffer) == N:
                solutions.append(buffer[:])
            else:
                queensproblem(buffer, N)
            print(buffer[-1])
            del buffer[-1]


def rsearch(N):
    global a
    for i in range(N):
        if check(a, i):
            a.append(i)
            if len(a) == N:
                print(a) # geschikte a gevonden
            elif rsearch(N):
                    return True
            del a[-1] # verwijder laatste element
    return False

solutions = [] # a geeft voor iedere rij de kolompositie aan
buffer = []
t = 0

queensproblem(buffer, 4)
print(solutions)
print("len(a):",len(solutions))