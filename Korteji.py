# # n,m,k,x,y,z,t,a = int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input())
# # x4 = n + m - x - t
# # x5 = n + k - z - t
# # x6 = m + k - y - t
# # x1 = n - t - x4 - x5
# # x2 = m - t - x4 - x6
# # x3 = k - t - x5 - x6
# # print(x1 + x2 + x3)
# # print(x4 + x5 + x6)
# # print(a - x1 -x2 -x3 - x4 - x5 - x6 - t)
# # a, b, c = set((int(c) for c in input().split())),\
# #           set((int(c) for c in input().split())),\
# #           set((int(c) for c in input().split()))
# # l = list(range(11))
# # for i in l:
# #     if i not in a | b | c:
# #         print(i, end=' ')
# # w = {i.strip(')?!.,:;(').lower() for i in sentence.split()}
# # l = [i for i in w if len(i) < 4]
# # print(*sorted(l, reverse=False))
# # files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# # files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
# # m = {i.lower() for i in files if i[i.index('.')+1:len(i)].lower() == 'png'}
# # print(*sorted(m))
# # users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
# #          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
# #          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
# #          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
# #          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
# #          {'name': 'John', 'phone': '233-421-32', 'email': ''},
# #          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
# #          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
# #          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
# #          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
# #          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
# #          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
# #          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
# #          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
# #          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
# #          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# # m = []
# # for c in users:
# #     if c['phone'][-1] == '8':
# #         m.append(c['name'])
# # print(*sorted(m))
#
# # m = [c['name'] for c in users if c['phone'][-1] == '8']
# # print(*sorted(m))
# # print(*sorted([c['name'] for c in users if c['phone'][-1] == '8']))
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# print(*sorted([c['name'] for c in users if 'email' not in c or c['email'] == '']))
# numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
# print(*[numbers[n] for c in input() for n in numbers.keys() if c == n], end=' ')
# inform = {'CS101': [3004, 'Хайнс', '8:00'], 'CS102': [4501, 'Альварадо', '9:00'], 'CS103': [6755,	'Рич', '10:00'], 'NT110': [1244, 'Берк', '11:00'], 'CM241': ['1411', 'Ли', '13:00']}
# h = input()
# print('{}: {}, {}, {}'.format(h, *inform[h]))
# shifr = {".":'1', ",":'11', "?":'111', "!":'1111', ":":'11111',
#         "A":'2', "B":'22', "C":'222',
#         "D":'3', "E":'33', "F":'333',
#         "G":'4', "H":'44', "I":'444',
#         "J":'5', "K":'55', "L":'555',
#         "M":'6', "N":'66', "O":'666',
#         "P":'7', "Q":'77', "R":'777', "S": '7777',
#         "T":'8', "U":'88', "V":'888',
#         "W":'9', "X":'99', "Y":'999', "Z": '9999',
#         " ":'0'
#         }
# j = input().upper()
# for k in j:
#     for key, value in shifr.items():
#         if k == key:
#             print(value, end='')
# morz = {'A': '.-', 'J': '.---',	'S': '...', '1': '.----', 'B': '-...', 'K': '-.-', 'T': '-', '2': '..---',\
#         'C': '-.-.', 'L': '.-..', 'U': '..-', '3': '...--', 'D': '-..',	'M': '--',	'V': '...-', '4': '....-',\
#         'E': '.', 'N': '-.', 'W': '.--', '5': '.....', 'F': '..-.', 'O': '---', 'X': '-..-', '6': '-....',\
#         'G': '--.', 'P': '.--.', 'Y': '-.--', '7': '--...', 'H': '....', 'Q': '--.-', 'Z': '--..', '8': '---..',\
#         'I': '..', 'R': '.-.', '0': '-----', '9': '----.'
#         }
# s = input().upper()
# for i in s:
#     for c in morz:
#         if i == c:
#             print(morz[c], end=' ')
