"""
Created on Thu Jan 27 10:37:18 2022

"""


#  1 - DARS


"""
# 1) Kvadratnik tomoni a berilgan. Uning perimetri aniqlansin. P = 4 * a
a = int(input("Kvadratning tomonini kiriting - "))
print(f"Tomoni a = {a} ga teng bo'lgan kvadratning perimetri P = {4 * a} ga teng")


# 2) Kvadratnik tomoni a berilgan. Uning yuzini aniqlang. S = a ** 2
a = int(input("Kvadratning tomonini kiriting - "))
print(f"Tomoni a = {a} ga teng bo'lgan kvadratning yuzi S = {a ** 2} ga teng")


# 3) To'g'ri to'rtbuechakning tomonlari a va b berilgan. Uning yuzasi S = a * b
#    va P = 2 * (a + b) perimetri aniqlansin.
print("To'g'ri to'rtburchakning tomonlarini kiriting")
a = int(input("a = "))
b = int(input("b = "))
print("S = ",a*b)
print("P = ",2*(a+b))


# 4) Aylananing diametri d berilgan. Uning uzunligi aniqlansin. L = п * d п = 3.14
d = float(input("Aylananing diametrini kiriting - "))
print("L = ",3.14 * d)


# 5) Kubning yon tomoni a berilgan. Uning hajmi V = a**3 va to'la sirti S = 6*(a**2) aniqlansin.
a = float(input("Kubning tomonini kiriting - "))
V = a**3
S = 6*(a**2)
print("V = ",V)
print("S = ",S)


# 6) Paralelepipedning tomonlari a, b, c berilgan. Uning hajmini V = a*b*c va 
#    to'la sirti S = 2*(a*b + a*c + b*c) aniqlansin.
print("Paralelepipedning tomonlarini kiriting")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("v = ",a*b*c)
print("S = ",2*(a*b + a*c + b*c))


# 7) Doiraning radiusi R berilgan. Uning uzunligi L va yuzasi S aniqlansin.
#    L = 2*п*R va S = п*R
R = float(input("Doiraning radiusini kiriting R = "))
print("L = ", 2 * 3.14 * R)
print("S = ", 3.14* R)


# 8) Ikkita son a va b berilgan. Ularning o'rta arifmetigi aniqlansin. (a+b)/2
print("Ikkita sonni kiriting")
a = float(input("Birinchi son - "))
b = float(input("Ikkinchi son - "))
print((a + b)/2)


# 9) Ikkita manfiy bo'lmagan son a va b berilgan. Ularning o'rta geometrigi 
#    aniqlansin. (a * b)**(1/2)
print("Ikkita musbat son kiriting")
a = float(input("Birinchi son - "))
b = float(input("Ikkinchi son - "))
print((a * b)**(1/2))


# 10) Nolga teng bo'lmagan ikkita son berilgan. Ularning yig'indisini, ko'paytmasini
#     va har birining kvadrati aniqlansin.
print("Nolga teng bo'lmagan ikkita son kiriting")
a = float(input("Birinchi son - "))
b = float(input("Ikkinchi son - "))
print("Yig'idisi  ", a + b)
print("Ko'paytmasi  ", a * b)
print("Birinchisining kvadrati  ", a ** 2)
print("Ikkinchisining kvadrati  ", b ** 2)


# 11) Nolga teng bo'lmagan ikkita son berilgan. Ularning yig'indisini, ko'paytmasini
#     va har birining moduli aniqlansin.
a = float(input("Birinchi son - "))
b = float(input("Ikkinchi son - "))
print("Yig'idisi  ", a + b)
print("Ko'paytmasi  ", a * b)
if a > 0:
    print("Birinchining moduli  ", a )
else:
    print("Birinchi sonning moduli  ", -a )
if b > 0:
    print("Ikkinchi sonning moduli  ", b )
else:
    print("Ikkinchi sonning moduli  ", -b )

    
# 12) To'g'ri uchburchakning katetlari a va b berilgan. Uning gipatinuzasi c va
#     perimetri P aniqlansin. c = (a**2 + b**2) ** (1/2)   P = a + b + c 
print("Uchburchakning katetlarini kiriting")
a = float(input("a = "))
b = float(input("b = "))
c = (a**2 + b**2) ** (1/2)
print("Gipatinuzasi  c = ", c)
print("Perimetri  P = ", a + b + c)


# 13) Umumiy markazga ega bo'lgan ikkita aylana radiusi berilgan R1, R2 (R1 > R2)
#     Ularning yuzalari S1 va S2, ularning ayirmasi S3 aniqlansin.
#     S1 = п * (R1**2), S2 = п * (R2**2), S3 = п * ((R1 - R2)**2)
п = 3.14
print("Aylananing radiuslarini kiriting(R1 > R2)")
R1 = float(input("R1 = "))
R2 = float(input("R2 = "))
S1 = п * (R1**2)
S2 = п * (R2**2)
S3 = п * ((R1 - R2)**2)
print("S1 = ",S1)
print("S2 = ",S2)
print("S3 = ",S3)


# 14) Aylananing uzunligi L berilgan. Uning radiusi R va yuzasi S aniqlansin.
#     L = 2*п*R   S = п * (R**2)   п = 3.14
L = float(input("Aylananing uzunligini kiriting  L = "))
п = 3.14
R = L / (2*п)
print("R = ", L / (2*п))
print("S = ", п * (R**2))


# 15) Aylananing yuzasi S berilgan. Uning diametri d va radiusi R aniqlansin.
#     S = п * (R**2)   п = 3.14
S = float(input("Aylananing yuzasini kiriting  S = "))
п = 3.14
R = (S / п) ** 0.5
d = 2 * R
print("R = ", R)
print("d = ", d)


# 16) Sonlar o'qida ikkita nuqta orasidagi masofa aniqlansin. |x2 - x1|
print("Nuqtalarni kiriting")
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
if x2 >= x1:
    print("|x2 - x1| = ", x2 - x1)
else:
    print("|x1 - x2| = ", x1 - x2)


# 17) Sonlar o'qida A, B, C nuqtalar berilgan. AC va BC kesmalarning uzunligi
#     va kesmalar uzunligining yig'indisini topuvchi programma tuzilsin.
print("Nuqtalarni kiriting")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
AC = abs(A - C)
BC = abs(B - C)
ABC = AC + BC
print("AC = ", AC)
print("BC = ", BC)
print("AC + BC = ", ABC)


# 18) Sonlar o'qida A, B, C nuqtalar berilgan. C nuqta A va B nuqtalar orasida
#     joylashgan. AC va BC kesmalar uzunligining ko'paytmasini toping.(A>C>B)
print("Nuqtalarni kiriting")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
print("AC X BC = ", (C-A)*(B-C))


# 19) To'g'ri to'rtburchakning qarama-qarshi uchlari koordinatalari berilgan.
#     Uning tomonlari koordinata o'qiga parallel. To'g'ri to'rtburchakning 
#     perimetri va yuzasi aniqlansin. (x1; y1)   (x2; y2)
print("To'g'ri to'rtburchakning koordinatalarini kiriting (x1; y1)  (x2; y2)")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
xx = abs(x1 - x2)
yy = abs(y1 - y2)
P = 2 * (xx + yy)
S = xx * yy
print("P = ", P)
print("S = ", S)


# 20) Tekislikdagi  berilgan ikki nuqta (x1; y1) va (x2; y2) orasidagi masofa
#     topilsin.  sqrt[ (x1 - x2)**2 + (y1 - y2)**2 ]
print("Koordinatalarni kiriting")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
print(f"S = { ((x1 - x2)**2 + (y1 - y2)**2)**0.5 }")


# 21) Uchburchakning uchta tomoni uchlari koordinatalari berilgan (x1; y1), (x2; y2)
#     va (x3; y3). Ikki nuqta orasidagi masofani topish sqrt[ (x1 - x2)**2 + (y1 - y2)**2 ]
#     Uchburchakning yuzasini va perimetrini toping.
#     S = ( P*(P-a)*(P-b)*(P-c))**0.5    P = (a + b + c)/2
print("Uchburchakning koordinatalarini kiriting")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))
x3 = float(input("x3 = "))
y3 = float(input("y3 = "))
a = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
b = ((x2 - x3)**2 + (y2 - y3)**2)**0.5
c = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
P = (a + b + c)/2
S = ( P*(P-a)*(P-b)*(P-c))**0.5
print("P = ", P*2)
print("S = ", S)


# 22) Berilgan A va B sonlarning qiymatlarini almashtiring. A va B ning yangi
#     qiymati ekranga chiqarilsin.
print("A va B ning qiymatlarini kiriting")
A = float(input("A = "))
B = float(input("B = "))
A, B = B, A
print("A =",A)
print("B =",B)


# 23) A, B va C sonlar berilgan A ni qiymati B ga, B ni qiymati C ga, C ni qiymati
#     A ga almashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
print("A, B va C ning qiymatlarini kiriting")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
A, B, C = B, C, A
print("A =", A)
print("B =", B)
print("C =", C)


# 24) A, B va C sonlar berilgan. A ni qiymati C ga, C ni qiymati B ga va B ni 
#     qiymati A ga almashtirilsin. A, B va C ning yangi qiymatlari ekranga chiqarilsin.
print("A, B va C ning qiymatlarini kiriting")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
A, B, C = C, A, B
print("A =", A)
print("B =", B)
print("C =", C)


# 25) x ning qiymati berilganda y = 3*(x**6) - 6*(x**2) - 7 funksiyani qiymatini toping
x = float(input("x ning qiymatini kiriting  x = "))
print(f"y = { 3*(x**6) - 6*(x**2) - 7 }")


# 26) x ning qiymati berilganda y = 4*((x-3)**6) - 7*((x-3)**3 + 2
#     funksiyani qiymatini toping
x = float(input("x ning qiymatini kiriting  x = "))
print(f"y = { 4*((x-3)**6) - 7*((x-3)**3) + 2 }")


# 27) A soni berilgan. A ning A**2, A**4 va A**8 darajalarini 
#     aniqlovchi programma tuzilsin
A = float(input("A = "))
print("A2 =", A**2)
print("A4 =", A**4)
print("A8 =", A**8)


# 28) A soni berilgan. A ning A**2, A**3, A**5, A**10, A**15 darajalarini
#     aniqlovchi programma tuzing.
A = float(input("A = "))
print("A2 =", A**2)
print("A3 =", A**3)
print("A5 =", A**5)
print("A10 =", A**10)
print("A15 =", A**15)


# 29) a burchak gradusda berilgan (0 < a < 360). Berilgan burchakning qiymati
#     radianga o'tkazuvchi programma tuzilsin.
a = float(input("a = "))
print("Rad =", a*3.14/180)


# 30) a burchak radianda berilgan (0 < a < 2п). Berilgan burchakning qiymatini
#     gradusga o'tkazuvchi programma tuzilsin. п = 3.14
a = float(input("a = "))
print("Burchak =", a*180/3.14)


# 31) Temperatura Tf Ferengeytda berilgan. Temperatura qiymatini Tc gradus
#     selsiyga o'tkazuvchi programma tuzilsin. Tc = ( Tf - 32 ) * 5 / 9
Tf = float(input("Tf = "))
print("Tc =", ( Tf - 32 ) * 5 / 9 )


# 32) Temperatura Tc selsiyda berilgan. Temperatura qiymatini Tf gradus
#     Ferengeytga o'tkazuvchi programma tuzilsin. Tc = ( Tf - 32 ) * 5 / 9
Tc = float(input("Tc = "))
print("Tf =",  Tc * 9 / 5 + 32  )


# 33) x kg kanfet a so'm turadi. 1 kg kanfet qancha turishini
#     aniqlovchi programma tuzilsin.
x = float(input("x = "))
a = float(input("a = "))
print(x, "kg   ", a,"so'm")
print(1, "kg   ", a/x,"so'm")


# 34) x kg shokolad a so'm turadi va y kg kanfet b so'm turadi. 1 kg shokolad  
#     1 kg kanfetdan qancha qimmat turishini aniqlovchi programma tuzilsin.
x = float(input("x = "))
a = float(input("a = "))
y = float(input("y = "))
b = float(input("b = "))
print(x, "kg shokolad    ", a,"so'm")
print(y, "kg kanfet    ", b,"so'm")
print(1, "kg shokolad    ", a/x,"so'm")
print(1, "kg kanfet    ", b/y,"so'm")
print("1 kg shokolad 1 kg kanfetdan", a/x - b/y, "so'm qimmat turadi")


# 35) Qayiqning tezligi v km/soat, daryo oqimining tezligi u km/soat,( v > u ).
#     Qayiqning daryo oqimi bo'yicha harakatlanish vaqti t1, oqimga qarshi t2.
#     Qayiqning yurgan s yo'lini aniqlovchi programma tuzilsin.
print("Qayiqning oqim bo'yicha tezligi va vaqtini kiriting")
v = float(input("v = "))
t1 = float(input("t1 = "))
print("Qayiqning oqimga qarshi tezligi va vaqtini kiriting")
u = float(input("u = "))
t2 = float(input("t2 = "))
s = v * t1 - u * t2
print("Qayiqning yurgan yo'li",s,"km")


# 36) Birinchi avtomobilning tezligi v1 km/soat, ikkinchisiniki v2 km/soat,
#     ular orasidagi masofa s. Ular bir-biridan uzoqlasha boshlasa t vaqtdan
#     keyin ular orasidagi masofani aniqlaydigan programma tuzilsin.
print("Avtomobillarning tezliklari ular orasidagi masofa va vaqtini kiriting")
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))
s = float(input("s = "))
t = float(input("t = "))
S = s + (v1 + v2) * t
print("Avtomobillar orasidagi masofa",S,"km")


# 37) Birinchi avtomobilning tezligi v1 km/soat, ikkinchisiniki v2 km/soat,
#     ular orasidagi masofa s. Ular bir-biri tomonga harakatlana boshlasa t vaqtdan
#     keyin ular orasidagi masofani aniqlaydigan programma tuzilsin.
v1 = float(input("v1 = "))
v2 = float(input("v2 = "))
s = float(input("s = "))
t = float(input("t = "))
S = s - (v1 + v2) * t
print("Avtomobillar orasidagi masofa",abs(S),"km")


# 38) A va B koefetsentlari berilgan, Ax + B = 0 chiziqli tenglamaning yechimini
#     (x ni) aniqlaydigan programma tuzilsin. (A != 0)
print("Ax + B = 0 Chiziqli tenglamaning koefitsentlarini kiriting")
A = float(input("A = "))
B = float(input("B = "))
x = -(B/A)
print("x = ",x)


# 39) A, B, va C koefetsentlari berilgan, A(x**2) + Bx + C = 0 kvadrat tenglamaning
#     diskriminanti noldan katta bo'lsa uning yechimlarini aniqlaydigan programma
#     tuzilsin. (A != 0)  D = B**2 - 4AC  x1,2 = (-B +- (D**0.5))/(2*A)
print("Kvadrat tenglamaning koefetsentlarini kiriting")
A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))
D = B**2 - 4 * A * C
if D > 0:
    x1 = (-B + (D**0.5))/(2*A)
    x2 = (-B - (D**0.5))/(2*A)
    print("x1 =",x1, "  va  x2 =",x2)
elif D == 0:
    x = -B / (2*A)
    print("x =",x)
else:
    print("Tenglamaning yechimi yo'q")


# 40) A1, B1, C1,   A2 ,B2, C2 koefetsentlar berilgan, chiziqli tenglamalar sistemasi
#     yechimlarini aniqlaydigan programma tuzilsin.
#     A1x + B1y = C1    x = (C1*B2 - C2*B1) / (A1*B2 - A2*B1)
#     A2x + B2y = C2    y = (A1*C2 - A2*C1) / (A1*B2 - A2*B1)
print("A1x + B1y = C1")
print("A2x + B2y = C2")
print("Tenglamalar sistemasining koefetsentlarini kiriting")
A1 = float(input("A1 = "))
B1 = float(input("B1 = "))
C1 = float(input("C1 = "))
A2 = float(input("A2 = "))
B2 = float(input("B2 = "))
C2 = float(input("C2 = "))
x = (C1*B2 - C2*B1) / (A1*B2 - A2*B1)
y = (A1*C2 - A2*C1) / (A1*B2 - A2*B1)
print("x =",x)
print("y =",y)







#   2 - DARS


# kunni kiritsangiz necha haftayu necha kunligini aniqlaydigan pragramma
a = input("kunni kiriting - ")
b = a % 7
print(a//7, "hafta",a%7,"kun")


# kilobaytni kiritsangiz necha mb va kb ekanligini aniqlaydigan programma
a = int( input("kilobaytni kiriting - "))
print(a//1024,"mb",a%1024,"kb")


# uch honali son kiritsangiz teskarisiga chiqaradigan pragramma 245   542
a = int(input("uch honali son kiriting - "))
s = a // 100
d = a // 10
f = d % 10
g = a % 10
j = g * 100 + f * 10 +s
print(j)
"""


# sekundni kiritsangiz necha soat, minut, sekund ekanligini aniqlaydigan programma
a = int(input("sekundni kiriting - "))
soat = a // 3600
minut = (a - soat * 3600) // 60
sekund = a - soat * 3600 - minut * 60 
print(soat,"soat",minut,"minut",sekund,"sekund")









