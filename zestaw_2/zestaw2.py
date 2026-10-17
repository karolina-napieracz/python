#zadanie 2.10
def liczba_wyrazow(line):
    line=line.split()  
    print(len(line))

line = "liczba wyrazow \ntego zdania to\n jest" 
print('2.10 liczba wyrazów w line to:')
liczba_wyrazow(line)

#zadanie 2.11
word = 'word'
print('2.11',("_").join(word))

#zadanie 2.12
pierwsze=''
for a in line.split():
    pierwsze+=a[0]

print('2.12 string stworzony z pierwszych znaków wyrazów ze stringu line:',pierwsze)

ostatnie=''
for a in line.split():
    ostatnie+=a[len(a)-1]

print('2.12 string stworzony z ostatnich znaków wyrazów ze stringu line: ',ostatnie)

#zadanie 2.13
suma = 0
for a in line.split():
    suma += len(a)

print('2.13 łączna długość wyrazów w stringu line:',suma)

#zadanie 2.14
zdanie="jaki jest najdluzszy wyraz w tym zdaniu"
wyraz=max(zdanie.split(),key=len)
print('2.14 najdłuższy wyraz w zdaniu: ',zdanie,'to: "',wyraz, '", a jego dlugosc to: ', len(wyraz))

#zadanie 2.15
L=[1,2,5,10,65,15003]
ciag=''
for x in L:
    ciag += str(x)

print('2.15 string będący ciągiem cyfr kolejnych liczb z listy L: ',ciag)

#zadanie 2.18
line='GvR is a Dutch programmer. GvR is the creator of the Python programming language. GvR was born and raised in the Netherlands'
line=line.replace('GvR','Guido van Rossum') 

print('2.18 string line po zastąpieniu GvR ',line)

#zadanie 2.17
alfabetycznie=sorted(line.split())
print('2.17 Słowa posortowane alfabetycznie:',alfabetycznie)

dlugosciowo=sorted(line.split(),key=len)
print('2.17 Słowa posortowane zgodnie z długością:',dlugosciowo)

#zadanie 2.18
a = 135432857460328754356483560723460831274630286432
print('2.18 liczba wystąpień cyfry 0 w liczbie całkowitej',a ,'to: ', str(a).count('0'))

#zadanie 2.19
L=[1,243,33,79,45,653,2,646]
wynik=''
for a in L:
    a=str(a)
    while len(a)<3:
        a+='0'
    wynik+=a

print('2.19 string utworzony z listy: ',L,'wypełniony zerami to: ', wynik)