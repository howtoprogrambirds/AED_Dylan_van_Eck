def mybin(n):
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return mybin(n // 2) + str(n % 2)


print(mybin(5))
print(mybin(10))
print(mybin(3))
print(mybin(1))