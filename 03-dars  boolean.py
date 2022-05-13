
# 1) A butun sonlar berilgan. Jumlani rostlikka tekshiring: "A soni musbat".

A = int(input("A = "))
print(A > 0)



# 2) A butun sonlar berilgan. Jumlani rostlikka tekshiring: "A soni toq son".

A = int(input("A = "))
print(A % 2 == 1)



# 3) A butun sonlar berilgan. Jumlani rostlikka tekshiring: "A soni juft son".

A = int(input("A = "))
print(A % 2 == 0)



# 4) Ikkita butun A va B sonlari berilgan. Jumlani rostlikka tekshiring:
#    A > 2   va   B <= 3

A = int(input("A = "))
B = int(input("B = "))
print(A > 2   and   B <= 3)



# 5) Ikkita butun A va B sonlar berilgan. Jumlani rostlikka tekshiring:
#    A >= 0   yoki   B <= 2 

A = int(input("A = "))
B = int(input("B = "))
print(A >= 0   or   B < -2 )



# 6) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring: A<=B<=C

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A<=B<=C)



# 7) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
#    "B soni A va C sonlari orasida yotadi"

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A < B < C)



# 8) Ikkita butun A va B butun sonlar berilgan. Jumlani rostlikka tekshiring:
#    "A va B sonlari toq sonlar"

A = int(input("A = "))
B = int(input("B = "))
print(A % 2 == B % 2 == 1)



# 9) Ikkita butun A va B butun sonlar berilgan. Jumlani rostlikka tekshiring:
#    "A va B sonlarning hech bo'lmaganda bittasi toq son.

A = int(input("A = "))
B = int(input("B = "))
print(A % 2 == 1   or   B % 2 == 1)



# 10) Ikkita A va B butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A va B sonlarining faqat bittasi toq son".

A = int(input("A = "))
B = int(input("B = "))
print( A % 2 == 1  and  B % 2 == 0     or     A % 2 == 0  and  B % 2 == 1 )



# 11) Ikkita butun A va B butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A va B sonlarining har ikkalasi ham yoki toq son yoki juft son".

A = int(input("A = "))
B = int(input("B = "))
print( A % 2 == 1  and  B % 2 == 1     or     A % 2 == 0  and  B % 2 == 0 )



# 12) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A, B, C sonlarning har biri musbat".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A > 0  and  B > 0  and  C > 0)



# 13) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A, B, C sonlarning hech bo'lmaganda bittasi musbat".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A > 0  or  B > 0  or  C > 0)



# 14) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A, B, C sonlarning faqat bittasi musbat son".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A>0 and B<=0 and C<=0  or  A<=0 and B>0 and C<=0  or  A<=0 and B<=0 and C>0)



# 15) Uchta A, B, C butun sonlar berilgan. Jumlani rostlikka tekshiring:
#     "A, B, C sonlarning faqat ikkitasi musbat son".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(A>0 and B>0 and C<=0  or  A>0 and B<=0 and C>0  or  A<=0 and B>0 and C>0)



# 16) Musbat butun son berilgan. Jumlani rostlikka tekshiring:
#     "Berilgan son ikki honali juft son".

A = int(input("A = "))
print(A % 2 == 0  and  9 < A < 100)



# 17) Musbat butun son berilgan. Jumlani rostlikka tekshiring:
#     "Berilgan son uch honali toq son".

A = int(input("A = "))
print(A % 2 == 1  and  99 < A < 1000)



# 18) Jumlani rostlikka tekshiring. "Berilgan uchta butun sonlarning hech
#     bo'lmaganda ikkitasi bir-biriga teng".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print( A == B or A == C or B == C or A == B == C)



# 19) Jumlani rostlikka tekshiring. "Berilgan uchta butun sonlarning hech
#     bo'lmaganda bir jufti o'zaro qarama-qarshi".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print( A == -B or A == -C or B == -C )



