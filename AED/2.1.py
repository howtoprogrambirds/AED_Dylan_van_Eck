# def machtv3(a,n):
#     print (n, a)
#     m = 1
#     while n > 1:
#         if n%2 == 0:
#             return a**2 * machtv3(a, n//2)
#         else:
#             return a*machtv3(a, n - 1)
#     return m
#
# print(machtv3(2,6))

def machtv3(a,n):
    m = 1
    while n > 0:
        # print(m)
        if n%2 == 0:
            a = a*a
            n = n // 2
        else:
            m = m * a
            n = n - 1
    return m

print("test ", machtv3(2,1000))
print("controle ", 2**1000)