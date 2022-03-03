
# 1) k va n butun sonlari berilgan(n>0). k sonini n marta chiqaruvchi programma tuzilsin.

k = int(input("k = "))
n = int(input("(n>0) n = "))

for i in range(0,n):
    print(k, end=" ")
    


# 2) a va b butun sonlari berilgan (a<b). a va b sonlari orasidagi barcha butun sonlarni (a va b ni ham)chiqaruvchi va chiqarilgan sonlar sonini 
#    chiqaruvchi programma tuzilsin.(a va b ham chiqarilsin)

print("a va b ni kiriting (a<b)")
a = int(input("a = "))
b = int(input("b = "))
s=0
for i in range(a,b+1):
    s += 1
    print(i, end=" ")
print('\n',s," ta    a = ",a,"   b = ",b,sep="")



# 3) a va b butun sonlari berilgan (a<b). a va b sonlari orasidagi barcha butun sonlarni (a va b dan tashqari) kamayish tartibida chiqaruvchi va 
#    chiqarilgan sonlar sonini chiqaruvchi programma tuzilsin. 

print("a va b ni kiriting (a<b)")
a = int(input("a = "))
b = int(input("b = "))
s=0
for i in range(b-1,a,-1):
    s += 1
    print(i, end=" ")
print('\n',s," ta",sep="")



# 4) Bir kg konfetning narxi berilgan (haqiqiy son). 1, 2,...,10 kg konfetni narxini chiqaruvchi programma tuzilsin.

narx = float(input("narx = "))
for i in range(1,11):
    print(i,"kg   ",i*narx,"so'm")



# 5) Bir kg konfetning narxi berilgan (haqiqiy son). 0.1, 0.2,...,0.9,1 kg konfetni narxini chiqaruvchi programma tuzilsin.

narx = float(input("narx = "))
for i in range(1,11):
    print(i/10,"kg   ",i/10*narx,"so'm")



# 6) Bir kg konfetning narxi berilgan (haqiqiy son). 1.2, 1.4,...,2 kg konfetni narxini chiqaruvchi programma tuzilsin.

narx = float(input("narx = "))
for i in range(12,21,2):
    print(i/10,"kg   ",i/10*narx,"so'm")



# 7) a va b butun sonlar berilgan (a<b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaring.

print("a va b ni kiriting (a<b)")
a = int(input("a = "))
b = int(input("b = "))
s=0
for i in range(a,b+1):
    s += i
print(s)



# 8) a va b butun sonlar berilgan (a<b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaring.

print("a va b ni kiriting (a<b)")
a = int(input("a = "))
b = int(input("b = "))
s=1
for i in range(a,b+1):
    s *= i
print(s)



# 9) a va b butun sonlar berilgan (a<b). a dan b gacha bo'lgan barcha butun sonlar kvadratlarining yig'indisini chiqaring.

print("a va b ni kiriting (a<b)")
a = int(input("a = "))
b = int(input("b = "))
s=0
for i in range(a,b+1):
    s += (i**2)
print(s)



# 10) n butun soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin. s = 1 + 1/2 + 1/3 +...+ 1/n

n = int(input("n = "))
s=0
for i in range(1,n+1):
    s += 1/i
print(s)



# 11) n butun soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin.       s = n**2 + (n+1)**2 + (n+2)**2 +...+ (n*2)**2

n = int(input("n = "))
s=0
for i in range(n,n*2+1):
    s += i**2
print(s)



# 12) n butun soni berilgan (n>0). Quydagi ko'paytmani hisoblovchi programma tuzilsin.      s = 1.1 * 1.2 * 1.3 *...     (n ta ko'paytuvchi)

n = int(input("(n>0) n = "))
s=1
for i in range(1,n+1):
    s *= (i/10+1)
print(s)



# 13) n butun soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin.      s = 1.1 - 1.2 + 1.3 -...  

n = int(input("(n>0) n = "))
s=0
for i in range(1,n+1):
    if i % 2 == 1:
        s += (i/10+1)
    else:
        s -= (i/10+1)
print(s)



