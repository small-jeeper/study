# result = {}
# for i in range(1, 16):
#     result[i] = i ** 2
# print(result)
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
# result = {}
# for key in dict1.keys():
#     if key in dict2:
#         result[key] = dict1[key] + dict2[key]
#     else:
#         result[key] = dict1[key]
# for key in dict2.keys():
#     if key not in dict1.keys():
#         result[key] = dict2[key]
# print(result)
#         result[c] += 1
#         result[c] = 1
#     else:
#     if c not in result.keys():
# for c in text:
# print(result)
# result = {}
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# m = {}
# for c in s.split():
#     if c not in m:
#         m[c] = 1
#     else:
#         m[c] += 1
# k = []
# for key, value in m.items():
#     if value == max(m.values()):
#         k.append(key)
# print(min(k))
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# # result = {}
# # for c in pets:
# #     if c[1:] not in result:
# #         result[c[1:]] = [c[0]]
# #     else:
# #         result[c[1:]].append(c[0])
# #print(result)
# # for c in pets:
# #     result.setdefault(c[1:], [])
# #     result[c[1:]].append(c[0])
# # print(result)
# s = input().lower().split()
# for i in range(len(s)):
#     for c in '.,!?:;-':
#         s[i] = s[i].replace(c, '')
# result = {}
# for c in s:
#     result[c]= result.get(c, 0) + 1
# print(result)
# minv = min(result.values())
# m = []
# for key in result.keys():
#     if result[key] == min(result.values()):
#         m.append(key)
# print(min(m))
# s = input().split()
# dd = {}
# for c in s:
#     dd[c] = dd.get(c, 0) + 1
#     if dd[c] == 1:
#         print(str(c), end=' ')
#     else:
#         print(str(c) + '_' + str(dd[c] - 1), end=' ')
# n = int(input())
# di = {}
# for i in range(n):
#     c = input().split(': ')
#     di[c[0].lower()] = c[1]
# m = int(input())
# zapros = []
# for _ in range(m):
#     zapros.append(input().lower())
# for c in zapros:
#     if c.lower() in di:
#         print(di[c])
#     else:
#         print('Не найдено')
# s1, s2 = input().lower(), input().lower()
# for c in s1:
#     if c in '.,!?:;- ':
#         s1 = s1.replace(c, '')
# for c in s2:
#     if c in '.,!?:;- ':
#         s2 = s2.replace(c, '')
# sd1, sd2 = {}, {}
# for i in range(len(s1)):
#     sd1[s1[i]] = sd1.get(s1[i], 0) + 1
# for i in range(len(s2)):
#     sd2[s2[i]] = sd2.get(s2[i], 0) + 1
# if sd1 == sd2:
#     print('YES')
# else:
#     print('NO')
# n = int(input())
# sinon = {}
# for i in range(n):
#     l = input().split()
#     sinon[l[0]] = l[1]
#     sinon[l[1]] = l[0]
# print(sinon[input()])
# n = int(input())
# baza = {}
# for i in range(n):
#     s = input().split()
#     baza[s[0]] = s[1:]
# m = int(input())
# l = [input() for _ in range(m)]
# for c in l:
#     for key, value in baza.items():
#         if c in value:
#             print(key)
# n = int(input())
# tel = {}
# for i in range(n):
#     s = input().lower().split()
#     tel[s[0]] = s[1]
# m = int(input())
# k = []
# for i in range(m):
#     s = input().lower()
#     l = ''
#     for key, value in tel.items():
#         if s == value:
#             l = l + ' ' + key
#     if l == '':
#         l = 'абонент не найден'
#     k.append(l)
# print(*k, sep='\n')
# w = input()
# n = int(input())
# sl = {}
# for i in range(n):
#     s = input().split(': ')
#     sl[s[0]] = int(s[1])
# wr = {}
# for c in w:
#    wr[c] = wr.get(c, 0) + 1
# h = w
# for c in wr:
#     for i in sl:
#         if wr[c] == sl[i]:
#             h = h.replace(c, i)
# print(h)
# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None,\
#           'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige',\
#           'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
# result = {c: colors[c] for c in colors if colors[c] != None}
# print(result)
# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62, 'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654, 'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271, 'anna': 55, 'madlen': 876}
# result = {c: favorite_numbers[c] for c in favorite_numbers if 9 < favorite_numbers[c] < 100}
# print(result)
# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
# result = {months[c]: c for c in months}
# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(c.split(':')[0]): c.split(':')[1] for c in s.split()}
# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {c: [i for i in range(1, c + 1) if c % i == 0] for c in numbers}
# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
# result = {c: [ord(i) for i in c] for c in words}
# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
# result = {c: letters[c] for c in letters if c not in remove_keys}
# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
# result = {c: students[c] for c in students if students[c][0] > 167 and students[c][1] < 75}
# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
# result = {c[0]: (c[1:]) for c in tuples}
# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
# result = [{student_ids[i]: {student_names[i]: student_grades[i]}} for i in range(len(student_ids))]
# print(result)
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
# my_dict = {i: [c for c in my_dict[i] if c <= 20] for i in my_dict}
# print(my_dict)
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# ml = []
# for key, value in emails.items():
#     ml.extend([c + '@' +key for c in value])
# print(*sorted(ml), sep='\n')
# dna = input()
# cod = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
# for c in dna:
#     for k, v in cod.items():
#         if c == k:
#             print(v, end='')
# d = {}
# for c in input().split():
#     d[c] = d.get(c, 0) + 1
#     print(d[c], end=' ')
# d = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,\
#      'D': 2, 'G': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,\
#      'K': 5, 'J': 6, 'X': 8, 'Q': 10, 'Z': 10}
# p = 0
# for c in input():
#     for k,v in d.items():
#         if c == k:
#             p += v
# print(p)
# def build_query_string(params):
#     sp = [k + '=' + str(v) for k, v in sorted(params.items())]
#     return '&'.join(sp)
# print(build_query_string({'name': 'timur', 'age': 28}))
# def merge(dl):
#     d = {}
#     for i in range(len(dl)):
#         for k,v in dl[i].items():
#             d[k] = d.get(k, set())
#             d[k].add(v)
#     return d
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))
# f = {'W': 'write', 'X': 'execute', 'R': 'read'}
# n = int(input())
# d = {}
# for i in range(n):
#     s = input().split()
#     d[s[0]] = [f.get(c) for c in s[1:]]
# m = int(input())
# sp = []
# for i in range(m):
#     sp.append(input().split()[::-1])
# for c in sp:
#         if c[1] in d[c[0]]:
#             print('OK')
#         else:
#             print('Access denied')
n = int(input())
d = {}
for i in range(n):
    m = input().split()
    if m[0] not in d:
        d[m[0]] = {m[1]: 0}
    d[m[0]][m[1]] = d[m[0]].get(m[1], 0) + int(m[2])
for k, v in sorted(d.items()):
    print(k+ ':')
    for c, a in sorted(v.items()):
        print(c, a)