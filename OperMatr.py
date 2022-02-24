# n, m = [int(c) for c in input().split()]
# # matr1 = [[0] * m for _ in range(n)]
# matr1, matr2 =[], []
# for c in range(n):
#     matr1.append([int(c) for c in input().split()])
# input()
# for c in range(n):
#     matr2.append([int(c) for c in input().split()])
# for i in range(n):
#     for j in range(m):
#         print(matr1[i][j] + matr2[i][j], end=' ')
#     print()
# matr1, matr2 =[], []
# n, m = [int(c) for c in input().split()]
# for c in range(n):
#     matr1.append([int(c) for c in input().split()])
# input()
# m, k = [int(c) for c in input().split()]
# for c in range(m):
#     matr2.append([int(c) for c in input().split()])
# rez = [[0] * n for _ in range(k)]
# for i in range(n):
#     for c in range(k):
#         for j in range(m):
#             rez[i][c] += matr1[i][j] * matr2[j][c]
# for i in range(n):
#     for j in range(k):
#         print(str(rez[i][j]).ljust(3), end=' ')
#     print()
# Возведение квадратной матрицы в степень
# n = int(input())
# matr = []
# for c in range(n):
#     matr.append([int(c) for c in input().split()])
# m = int(input())
# matr1 = [[0] * n for _ in range(n)]
# for i in range(n):
#     matr1[i] = matr[i]
# for x in range(m - 1):
#     rez = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for c in range(n):
#             for j in range(n):
#                 rez[i][c] += matr1[i][j] * matr[j][c]
#     for i in range(n):
#         matr1[i] = rez[i]
# for i in range(n):
#      for j in range(n):
#          print(str(rez[i][j]).ljust(3), end=' ')
#      print()
s = input().split()
n = int(input())
m = [[0] for _ in range(n)]
print(m)
for i in range(n):
    for x in range(0, len(s), n - 1):
        m[i].append(s[x])
print(m)