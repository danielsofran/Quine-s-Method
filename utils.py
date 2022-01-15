from prettytable import PrettyTable

from monom import Monom

def afisare(l):
    for elem in l:
        print(elem)

def citire():
    Monom.ordin = int(input("Introduceti numarul de variabile x: "))
    inputstr = input("Introduceti monoamele in baza 10 sau 2: ")

    #inputstr = "15 13 14 10 2 4"
    #inputstr = "1 3 4 5 6 7 8 9 10 11 12 14"
    _ = inputstr.split()
    rez = []
    for __ in _:
        rez.append(Monom(int(__)))
    return rez

def getstats(nivele, maximale):
    bife = 0
    linii = 0
    index = 1
    for nivel in nivele:
        for grupa in nivel.grupe:
            linii += len(grupa)
            for m in grupa.monoame:
                if m.bifat:
                    bife+=1
                else:
                    maximale.append(m)
                    mintermi = [int(Monom(mint)) for mint in m.mintermi]
                    smin = ""
                    for mt in mintermi:
                        smin += f"m{mt} v "
                    smin = smin[:-3]
                    print(f"max{index}: {m} = {m.xuri()}= {smin}")
                    index += 1
    print(f"\nNumarul de linii din primul tabel: {linii}\nNumarul de bife: {bife}\nNumarul de linii nebifate/momame maximale: {linii-bife}\n")
    return linii-bife

def getmintermi(maximale):
    mintermi = []
    for monom in maximale:
        for m in monom.mintermi:
            val = int(Monom(m))
            if not val in mintermi:
                mintermi.append(val)
    return sorted(mintermi)

def createtable(maximale):
    index = 1
    t = PrettyTable()
    t.padding_width = 1
    t.field_names = ["  "] + [f"max{i}" for i in range(1, len(maximale)+1)]
    mintermi = getmintermi(maximale)
    table = []
    for m in mintermi:
        f = lambda x: '*' if x else " "
        col = [f(m in maxt) for maxt in maximale]
        t.add_row([str(m)] + col)
        table.append(col)
    print(t)
    return table, len(mintermi)

def showtable(table, maximale):
    t = PrettyTable()
    t.padding_width = 1
    t.field_names = ["  "] + [f"max{i}" for i in range(1, len(maximale) + 1)]
    mintermi = getmintermi(maximale)
    for i in range(len(mintermi)):
        t.add_row([str(mintermi[i])] + table[i])
    print(t)

def marcat(ch):
    if ch == 'x' or ch == 'O': return True
    return False
