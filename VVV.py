n, m = [int(i) for i in input().split()]
matr = [["." for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if ((i % 2 != 0) and (j % 2 == 0)) or (j % 2 != 0) and (i % 2 == 0):
            matr[i][j] = '*'
for c in matr:
    print(*c, sep=' ')