# 20) Uch honali son berilgan. Jumlani rostlikka tekshiring:
#     "Ushbu sonning barcha raqamlari xar xil".

A = int(input("A = "))
bir = A // 100
ikki = A % 100 // 10
uch = A % 10
print(bir != ikki and bir != uch and ikki != uch)



# 21) Uch honali son berilgan. Jumlani rostlikka tekshiring:
#     "Ushbu sonning raqamlari ketma-ket o'suvchi bo'lib joylashgan".

A = int(input("A = "))
bir = A // 100
ikki = A % 100 // 10
uch = A % 10
print(bir < ikki < uch)



# 22) Uch honali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonning
#     raqamlari ketma-ket o'suvchi yoki kamayuvchi bo'lib joylashgan".

A = int(input("A = "))
bir = A // 100
ikki = A % 100 // 10
uch = A % 10
print(bir < ikki < uch   or   bir > ikki > uch)



# 23) Uch honali son berilgan. Jumlani rostlikka tekshiring: "Ushbu sonni 
#     chapdan o'qiganda ham, o'ngdan o'qiganda ham bir hil".

A = int(input("A = "))
bir = A // 100
ikki = A % 100 // 10
uch = A % 10
print(bir == ikki == uch)



# 24) A, B, C sonlar berilgan (A soni noldan farqli). D = B**2 - 4*A*C
#     diskerminantdan foydalanib, jumlani rostlikka tekshiring:
#     "A*(x**2)+B*x+C kvadrat tenglama haqiqiy ildizga ega".

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = B**2 - 4*A*C
print(D >= 0)



# 25) x, y sonlar berilgan. Jumlani rostlikka tekshirng: "Koordinatalari
#     (x,y) bo'lgan nuqta, koordinata choragining ikkinchisida yotadi".

x = int(input("x = "))
y = int(input("y = "))
print(x < 0  and  y > 0)



# 26) x, y sonlar berilgan. Jumlani rostlikka tekshiring: "Koordinatalari
#     (x,y) bo'lgan nuqta, koordinata choragining to'rtinchisida yotadi".

x = int(input("x = "))
y = int(input("y = "))
print(x > 0  and  y < 0)



# 27) x, y sonlar berilgan. Jumlani rostlikka tekshirng: "Koordinatalari
#     (x,y) bo'lgan nuqta, koordinata choragining 2-sida yoki 3-sida yotadi".

x = int(input("x = "))
y = int(input("y = "))
print(x < 0 and y > 0   or   x < 0 and y < 0)



# 28) x, y sonlar berilgan. Jumlani rostlikka tekshirng: "Koordinatalari
#     (x,y) bo'lgan nuqta, koordinata choragining 1-sida yoki 3-sida yotadi".

x = int(input("x = "))
y = int(input("y = "))
print(x > 0 and y > 0   or   x < 0 and y < 0)



# 29) (x,y), (x1,y1), (x2,y2) sonlari berilgan. Jumlani rostlikka tekshiring:
#     "Koordinatalari (x,y) bo'lgan nuqta, chap yuqori cho'qqisi (x1,y1)
#     koordinatalarga ega bo'lgan va o'ng pastkisi (x2,y2) bo'lgan, tomonlari
#     esa koordinata o'qlariga parallel bo'lgan to'rtburchak ichida yotadi".

x = int(input("x = "))
y = int(input("y = "))
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print(x1 < x < x2  and  y2 < y < y1)



# 30) a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c
#     tomonli uchburchak teng tomonli bo'ladi".

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a == b == c)



# 31) a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c
#     tomonli uchburchak teng yonli bo'ladi".

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a == b or a == c or b == c)



# 32) a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c
#     tomonli uchburchak to'g'ri burchakli bo'ladi".

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2)



# 33) a, b, c butun sonlar berilgan. Jumlani rostlikka tekshiring: "a, b, c
#     tomonli uchburchak yasash mumkin".

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print(a + b > c and a + c > b and b + c > a)



