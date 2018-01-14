def swap(a,i,j):
    a[i],a[j] = a[j],a[i]

import random


def qsort(a,low=0,high=-1):
    check = 0
    if high == -1:
        high = len(a) -1
    if low < high:
        #swap(a,low, random.randint(low,high))
        b = a[low:high + 1]
        swap(a,low, low+b.index(min(b)))
        m = low
        for j in range(low+1,high+1):
            check = check + 1
            if a[j] < a[low]:
                print("$")
                m += 1
                swap(a,m,j)
                            # low < i <= m : a[i] < a[low]
                            # i > m        : a[i] >= a[low]
        print("this round how many checks: ",check)
        swap(a,low,m)
                            # low <= i < m : a[i] < a[m]
                            # i > m              : a[i] >= a[m]
        if m > 0:
           qsort(a,low,m-1)
        qsort(a ,m+1,high)



my_randoms = []
for i in range(100):
    my_randoms.append(random.randrange(1,10000,1))

print(my_randoms)

qsort(my_randoms)

print(my_randoms)

a = [2,1,3,4,5,2,1,3,4]
low = 5
high = 7
# b = a[low:high+1]
# print(low+b.index(min(b)))