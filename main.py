from test_monom import test
from monom import Monom
from repo import *
from utils import *
test()

monoame = citire()
monoame.sort(key=lambda m: m.nr1(), reverse=True)

nivele = [Nivel()]
grupe = [Grupa()]
nr_de_1 = monoame[0].nr1()

# region Grupe init
nivele[0].nivel_factorizare = 0
for m in monoame:
    if m.nr1() == nr_de_1:
        grupe[-1].nr1 = nr_de_1
        grupe[-1].monoame.append(m)
    else:
        nivele[0].grupe.append(grupe[-1])
        grupe.append(Grupa())
        nr_de_1 = m.nr1()
        grupe[-1].nr1 = nr_de_1
        grupe[-1].monoame.append(m)
nivele[0].grupe.append(grupe[-1])
#endregion

# region primul tabel
while True: # loop nivele
    n = Nivel()
    n.nivel_factorizare = len(nivele)
    n.grupe.append(Grupa())

    for i in range(len(nivele[-1].grupe)-1): # loop grupe
        for i1 in range(len(nivele[-1].grupe[i].monoame)):
            for i2 in range(len(nivele[-1].grupe[i+1].monoame)):
                try:
                    s = nivele[-1].grupe[i].monoame[i1] + nivele[-1].grupe[i + 1].monoame[i2]
                    for m_ in n.grupe[-1].monoame:
                        if m_ == s: break
                    else: n.grupe[-1].add(s)
                except ValueError: pass
        if len(n.grupe[-1]) == 0:
            continue
        else:
            n.grupe.append(Grupa())

    n.grupe = n.grupe[:-1] # stergem ultima grupa vida
    nivele.append(n)
    if len(n.grupe) == 1:
        break
    elif len(n.grupe) == 0:
        nivele.pop()
        break
afisare(nivele)
#endregion

monoame_maximale = []
monoame_centrale = []
poz_monoame_centrale = []
linii = getstats(nivele, monoame_maximale)

#region tabel2
table, n = createtable(monoame_maximale)
incercuite = 0
stelutze = 0
for i in range(n):
    stars_per_line = 0
    si, sj = 0, 0
    for j in range(len(monoame_maximale)):
        if table[i][j] == '*':
            stars_per_line += 1
            si, sj = i, j
    if stars_per_line == 1:
        table[si][sj] = 'O'
        incercuite += 1
        if not monoame_maximale[sj] in monoame_centrale:
            monoame_centrale.append(monoame_maximale[sj])
            poz_monoame_centrale.append(sj+1)
    stelutze += stars_per_line
#endregion
_l = len(monoame_centrale)
if _l == 0:
    print(f"Monoame centrale: NU EXISTA")
else:
    print(f"Monoame centrale: {[f'max{i}' for i in poz_monoame_centrale]}")

caz = 0
if _l == 0:
    caz = 3
    print("Caz 3\n")
elif _l == len(monoame_maximale):
    caz = 1
    print("Caz 1\n1 forma simplificata")
    showtable(table, monoame_maximale)
    print("\n")
    showrez(linii, len(monoame_maximale), stelutze, incercuite, len(monoame_centrale), caz, 1)
    exit(0)
else: caz = 2

if caz == 2:
    print("Caz 2\n")
    showtable(table, monoame_maximale)
    for cj in poz_monoame_centrale:
        for i in range(n):
            ch = table[i][cj-1]
            if ch == ' ':
                table[i][cj-1] = "█"
            if ch == '*':
                table[i][cj - 1] = 'x'

    showtable(table, monoame_maximale)

    for i in range(n):
        for j in range(len(monoame_maximale)):
            if marcat(table[i][j]):
                for j1 in range(len(monoame_maximale)):
                    ch = table[i][j1]
                    if ch == ' ':
                        table[i][j1] = "█"
                    if ch == '*':
                        table[i][j1] = 'x'

    showtable(table, monoame_maximale)

rest_monoame = []
for m in monoame_maximale:
    if not m in monoame_centrale:
        rest_monoame.append(m)

def solutie(p):
    if len(p) > len(rest_monoame): return False
    if len(monoame_centrale) + len(p) != len(monoame_maximale):
        return False
    fs = monoame_centrale[:] # forma simplificata
    for i in range(len(p)):
        if p[i] == True:
            fs.append(rest_monoame[i])
    mintermi = getmintermi(monoame_maximale)
    for mt in mintermi:
        for mmax in fs:
            if mt in mmax:
                break
        else:
            return False
    return True

imin = 1000
rez = []

def back(l):
    l.append(False)
    for cand in [False, True]:
        l[-1] = cand
        if len(l)<len(rest_monoame):
            back(l[:])
        else: # egale
            if solutie(l):
                nrmint = l.count(True)
                global imin
                if nrmint < imin:
                    imin = nrmint
                    rez.clear()
                    rez.append(l)
                elif nrmint == imin:
                    rez.append(imin)
    l.pop()

back([])
print(f"Numarul formelor simplificate: {len(rez)}")
print("\n............................................\n"
      "████████████████████████████████████████████\n\n")

showrez(linii, len(monoame_maximale), stelutze, incercuite, len(monoame_centrale), caz, len(rez))


# for g in grupe:
#     print("Grupa")
#     for m in g.monoame:
#         print(m, end="")
#     print()


