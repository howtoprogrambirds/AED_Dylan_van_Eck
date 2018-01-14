def B(n,k,a):
    if n < 0 or k < 0:
        return -1;
    else:
        for row in range(k+1):
            a.append([0]*(n+1));
            a[-1][0] = 1;
        print(a)
        for i in range(1, n+1):
            for row in range(1, k+1):
                a[row][i] = a[row-1][i] + a[row-1][i-1]
        print(a[k][n])
        return a[k][n];

a = [];
print(B(3,6,a))
print(a)
