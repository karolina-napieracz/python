#zadanie 1
#1)Poprawne: średniki nie są potrzebne, ale nie wpłyną na działanie kodu

#2) Nie jest poprawne, ponieważ po pętli for : powinno znaleźć się wcięcie i dopiero instrukcja do wykonania.
#Przy instrukcjach prostych można zrezygnować z wcięcia po instrukcji if :
#Poprawione:
#for i in "axby": 
#    if ord(i) < 100: print (i)

#3) Niepoprawne: Po for : należy wykonać wcięcie.
#Instrukcja if jest poprawna, ponieważ jest to wyrażenie trójargumentowe
#for i in "axby": 
#   print (ord(i) if ord(i) < 100 else i)


x = 2 y = 3
if (x > y):
    result = x
else:
    result = y

print(result)