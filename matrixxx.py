def razb_spis_1():
    s = input().split()
    n = int(input())
    m = [[] for _ in range(n)]
    for i in range(n):
        for x in range(i, len(s), n):
            m[i].append(s[x])
    return m
def poboch_2():
    n = int(input())
    m = []
    for c in range(n):
        m.append([int(c) for c in input().split()])
    mel = m[0][0]
    for i in range(n):
        for j in range(n):
            if i + j + 1 >= n:
                if m[i][j] > mel:
                    mel = m[i][j]
    print(mel)
def transponir_3():
    n = int(input())
    m = []
    for c in range(n):
        m.append([int(c) for c in input().split()])
    matr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matr[j][i] = m[i][j]
    for i in range(n):
        for j in range(n):
            print(str(matr[i][j]).ljust(3), end=' ')
        print()
def snowflake_4():
    n = int(input())
    m = [['.'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i == n // 2) or (j == n // 2) or (i == j) or (i + j + 1 == n):
                m[i][j] = '*'
    for c in m:
        print(*c)
def simmetr_matr_5():
    n = int(input())
    m = []
    for c in range(n):
        m.append([int(c) for c in input().split()])
    c = 0
    flag = True
    for i in range(n):
        for j in range(n):
            if i + j + 1 != n:
                if m[i][j] == m[n - 1 - j][n - 1 - i]:
                    flag = True
                else:
                    flag = False
                    break
    if flag == True:
        print('YES')
    else:
        print('NO')
def latkv_6():
    n = int(input())
    m = []
    for c in range(n):
        m.append([int(c) for c in input().split()])
    l = [c for c in range(1, n + 1)]
    flag = True
    for i in range(len(l)):
       if sorted(m[i]) == l:
           flag = True
       else:
           flag = False
           break
    for j in range(n):
        a = m[0][j]
        for i in range(1, n):
            if m[i][j] == a:
                flag = False
                break
    if flag:
        print('YES')
    else:
        print('NO')
def ferzi_7():
    chess = [['.' for j in range(8)] for i in range(8)]
    n = input()
    a = '87654321'.index(n[1])
    b = 'abcdefgh'.index(n[0])
    chess[a][b] = 'Q'
    for i in range(8):
        for j in range(8):
            #if ((abs(a - i) == 2) and (abs(b - j) == 1)) or ((abs(b - j) == 2) and (abs(a - i) == 1)):
            if (j == b and i != a) or (i == a and j != b) or (abs(b - j) == abs(a - i) and (i != a)):
                chess[i][j] = '*'
    for c in chess:
        print(*c)
def diag_8():
    n = int(input())
    m = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                m[i][j] = abs(j - i)
    for c in m:
        print(*c)

