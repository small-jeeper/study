def z1():
    n, m, k, p = int(input()), int(input()), int(input()), int(input())
    print(n - (m + k - p))
def z2():
    s = [c for c in input().split()]
    print(len(s) - len(set(s)))
def z3():
    n = int(input())
    m = set()
    for _ in range(n):
        m.add(input())
    if input() not in m:
        print('OK')
    else:
        print('REPEAT')
def z4():
    m, n = int(input()), int(input())
    bibl = set()
    for _ in range(m):
        bibl.add(input())
    l = []
    for i in range(n):
        if input() in bibl:
            l.append('YES')
        else:
            l.append('NO')
    print(*l, sep='\n')
def z5():
    s1, s2 = set(int(c) for c in input().split()), set(int(c) for c in input().split())
    if s1.isdisjoint(s2):
        print('BAD DAY')
    else:
        print(*sorted(s1.intersection(s2), reverse=True))
def z6():
    s1, s2 = set(int(c) for c in input().split()), set(int(c) for c in input().split())
    if s1 == s2:
        print('YES')
    else:
        print('NO')
def z7():
    m, n = int(input()), int(input())
    matem, csi = set(), set()
    for _ in range(m):
        matem.add(input())
    for _ in range(n):
        csi.add(input())
    print(len(matem - csi))
def z8():
    m, n = int(input()), int(input())
    matem = {input() for _ in range(m)}
    csi = {input() for _ in range(n)}
    if matem == csi:
        print('NO')
    else:
        print(len(matem ^ csi))
def z9():
    s1, s2 = set(c for c in input().split()), set(c for c in input().split())
    print(*sorted(s1.union(s2)), sep=' ')
def z10():
    m, n = int(input()), int(input())
    mc = set()
    for i in range(n + m):
        c = input()
        if c not in mc:
            mc.add(c)
        else:
            mc.remove(c)
    if mc != set():
        print(len(mc))
    else:
        print('NO')
def z11():
    m = int(input())
    mas = set()
    ni = int(input())
    for _ in range(ni):
        mas.add(input())
    for i in range(1, m):
        masi = set()
        ni = int(input())
        for _ in range(ni):
            masi.add(input())
        mas.intersection_update(masi)
    print(*sorted(mas), sep='\n')
