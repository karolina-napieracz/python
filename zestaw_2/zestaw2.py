#zadanie 2.10

def liczba_wyrazow(line):
    line=line.split()  
    print(len(line))


line = "liczba wyrazow \ntego zdania to\n jest" 
liczba_wyrazow(line)

#zadanie 2.11
word = 'word'
print(("_").join(word))

#zadanie 2.12
pierwsze=''
for a in line.split():
    pierwsze+=a[0]

print(pierwsze)

ostatnie=''
for a in line.split():
    ostatnie+=a[len(a)-1]

print(ostatnie)

#zadanie 2.13

suma = 0
for a in line.split():
    suma += len(a)

print(suma)