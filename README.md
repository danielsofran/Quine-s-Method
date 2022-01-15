# Metoda lui Quine

## Instalare

Acest proiect necesită instalarea pachetului **prettytable**
În Visual Studio:
```bash
pip install prettytable
```
În interpretorul nativ:
```bash
python -m pip install -U prettytable
```

## Legendă

În primul tabel:
- x: **bifă**
- numărul nivelului: **numărul de -** din grupurile pe care le conține
- numărul grupei: **numărul de 1** al monoamelor conținute
- lista de numere: **indicii mintermilor** din care monomul respectiv a fost obținut

În cel de-al doilea tabel:
- O: * încercuită
- █: spațiu hașurat
- x: * hașurată

## Rulare

Se va rula script-ul **main.py**.


## Exemplu

```
Introduceti numarul de variabile x: 3
Introduceti mintermii in baza 10 sau 2: 5 2 1 6 0
    Nivelul 0
Grupa 2
x 101 [5]
x 110 [6]
Grupa 1
x 010 [2]
x 001 [1]
Grupa 0
x 000 [0]


    Nivelul 1
Grupa 1
  -01 [5, 1]
  -10 [6, 2]
Grupa 0
  0-0 [2, 0]
  00- [1, 0]


max1: -01 = (not x2) (x3) = m5 v m1
max2: -10 = (x2) (not x3) = m6 v m2
max3: 0-0 = (not x1) (not x3) = m2 v m0
max4: 00- = (not x1) (not x2) = m1 v m0

Numarul de linii din primul tabel: 9
Numarul de bife: 5
Numarul de linii nebifate/momame maximale: 4

+----+------+------+------+------+
|    | max1 | max2 | max3 | max4 |
+----+------+------+------+------+
| 0  |      |      |  *   |  *   |
| 1  |  *   |      |      |  *   |
| 2  |      |  *   |  *   |      |
| 5  |  *   |      |      |      |
| 6  |      |  *   |      |      |
+----+------+------+------+------+
Monoame centrale: ['max1', 'max2']
Caz 2

+----+------+------+------+------+
|    | max1 | max2 | max3 | max4 |
+----+------+------+------+------+
| 0  |      |      |  *   |  *   |
| 1  |  *   |      |      |  *   |
| 2  |      |  *   |  *   |      |
| 5  |  O   |      |      |      |
| 6  |      |  O   |      |      |
+----+------+------+------+------+
+----+------+------+------+------+
|    | max1 | max2 | max3 | max4 |
+----+------+------+------+------+
| 0  |  █   |  █   |  *   |  *   |
| 1  |  x   |  █   |      |  *   |
| 2  |  █   |  x   |  *   |      |
| 5  |  O   |  █   |      |      |
| 6  |  █   |  O   |      |      |
+----+------+------+------+------+
+----+------+------+------+------+
|    | max1 | max2 | max3 | max4 |
+----+------+------+------+------+
| 0  |  █   |  █   |  *   |  *   |
| 1  |  x   |  █   |  █   |  x   |
| 2  |  █   |  x   |  x   |  █   |
| 5  |  O   |  █   |  █   |  █   |
| 6  |  █   |  O   |  █   |  █   |
+----+------+------+------+------+
Numarul formelor simplificate: 2

............................................
████████████████████████████████████████████


Numărul total al liniilor (distincte) din primul tabel Quine-Mc’Clusky este: 9
Numărul monoamelor maximale este: 4
Numărul total de ”*” din cel de al doilea tabel Quine-Mc’Clusky este: 8
Numărul de ”*” încercuite este: 2
Numărul monoamelor centrale este: 2
Cazul algoritmului de simplificare este: 2
Nr. de forme simplificate ale funcției este: 2
