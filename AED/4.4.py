m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

def F(n,a):
    a.append([1]*(n+1));
    for i in range(len(m)-1):
        a.append([0]*(n+1))
        a[-1][0] = 1;

    for i in range(1, len(m)):
        for j in range(1, n+1):
            if j >= m[i]:
                a[i][j] = a[i - 1][ j] + a[i][ j - m[i]]
            if j < m[i]:
                a[i][j] = a[i - 1][ j]
    print(a)




a = [];
F(7,a)