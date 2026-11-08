import math
from math import gcd   # Py3

def add_frac(frac1, frac2):
    if(mianownik_zero(frac1) or mianownik_zero(frac2)):
        return 'Mianownik nie moze byc zerem'
    else:
        if frac1[1]==frac2[1]:
            return [frac1[0]+frac2[0],frac1[1]]
        else:
            frac1,frac2=do_wspolnego(frac1,frac2)
            return[frac1[0]+frac2[0],frac1[1]]

def sub_frac(frac1, frac2):
    if(mianownik_zero(frac1) or mianownik_zero(frac2)):
            return 'Mianownik nie moze byc zerem'
    else:
        if frac1[1]==frac2[1]:
            return [frac1[0]-frac2[0],frac1[1]]
        else:
            frac1,frac2=do_wspolnego(frac1,frac2)
            return[frac1[0]-frac2[0],frac1[1]]
        
def mul_frac(frac1, frac2):
    d=math.gcd(frac1[0],frac2[1])
    e=math.gcd(frac1[1],frac2[0])
    if d:
        frac1[0]=frac1[0]/d
        frac2[1]=frac2[1]/d
    if e:
        frac1[1]=frac1[1]/e
        frac2[0]=frac2[0]/e
    return [frac1[0]*frac2[0],frac1[1]*frac2[1]]

def div_frac(frac1, frac2):
    if(mianownik_zero(frac1) or mianownik_zero(frac2)):
        return 'Mianownik nie moze byc zerem'
    else:
        if is_zero(frac2):
            return 'Nie mozna dzielic przez zero'
        else:
            frac2 = [frac2[1], frac2[0]]
            return mul_frac(frac1, frac2)

def is_positive(frac):
    if(mianownik_zero(frac)):
        return False
    else:
        if frac[0]*frac[1] > 0:
            return True
        else:
            return False

    
def is_zero(frac):  
    if(mianownik_zero(frac)):
        return False
    else:
        if frac[0] == 0:
            return True
        else:
            return False
    
def cmp_frac(frac1, frac2):       # -1 | 0 | +1
    if(mianownik_zero(frac1) or mianownik_zero(frac2)):
        return 'Mianownik nie moze byc zerem'
    else:
        a = frac1[0]*frac2[1]
        b = frac2[0]*frac1[1]

        if frac1[1]*frac2[1] < 0:
            a = -a
            b = -b
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
        
def frac2float(frac):              # konwersja do float
    if(mianownik_zero(frac)):
        return 'Mianownik nie moze byc zerem'
    else:
        return frac[0]/frac[1]
def mianownik_zero(frac):
    if frac[1]==0:
        return True
    else:
        return False
    
def do_wspolnego(frac1, frac2):
    d=(frac1[1] * frac2[1])//math.gcd(frac1[1], frac2[1])
    return [[frac1[0]* (d//frac1[1]),d],[frac2[0] *(d// frac2[1]),d]]

f1 = [-1, 2]      # -1/2
f2 = [1, -2]      # -1/2 (niejednoznaczność)
f3 = [0, 1]       # zero
f4 = [0, 2]       # zero (niejednoznaczność)
f5 = [3, 1]       # 3
f6 = [6, 2]       # 3 (niejednoznaczność)

print(mianownik_zero([-1,2]))
print(mul_frac(f1, f2))