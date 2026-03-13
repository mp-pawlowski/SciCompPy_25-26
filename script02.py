# 2.1

#Create a long positive integer. Find the number of zeros. Hint: change the number to a string.

l = 20150615486413100505051315431035
str(l).count("0")

#--------------------------------
# 2.2

# Explain the results.

x = 5
x == 5 and 3 + 8   # 11
# Pierwsza część wyrażenia zwraca wartość True, wykonywane jest obliczenie z drugiej części
x == 4 and 3 + 8   # False
# Pierwsza część wyrażenia zwraca wartość False, reszta wyrażenia jest ignorowana
3 + 8 and x == 5   # True
# Zwracana jest odpowiedź na ostatnią część wyrażenia, którą jest wartość True
3 + 8 and x == 4   # False
# Zwracana jest odpowiedź na ostatnią część wyrażenia, którą jest wartość False (x wynosi 5)

isinstance(True, int)    # True
# Wartość True jest przechowywana jako 1, czyli integer
isinstance(True, bool)   # True
# Wartość True jest odczytywana jako zmienna bool

#--------------------------------
# 2.3

#Find the sum 1*1 + 3*3 + 5*5 + ... + 2027*2027 [hint: use sum() and range()].

sum(n * n for n in range(1, 2028,2))

#--------------------------------
# 2.4.A

# Find Unicode code points (int) for all characters of your name.

t = "Michał"
[ord(c) for c in t]

#2.4.B

#Prepare the periodic table (ten elements) as a list
#pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4), ...].
#Use pt to print a table (3 right + 20 left + 6 center + 10 right)
#Hint: use the for loop:
#for (n, name, symbol, weight) in pt:
# use variables (n, name, symbol, weight) to create a proper line

pt = [(1,"Hydrogen","H",1), (2,"Helium","He",4),
      (3,"Lithium","Li",7), (4,"Beryllium","Be",9),
      (5,"Boron","B",11), (6,"Carbon","C",12),
      (7,"Nitrogen","N",14), (8,"Oxygen","O",16),
      (9,"Fluorine","F",19), (10,"Neon","Ne",20)]

print("""+---+--------------------+------+----------+
|No.|Name (en)           |Symbol|Weight (u)|
+---+--------------------+------+----------+""")
for (n, name, symbol, weight) in pt:
    print("|" + str(n).rjust(3) + "|" + name.ljust(20) + "|" +
          symbol.center(6) + "|" + str(weight).rjust(10) + "|")
print("+---+--------------------+------+----------+")

#--------------------------------
# 2.5

#Let S be a long string (many lines).

S = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit. Aenean 
vehicula sapien vel nulla ultricies, 
ac mollis mi consequat."""

#Find the number of black characters in S [not whitespace, see the method S.isspace()].

l = S.split()
len("".join(l))

#Find the number of words in S (a word is a sequence of black characters).

len(l)

#Find the longest word in S.

max(l, key = len)

#Sort words from S according to (1) the lexicographic order, (2) the length.

#1
l.sort(key = str.lower)
#2
l.sort(key = len)

#--------------------------------
# 2.6

# Find and explain the results.

t = (2, 4)
print(t[2])
# Błąd - krotka t zawiera tylko dwie wartości o indeksach 0 i 1
t.append(6)
# Błąd - krotka nie podlega modyfikacji
a, b = t ; print(a, b)
# Zwracane są obie wartości krotki t. Przypisanie do krotki takiej samej liczby zmiennych,
# ile wynosi jej długość, skutkuje przypisaniem do każdej zmiennej jednej wartości z krotki.

#--------------------------------
# 2.7

#Create a dict for conversion of roman numerals/strings (I, IV, V, IX, X, XL, L, XC, C, CD, D, CM, M)
#to arabic numbers. Use different methods.

r = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
a = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
D1 = dict(zip(r, a))

D2 = dict([("I", 1), ("IV", 4), ("V", 5), ("IX", 9), ("X", 10), ("XL", 40), ("L", 50),
           ("XC", 90), ("C", 100), ("CD", 400), ("D", 500), ("CM", 900), ("M", 1000)])

D3 = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50,
      "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}