# 14) n butun soni berilgan (n>0). Shu sonning kvadratini quydagi formula asosida hisoblovchi programma tuzilsin.     n**2 = 1 + 3 + 5 +...+ (2*n - 1)

n = int(input("n = "))
a = 2*n-1
s = 0
for i in range(1,a,2):
    s += i
    print(i,end=" + ")
print(2*n-1,"=",n**2)



# 15) n butun soni va a haqiqiy soni berilgan (n>0). a ning n-darajasini aniqlovchi programma tuzilsin.      a**n = a*a*a...a

n = int(input("n = "))
a = float(input("a = "))
s=1
for i in range(1,n+1):
    s *= a
print(s)



# 16) n butun soni va a haqiqiy soni berilgan (n>0). Bir sikldan foydalanib a ning 1 dan n gacha bo'lgan barcha darajalarini chiqaruvchi programma tuzilsin.

n = int(input("n = "))
a = float(input("a = "))
for i in range(1,n+1):
    print(a**i,end=", ")



# 17) n butun soni va a haqiqiy soni berilgan (n>0). Bir sikldan foydalanib quydagi a ning 1 dan n gacha bo'lgan barcha darajalarini chiqaruvchi 
#     va yig'indini hisoblovchi programma tuzilsin.

n = int(input("n = "))
a = float(input("a = "))
s = 0
for i in range(1,n+1):
    s += a**i
    print(a**i,end=", ")
print("  s =",s)



# 18) n butun soni va a haqiqiy soni berilgan (n>0). Bir sikldan foydalanib quydagi a ning 1 dan n gacha bo'lgan barcha darajalarini chiqaruvchi va yig'indini
#     hisoblovchi programma tuzilsin.   1 - a + a**2 - a**3 +....((-1)**n)*(a**n)  shart operatoridan foydalanilmasin

n = int(input("n = "))
a = float(input("a = "))
s = 0
for i in range(1,n+1):
    s = s + ((-a)**i)
    print(a**i,end=", ")
print("  s =",s+1)



# 19) n butun soni va a haqiqiy soni berilgan (n>0). 1 dan n gacha bo'lgan sonlar ko'paytmasini chiqaruvchi programma tuzilsin ya'ni faktaryal hisoblansin. 
#     n! = 1 * 2 * 3 *... * n

n = int(input("n = "))
a = float(input("a = "))
s = 1
for i in range(1,n+1):
    s *= i
print(s)



# 20) n butun soni berilgan (n>0). Bir sikldan foydalangan holda quydagi yig'indini hisoblovchi programma tuzilsin.      1! + 2! + 3! +...+ n!

n = int(input("n = "))
summa = 0
faktaryal = 1
for i in range(1,n+1):
    faktaryal *= i
    summa += faktaryal
print(summa)
        
        

# 21) n butun soni berilgan (n>0). Bir sikldan foydalangan holda quydagi yig'indini hisoblovchi programma tuzilsin. (olingan natija tahminan e = exp(1) ga yaqinlashadi)
#     1 + 1/(1!) + 1/(2!) + 1/(3!) +...+ 1/(n!)

n = int(input("n = "))
summa = 0
faktaryal = 1
for i in range(1,n+1):
    faktaryal *= i
    summa += 1/faktaryal
print(summa+1)



# 22) n butun soni va x haqiqiy soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin. (olingan natija tahminan e**x ga yaqinlashadi)
#     1 + x + (x**2)/(2!) + (x**3)/(3!) +...+(x**n)/(n!)

n = int(input("n = "))
x = float(input("x = "))
faktaryal = 1
daraja = 1
summa = 0
for i in range(1,n+1):
    faktaryal *= 1
    daraja *= x
    summa += daraja / faktaryal 
print(summa+1)



# 23) n butun soni va x haqiqiy soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin. (olingan natija tahminan sin(x) ga yaqinlashadi)
#     x - (x**3)/(3!) + (x**5)/(5!) -...+ (-(-1)**n)*(x**(2*n-1))/((2*n-1)!)

n = int(input("n = "))
x = float(input("x = "))

