"""
Created on Sun Feb  6 14:49:59 2022



# 1) Butun son berilgan. Agar berilgan son musbat bo'lsa, 1 ga oshirilsin, aks
#    holda o'zgartirilmasin. Hosil bo'lgan sonni ekranga chiqaring.

son = int(input("Butun son kiriting - "))
if son > 0:
    print(son,'+ 1 =',son+1)
else:
    print(son)
    
    

# 2) Butun son berilgan. Agar berilgan son musbat bo'lsa, 1 ga oshirilsin, aks
#    holda 2 ga kamaytirilsin. Hosil bo'lgan sonni ekranga chiqaring.

son = int(input("Butun son kiriting - "))
if son > 0:
    print(son,'+ 1 =',son+1)
else:
    print(son,'- 2 =',son-2)
  


# 3) Butun son berilgan. Agar berilgan son musbat bo'lsa, 1 ga oshiring, agar
#    manfiy bo'lsa 2 ga kamaytiring. Agar nolga teng bo'lsa, 10 ni o'zlashtirsin.
#    Hosil bo'lgan sonni ekranga chiqaruvchi programma tuzilsin.

son = int(input("Butun son kiriting - "))
if son > 0:
    print(son,'+ 1 =',son+1)
elif son == 0:
    print(10)
else:
    print(son,'- 2 =',son-2)



# 4) Uchta butun son berilgan. Shu sonlar orasidan nechta musbat son borligini
#    aniqlovchi programma tuzilsin.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = 0
if a > 0:
    s += 1
if b > 0:
    s += 1
if c > 0:
    s += 1
print(s,"ta")



# 5) Uchta butun son berilgan. Shu sonlar orasidan nechta musbat va manfiy son 
#    borligini aniqlovchi programma tuzilsin.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
s = 0
n = 0
if a > 0:
    s += 1
elif a < 0:
    n += 1

if b > 0:
    s += 1
elif b < 0:
    n += 1

if c > 0:
    s += 1
elif c < 0:
    n += 1
print(s,"ta musbat")
print(n,"ta manfiy")



# 6) Ikkita butun son berilgan. Shu sonlarning kattasini aniqlang.

a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(a)
elif a == b:
    print('ikkita son teng')
else:
    print(b)



# 7) Ikkita butun son berilgan. Shu sonlarning kichchigini tartib raqamini aniqlang.

a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(b)
else:
    print(a)



# 8) Ikkita butun son berilgan. Shu sonlarning avval kattasini keyin
#    kichchigini ekranga chiqaruvchi programma tuzing.

a = int(input("a = "))
b = int(input("b = "))
if a > b:
    print(a)
    print(b)
elif a == b:
    print('ikkita son teng')
else:
    print(b)
    print(a)



# 9) A va B haqiqiy sonlar berilgan. Shu sonlarni shunday o'zgartirish kerakki
#    A son kichchik B son katta bo'lsin. A va B ning qiymatini ekranga chiqaring.

A = float(input("A = "))
B = float(input("B = "))

C = A + B
if A > B:
    print("A =",C-A)
    print("B =",C-B)
elif A == B:
    print("A =",A)
    print("B =",B)
else:
    print("A =",C-B)
    print("B =",C-A)
    


# 10) A va B butun sonlari berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa
#     A va B o'zgaruvchilari ularning yig'indisini o'zlashtirsin. Agar teng
#     bo'lsa, 0 ni o'zlashtirsin. A va B ning qiymati ekranga chiqarilsin.

A = int(input("A = "))
B = int(input("B = "))

if A == B:
    A = 0
    B = 0
    print("A =",A)
    print("B =",B)
elif A != B:
    C = A + B
    print("A =",C)
    print("B =",C)



# 11) A va B butun sonlar berilgan. Agar o'zgaruvchilar o'zaro teng bo'lmasa,
#     A va B bu sonlarning kattasini o'zlashtirsin. Agar teng bo'lsa, 0 ni
#     o'zlashtirsin. A va B ning qiymatini ekranga chiqaring.

A = int(input("A = "))
B = int(input("B = "))

if A == B:
    A = 0
    B = 0
    print("A =",A)
    print("B =",B)
elif A > B:
    A = A
    B = A
    print("A =",A)
    print("B =",B)
elif A < B:
    A = B
    B = B
    print("A =",A)
    print("B =",B)




# 12) Uchta son berilgan. Shu sonlarni kichigini aniqlovchi programma tuzilsin.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A <= B and A <= C:
    print(A)
elif B <= A and B <= C:
    print(B)
else:
    print(C)



# 13) Uchta son berilgan. Shu sonlarning o'rtachasi aniqlang.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if B <= A <= C  or  C <= A <= B:
    print(A)
elif A <= B <= C  or  C <= B <= A:
    print(B)
else:
    print(C)



# 14) Uchta son berilgan. Shu sonlarning avval kichigini keyin kattasini aniqlang.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A <= B  and  A <= C:
    print(A)
    if B >= C:
        print(B)
    else:
        print(C)
elif B <= A  and  B <= C:
    print(B)
    if A >= C:
        print(A)
    else:
        print(C)
else:
    print(C)
    if A >= B:
        print(A)
    else:
        print(B)



# 15) Uchta son berilgan. Shu sonlarning yig'indisi eng katta bo'ladigan 
#     ikkitasini ekranga chiqaruvchi programma tuzilsin.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A <= B and A <= C:
    print(B,"va",C)
elif B <= A and B <= C:
    print(A,'va',C)
else:
    print(A,'va',B)
     


# 16) A, B, C haqiqiy sonlar berilgan. Agar berilgan sonlar o'sish tartibida
#     berilgan bo'lsa, sonlarni ikkilantiring, aks holda sonlarni ishorasi
#     o'zgartirilsin. A, B, C ning qiymatlarini ekranga chiqaring.

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

if A < B < C:
    print(2*A,2*B,2*C)
else:
    print(-A,-B,-C)



# 17) A, B, C haqiqiy sonlar berilgan. Agar berilgan sonlar o'sish yoki kamayish
#     tartibida berilgan bo'lsa, sonlarni ikkilantiring, aks holda sonlarni 
#     ishorasi o'zgartirilsin. A, B, C ning qiymatlarini ekranga chiqaring.

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

if A < B < C  or  A > B > C:
    print(2*A,2*B,2*C)
else:
    print(-A,-B,-C)



# 18) Uchta butun son berilgan. Shu sonlarni ikkitasi o'zaro teng, qolgan
#     bittasini tartib raqami aniqlansin.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

if A == B:
    print(C)
elif A == C:
    print(B)
elif B == C:
    print(A)
else:
    print("Bu sonlar bir biriga teng emas.")



# 19) To'rtta butun son berilgan. Shu sonlarni uchtasi o'zaro teng, qolgan
#     bittasini tartib raqami aniqlansin.

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

if A == B == C:
    print(D)
elif A == B == D:
    print(C)
elif A == D == C:
    print(B)
elif D == B == C:
    print(A)
else:
    print("Bu sonlarning 3 tasi bir biriga reng emas.")



# 20) Sonlar o'qida uchta a, b, c nuqtalar berilgan. a nuqtaga eng yaqin nuqta
#     va ular orasidagi masofa topilsin.

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

ab = abs(a-b)
ac = abs(a-c)
if ab > ac:
    print(ac)
else:
    print(ab)



# 21) Koordinatalar tekisligida butun son berilgan. Agar nuqta koordinata boshida
#     yotsa 0 chiqarilsin. Agar nuqta ox yoki oy o'qlarida joylashsa mos holda
#     1 va 2 chiqarilsin. Agar nuqta kordinata o'qida joylashmasa 3 chiqarilsin.

x = int(input("x = "))
y = int(input("y = "))

if x == 0 and y == 0:
    print(0)
elif x == 0 and y != 0:
    print(2)
elif x != 0 and y == 0:
    print(1)
else:
    print(3)



# 22) OX va OY koordinata o'qlarida yotmaydigan nuqta berilgan.
#     Nuqta joylashgan koordinata choragi aniqlansin.

x = int(input("x = "))
y = int(input("y = "))

if x > 0 and y > 0:
    print("1-chorak")
elif x < 0 and y > 0:
    print("2-chorak")
elif x < 0 and y < 0:
    print("3-chorak")
elif x > 0 and y < 0:
    print("4-chorak")
else:
    print("x yoki y ga 0 dan boshqa son kiriting")



from math import *

# 24 x haqiqiy soni berilgan. Quydagi funksiya hisoblansin.
#    x > 0    2*sin(x)         
#    x <= 0   x-6

x = float(input("x = "))
if x > 0:
    print(2*sin(x))
else:
    print(x-6)



# 25) x haqiqiy soni berilgan. Quydagi funksiya hisoblansin.
#     x < -2  or  x > 2    2 * x
#     else   -3 * x

x = float(input("x = "))
if x < -2  or  x > 2:
    print(2*x)
else:
    print(-3*x)



# 26) x haqiqiy soni berilgan. Quydagi funksiya hisoblansin.
#           |  -x,  agar  x <= 0
#     f(x)  |  x**2, agar 0 < x < 2
#           |  4, agar  x >= 2

x = float(input("x = "))
if x <= 0:
    print(-x)
elif 0 < x < 2:
    print(x**2)
else:
    print(4)



# 27) x haqiqiy soni berilgan. Quydagi funksiya hisoblansin.
#           0,  agar  x < 0
#           1, agar 0 <= x < 1  or  2 <= x < 3
#           -1, agar 1 <= x < 2  or  3 <= x < 4 

x = float(input("x = "))
if x < 0:
    print(0)
elif int(x) % 2 == 0:
    print(1)
elif int(x) % 2 == 1 :
    print(-1)
else:
    print("Berilgan oraliqdagi sonni kiriting")



# 28) Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini
#     aniqlovchi programma tuzilsin. Kabisa bo'lsa 366 kun, bo'lmasa 365 kun bor.

yil = int(input("Yilni kiriting - "))

if yil % 400 == 0:
    print("366 kun")
elif yil % 100 == 0:
    print("365 kun")
elif yil % 4 == 0:
    print("366 kun")
else:
    print("365 kun")



# 29) Butun son berilgan. Berilgan sonni "musbat toq son", "manfiy juft son",
#     "son nolga teng" va x.k ekranga yozadigan programma tuzilsin.

son = int(input("son = "))
if son > 0:
    a = son % 2
    if a == 0:
        print("musbat juft son")
    else:
        print("musbat toq son")
elif son < 0:
    a = son % 2
    if a == 0:
        print("manfiy juft son")
    else:
        print("manfiy toq son")
else:
    print("son nolga teng")



# 30) 1-999 oraliqdagi sonlar berilgan. Berilgan sonni "Ikki honali juft son",
#     "uch honali toq son" va x.k ekranga yozadigan programma tuzilsin.

son = int(input("1-999 oralig'ida biror bir son kiriting - "))

if 1 <= son < 10:
    a = son % 2
    if a == 0:
        print("bir honali juft son")
    else:
        print("bir honali toq son")
elif 10 <= son < 100:
    a = son % 2
    if a == 0:
        print("ikki honali juft son")
    else:
        print("ikki honali toq son")
elif 100 <= son < 1000:
    a = son % 2
    if a == 0:
        print("uch honali juft son")
    else:
        print("uch honali toq son")
else:
    print("1-999 oralig'idagi sonni kiriting")

"""