# 34) Shaxmat doskasining x, y kordinatalari berilgan (1-8 oraliqda yotuvchi
#     butun sonlar). Doskaning chap pastki maydoni (1,1) qoraligini hisobga olib
#     jumlani roslikka tekshiring: "Berilgan (x,y) maydon oq".

x = int(input("x = "))
y = int(input("y = "))
print(x % 2 == 0 and y % 2 == 1   or   x % 2 == 1 and y % 2 == 0)



# 35) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Berilgan maydonlar bir xil rangda"

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a =   x1 % 2 ==  1  and  y1 % 2 == 0    and   x2 % 2 == 1  and  y2 % 2 == 0
b =   x1 % 2 ==  0  and  y1 % 2 == 1    and   x2 % 2 == 0  and  y2 % 2 == 1
c =   x1 % 2 ==  0  and  y1 % 2 == 0    and   x2 % 2 == 0  and  y2 % 2 == 0
d =   x1 % 2 ==  1  and  y1 % 2 == 1    and   x2 % 2 == 1  and  y2 % 2 == 1
print( a or b or c or d )



# 36) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Rux bir yurishda bir maydondan ikkinchisiga o'ta oladi".

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a =  x1 != x2  and  y1 == y2   or   x1 == x2  and  y1 != y2
print(a)



# 37) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Shoh bir yurishda bir maydondan ikkinchisiga o'ta oladi".

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a =  x1 + 1 == x2  and  y1 == y2   or   x1 - 1 == x2  and  y1 == y2
b =  y1 + 1 == y2  and  x1 == x2   or   y1 - 1 == y2  and  x1 == x2
c =  x1 + 1 == x2  and  y1 + 1 == y2   or   x1 - 1 == x2  and  y1 - 1 == y2
d =  x1 + 1 == x2  and  y1 - 1 == y2   or   x1 - 1 == x2  and  y1 + 1 == y2
print(a or b or c or d)



# 38) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Fil bir yurishda bir maydondan ikkinchisiga o'ta oladi".

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

n = abs(x1 - x2)
a =  x1 != x2           and  y1 != y2
b =  x1 + n == x2       and  y1 + n == y2
c =  abs(x1 - n) == x2  and  abs(y1 - n) == y2
d =  x1 + n == x2       and  abs(y1 - n) == y2
e =  abs(x1 - n) == x2  and  y1 + n == y2

print(a and b or c or d or e)



# 39) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Farzin bir yurishda bir maydondan ikkinchisiga o'ta oladi".

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a =  x1 != x2  and  y1 == y2   or   x1 == x2  and  y1 != y2   # RUX

n = abs(x1 - x2)                                              # FIL
t =  x1 != x2           and  y1 != y2                
b =  x1 + n == x2       and  y1 + n == y2
c =  abs(x1 - n) == x2  and  abs(y1 - n) == y2
d =  x1 + n == x2       and  abs(y1 - n) == y2
e =  abs(x1 - n) == x2  and  y1 + n == y2

print(a or t and b or c or d or e)


# 40) Shaxmat doskasining ikkita turli (x1,y1), (x2,y2) koordinatalari berilgan.
#     (1-8 oraliqda yotuvchi butun sonlar). jumlani roslikka tekshiring: 
#     "Ot bir yurishda bir maydondan ikkinchisiga o'ta oladi".

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

a =  x1 + 1 == x2  and  y1 + 2 == y2   or   x1 - 1 == x2  and  y1 + 2 == y2
b =  x1 + 2 == x2  and  y1 + 1 == y2   or   x1 + 2 == x2  and  y1 - 1 == y2
c =  x1 - 2 == x2  and  y1 + 1 == y2   or   x1 - 2 == x2  and  y1 - 1 == y2
d =  x1 + 1 == x2  and  y1 - 2 == y2   or   x1 - 1 == x2  and  y1 - 2 == y2

print(a or b or c or d)