n = int(input("n = "))
x = float(input("x = "))
faktaryal = 1
summa = x
for i in range(2,n+1):
    faktaryal *= (2*i-2)*(2*i-1)
    summa += (-(-1)**i) * (x**(2*i - 1))/faktaryal
print(summa)



# 24) n butun soni va x haqiqiy soni berilgan (n>0). Quydagi yig'indini hisoblovchi programma tuzilsin. (olingan natija tahminan cos(x) ga yaqinlashadi)
#     1 - (x**2)/(2!) + (x**4)/(4!) -...+ (-(-1)**n)*(x**(2*n-2))/((2*n-2)!)

n = int(input("n = "))
x = float(input("x = "))

n = int(input("n = "))
x = float(input("x = "))
faktaryal = 1
summa = 1
for i in range(2,n+1):
    faktaryal *= (2*i-2)*(2*i-3)
    summa += (-(-1)**i) * (x**(2*i-2))/faktaryal
print(summa)   



# 25) n butun soni va x haqiqiy soni berilgan (n>0, |x|<1). Quydagi yig'indini hisoblovchi programma tuzilsin.    x - (x**2)/2 + (x**3)/3 -...+((-1)**(n-1)) * (x**n)/n

n = int(input("n = "))
x = float(input("x = "))

summa = 0
for i in range(1,n+1):
    summa += ((-1)**(i-1)) * (x**i)/i
print(summa)



# 26) n butun soni va x haqiqiy soni berilgan (n>0, |x|<1). Quydagi yig'indini hisoblovchi programma tuzilsin.  x - (x**3)/3 + (x**5)/5 -...+(-(-1)**n) * (x**(2*n-1))/(2*n-1)

n = int(input("n = "))
x = float(input("x = "))

summa = 0
for i in range(1,n+1):
    summa += (-(-1)**i) * (x**(2*i-1))/(2*i-1)
print(summa)



# 27) n butun soni va x haqiqiy soni berilgan (n>0, |x|<1). Quydagi yig'indini hisoblovchi programma tuzilsin. 
#     x + 1*(x**3)/(2*3) + 1*3*(x**5)/(2*4*5) +...+1*3*...*(2*n-1)*(x**(2*n+1))/(2*4*...*(2*n)*(2*n+1))

n = int(input("n = "))
x = int(input("x = "))

s = x
p = 1

