# n = int(input())
# matr = [[1] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if (i > j and j < n - i -1) or (i < j and j > n - i -1):
#             matr[i][j] = 0
# for i in matr:
#     print(*i, sep=' ')
# n, m = [int(c) for c in input().split()]
# l = [i for i in range(1, m + 1)]
# matr = [[0] * m for _ in range(n)]
# j = 0
# for i in range(n):
#     matr[i] = l[j:]+l[:j]
#     if j == m - 1:
#         j = 0
#     else:
#         j += 1
# for c in matr:
#      print(*c, sep=' ')
# ЗАПОЛНЕНИЕ МАТРИЦЫ ЗМЕЙКОЙ
# n, m = [int(i) for i in input().split()]
# matr = [[0] * m for _ in range(n)]
# a = 1
# for i in range(n):
#     if i % 2 == 0:
#         for j in range(m):
#             matr[i][j] = a
#             a += 1
#     else:
#         for j in range(m - 1, -1, -1):
#             matr[i][j] = a
#             a += 1
# for c in matr:
#     print(*c, sep=' ')
# n, m = [int(i) for i in input().split()]
# matr = [[0] * m for _ in range(n)]
# a = 1
# for j in range(m):
#     for c in range(j, -1, -1):
#         r = j - c
#         matr[r][c] = a
#         a += 1
#         if r == n - 1:
#             break
# if m > 1:
#     for i in range(1, n):
#         x = i + j
#         for r in range(i, n):
#             c = x - r
#             matr[r][c] = a
#             a += 1
#             if c == 0:
#                 break
# else:
#     for i in range(1, n):
#         matr[i][0] = a
#         a += 1
# for i in range(n):
#     for j in range(m):
#         print(str(matr[i][j]).ljust(3), end=' ')
#     print()
# n, m = (int(c) for c in input().split())
# matr = [[0] * m for _ in range(n)]
# low_n, low_m = 0, 0
# high_n, high_m = n - 1, m - 1
# c = int((n + 1) / 2)
# a = 0
# for x in range(c):
#     for j in range(low_m, high_m + 1):
#         a += 1
#         matr[x][j] = a
#     if a >= n * m:
#         break
#     for i in range(low_n + 1, high_n + 1):
#         a += 1
#         matr[i][high_m] = a
#     if a >= n * m:
#         break
#     for j in range(high_m - 1, low_m - 1, -1):
#         a += 1
#         matr[high_n][j] = a
#     if a >= n * m:
#         break
#     for i in range(high_n - 1, low_n, -1):
#         a += 1
#         matr[i][j] = a
#     if a >= n * m:
#         break
#     low_m += 1
#     low_n += 1
#     high_m -= 1
#     high_n -= 1
# for i in range(n):
#     for j in range(m):
#         print(str(matr[i][j]).ljust(3), end=' ')
#     print()
