from monom import Monom
class Grupa:
    def __init__(self, nr1=-1):
        self.monoame = []
        self.nr1 = nr1

    def __len__(self):
        return len(self.monoame)

    def add(self, m):
        if self.nr1 == -1 or m.nr1() == self.nr1:
            self.monoame.append(m)
            self.nr1 = m.nr1()
        else: raise ValueError("Nivel de factorizare diferit!")

    def __str__(self):
        rez = f"Grupa {self.nr1}\n"
        def tox(bf):
            if bf: return 'x'
            else: return ' '
        for m in self.monoame:
            rez += f"{tox(m.bifat)} {m.data} {[int(Monom(elem)) for elem in m.mintermi]}\n"
        return rez

class Nivel:
    def __init__(self, niv=0):
        self.grupe = []
        self.nivel_factorizare = niv

    def __str__(self):
        rez = f"    Nivelul {self.nivel_factorizare}\n"
        for g in self.grupe:
            rez += str(g)
        return rez+"\n"

