class Monom:
    ordin = 0
    def __init__(self, nr="", grup=1, bifat=False):
        self.mintermi = []
        self.data = ""
        self.grup = grup
        self.bifat = bifat
        if isinstance(nr, str):
            self.data = nr
            if len(self.data) < Monom.ordin:
                self.data = "0"*(Monom.ordin-len(self.data)) + self.data
        elif isinstance(nr, int):
            self.data = bin(nr)[2:]
            if len(self.data) < Monom.ordin:
                self.data = "0"*(Monom.ordin-len(self.data)) + self.data
        else: # e p lista sau un pointer
            for c in nr:
                if c == 1 or c == '1':
                    self.data += "1"
                else: self.data += "0"
        self.mintermi.append(self.data)

    def xuri(self):
        rez = ""
        for i in range(len(self.data)):
            if self.data[i] == '1':
                rez += f"(x{i+1}) "
            elif self.data[i] == '0':
                rez += f"(not x{i+1}) "
        return rez

    def __len__(self):
        return len(self.data)

    def nr1(self):
        nr = 0
        for c in self.data:
            if c == '1':
                nr += 1
        return nr

    def nivel_factorizare(self):
        rez = 0
        for c in self.data:
            if c == '-':
                rez += 1
        return rez

    def __int__(self):
        rez = 0
        p2 = 1
        for c in reversed(self.data):
            if c == '1':
                rez += p2
            p2 *= 2
        return rez

    def __str__(self):
        return self.data

    def __contains__(self, item: int):
        return item in [int(Monom(mt)) for mt in self.mintermi]

    def __getitem__(self, item):
        return int(self.data[item-1])

    def __setitem__(self, key, value):
        rez = ""
        for i in range(len(self.data)):
            if i != key-1:
                rez += self.data[i]
            else:
                rez += str(value)
        self.data = rez

    def __add__(self, other):
        m = Monom()
        m.mintermi = self.mintermi + other.mintermi
        diferente = 0
        rez = ""
        for c1, c2 in zip(self.data, other.data):
            if c1 != c2:
                if c1 == '-' or c2 == '-':
                    raise ValueError("- mismatch!")
                rez += "-"
                diferente += 1
                if diferente > 1:
                    raise ValueError("Nu factorizeaza!")
            else:
                rez += c1
        if diferente == 0:
            raise ValueError("Egale!")
        m.data = rez
        self.bifat = True
        other.bifat = True
        return m

    def __eq__(self, other):
        return self.data == other.data





