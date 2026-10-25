#zadanie 1

#1)Poprawne: średniki nie są potrzebne, ale nie wpłyną na działanie kodu
#Jedyny niezbędny średnik to ten, który rozdziela definicje x i y jeśli obie znajdują się w jednej linijce.

#2) Nie jest poprawne, ponieważ po pętli for : powinno znaleźć się wcięcie i dopiero instrukcja do wykonania.
#Przy instrukcjach prostych można zrezygnować z wcięcia po instrukcji if :
#Poprawione:
#for i in "axby": 
#    if ord(i) < 100: print (i)

#3) Niepoprawne: Po for : należy wykonać wcięcie.
#Instrukcja if jest poprawna, ponieważ jest to wyrażenie trójargumentowe
#for i in "axby": 
#   print (ord(i) if ord(i) < 100 else i)


#zadanie 2

#sort() modyfikuje listę i zwraca none, więc po przypisaniu L.sorted() do L otrzymamy L = none
#powinno być:
L = [3, 5, 4] ; L.sort()
print(L)

#to zadziała, gdy zmiennych po przecinku po lewej stronie znaku = będzie tyle samo co wartości po przecinku po prawej
#wtedy każdej zmiennej zostanie przypisana odpowiednia wartość:
x, y , z= 1, 2, 3
print(x)
print(y)
print(z)

#elementy listy przy definiowaniu muszą znajdować się w nawiasach kwadratowych
X = [1, 2, 3 ]; X[1] = 4
print(X) 

# brak indeksu 3 X[3] nie istnieje w liście X. Indeksy są od 0.
# X = [1, 2, 3] ; X[3] = 4

#append() nie działa na obiekt string
#X = "abc" ; X.append("d")

#Map przekazuje range(8) jako argumenty do wywolania pow. 
#Pow dostarcza po 1 argumencie przy wywolaniu, a pow potrzebuje dwoch od obliczenia potegi, wiec kod nie zadziala bo pow dostanie od range(8) tylko jeden argument
# L = list(map(pow, range(8)))

#zadanie 3

for i in range(30):
    if i%3==0 :
        continue
    else:
        print(i)

j=0
while j< 30 :
    if j%3==0:
        j+=1
    else:
        print(j)
        j+=1