for i in range(1,n+1):
    p *= (2*i-1)/(2*i)
    s += p*(x**(2*i+1)/(2*i+1)

print(s)



# 28) n butun soni va x haqiqiy soni berilgan (n>0, |x|<1). Quydagi yig'indini hisoblovchi programma tuzilsin. 
#     1 + x/2 - 1*(x**2)/(2*4) + 1*3(x**3)/(2*4*6) -...+(-1)**(n-1)*1*3...*(2*n-3)*(x**n)/(2*4*...*(2*n))

n = int(input("n = "))
x = int(input("x = "))

p = 1
s = 1+x/2

for i in range(1,n+1):
    p *= (2*i-1)/(2*i)
    i = i + 1
    s += ((-1)**i)*p*(x**(i)/(2*i)

print(s)




# 29) n butun soni va sonlar o'qida 2 ta A, B nuqta berilgan. (A, B haqiqiy son). [A,B] kesmani teng n ta kesmaga bo'ling. 
#      [A,B] kesmada ajratilgan barcha nuqtalarni chiqaring.

n = int(input("n = "))
A = float(input("A = "))
B = float(input("B = "))

a = (B - A) / n

for i in range(1,n):
    A += a
    print(round(A,2),end=",  ")



from math import *

# 30) n butun soni va sonlar o'qida 2 ta A, B nuqta berilgan. (A, B haqiqiy son). [A,B] kesmani teng n ta kesmaga bo'ling. [A,B] kesmada ajratilgan 
#     barcha nuqtalar uchun F(x) = 1 - sin(x) funksiya qiymatini hisoblang.

n = int(input("n = "))
A = float(input("A = "))
B = float(input("B = "))

a = (B - A) / n

for i in range(1,n):
    A += a
    print(1-sin(A),end=",  ")



# 31 n butun soni berilgan (n>0). Quydagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.   A0 = 2;   An = 2 + 1/A(n-1); n = 1,2,...n   n-indeks

n = int(input("n = "))
B = 2
for i in range(1,n+1):
    A = B
    B = 2+1/A
    print("A",i-1,"=",A,end=",   ")



# 32) n butun soni berilgan (n>0). Quydagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.   A0 = 1;   An = (A(n-1) + 1)/n;   n = 1,2,...n   n-indeks

n = int(input("n = "))
B = 1
for i in range(1,n+1):
    A = B
    B = (A + 1) / i
    print("A",i-1,"=",A,end=",   ")



# 33) n butun soni berilgan (n>1). Fibonachchi ketma-ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
#    F1 = 1;  F2 = 1;    Fn = F(n-2) + F(n-1);  n = 3,4,...n   n-indeks

# 1-usul
F1 = 1
F2 = 1

n = int(input("n = "))

print(F1,F2,end=" ")

for i in range(3,n+1):
    F1,F2 = F2,F1+F2
    print(F2, end=" ")


# 1-usul
F1 = 1
F2 = 1

n = int(input("n = "))

print(F1,F2,end=" ")

for i in range(3,n+1):
    F3 = F1 + F2
    F1 = F2
    F2 = F3
    
    print(F3, end=" ")
    


# 34) n butun soni berilgan (n>1). Quydagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
#     A1 = 1;  A2 = 2;    An = (A(n-2) + 2*A(n-1)) / 3;   n = 3,4,...n   n-indeks

A1 = 1
A2 = 2

n = int(input("n = "))

print(A1,A2,end=" ")

for i in range(3,n+1):
    A3 = (A1 + 2*A2) / 3
    print(A3,end=", ")
    A1 = A2
    A2 = A3
    


# 35) n butun soni berilgan (n>2). Quydagi ketma-ketlikning dastlabki n ta hadini chiqaruvchi programma tuzilsin.
#     A1 = 1;  A2 = 2;  A3 = 3;   An = A(n-1) + A(n-2) - 2*A(n-3);   n = 4,5,...n

A1 = 1
A2 = 2 
A3 = 3

n = int(input("n = "))

print(A1,A2,A3,end=" ")

for i in range(4,n+1):
    A4 = A3 + A2 - 2*A1
    print(A4,end=", ")
    A1 = A2
    A2 = A3
    A3 = A4


# ICHMA-ICH OCHILGAN SIKLLAR


# 36) n va k butun sonlar berilgan. Quydagi yig'indini chiqaruvchi programma tuzilsin.     1**k + 2**k + ... + n**k

n = int(input("n = "))
k = int(input("k = "))
s = 0
for i in range(1,n+1):
    s += i**k
print(s)



# 37) n butun soni berilgan. Quydagi yig'indini chiqaruvchi programma tuzilsin.     1**1 + 2**2 + ... + n**n

n = int(input("n = "))
s = 0
for i in range(1,n+1):
    s += i**i
print(s)



# 38) n butun soni berilgan. Quydagi yig'indini chiqaruvchi programma tuzilsin.     1**(n) + 2**(n-1) + ... + n**1

n = int(input("n = "))
s = 0
for i in range(1,n+1):
    s += (i**(n+1-i))
print(s)



# 39) A va B butun sonlar berilgan (A<B). A va B sonlar orasidagi barcha butun sonlarni chiqaruvchi programma tuzilsin. Bunda har bir son
#     o'zining qiymaticha chiqarilsin. Ya'ni 3 soni 3 marta chiqarilsin.

A = int(input("A = "))
B = int(input("B = "))

for i in range(A+1,B):
    for j in range(1,i+1):
        print(i,end=" ")
    print('\n')



# 40) A va B butun sonlar berilgan (A<B). A va B sonlar orasidagi barcha butun sonlarni chiqaruvchi programma tuzilsin. 
#     Bunda A soni 1 marta, (A+1) soni 2 marta chiqariladi va xakazo.

A = int(input("A = "))
B = int(input("B = "))

for i in range(A,B+1):
    for j in range(A-1,i):
        print(i,end=" ")
    print('\n')

