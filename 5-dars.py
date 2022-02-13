"""
Created on Wed Feb  9 10:20:41 2022
"""

"""
#  B O' L I N M A   ishlagani yuq

a = int(input("Bo'linuvchini kiriting:  a = "))
b = int(input("Bo'luvchini kiriting:  b = "))
s = 0
n = 0
while s <= a:
    s += b
    n += 1
qol = s - b
qoldiq = a - qol

w = 0
y = qoldiq
while y != 0:
    w += 10
    y -= 1
   
s = 0
u = 0
while s <= w:
    s += b
    u += 1

print(n-1,u-1,sep=".")





#  K O' P A Y T M A

a = int(input("1-ko'paytuvchini kiriting:  a = "))  
b = int(input("2-ko'paytuvchini kiriting:  b = "))  
s = 0
n = a
while n != 0:
    s += b
    n -= 1
print(s)




#  Q O L D I Q L I     B O' L I S H

a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
s = 0
while s <= a:
    s += b
print(a - (s - b))





#  B U T U N   B O' L I S H

a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
s = 0
n = 0
while s <= a:
    s += b
    n += 1
print(n-1)





#  D A R A J A G A   K O' T A R I S H    ishlagani yuq

a = int(input("Sonni kiriting:  a = "))  
b = int(input("Darajani kiriting:  b = "))
s = 0
n = b -1
while  n != 0:
    a += a
    n -= 1
print(a)


"""

"""
# 1) 1-7 gacha bo'lgan butun sonlar berilgan. Kiritilgan songa mos ravishta
#    hafta kunlari so'zda ifodalovchi programma tuzilsin.

kun = int(input("kunni kiriting(1-7) - "))
if kun == 1:
    print("Dushanba")
elif kun == 2:
    print("Seshanba")
elif kun == 3:
    print("Chorshanba")
elif kun == 4:
    print("Payshanba")
elif kun == 5:
    print("Juma")
elif kun == 6:
    print("Shanba")
elif kun == 7:
    print("Yakshanba")
else:
    print("1-7 oralig'idagi sonni kiriting.")



# 2) K butun son berilgan. Baho natijalarini chiqaruvchi programma tuzing.
#    (1-yomon, 2-qoniqarsiz, 3-qoniqarli, 4-yaxshi, 5-a'lo). Agar k soni
#    1-5 gacha oraliqqa tegishli bo'lmasa "xato" deb chiqarilsin.

k = int(input("(1-5):  k = "))
if k == 1:
    print("yomon")
elif k == 2:
    print("qoniqarsiz")
elif k == 3:
    print("qoniqarli")
elif k == 4:
    print("yaxshi")
elif k == 5:
    print("a'lo")
else:
    print("xato")



# 3) Oy raqamini berilgan. Kiritilgan oy qaysi faslga tegishli ekanligini
#    chiqaruvchi programma tuzilsin. (Masalan: 2 chi oy, "qish")

k = int(input("(1-12):  k = "))
if 1 <= k <= 3:
    print("Qish")
elif 4 <= k <= 6:
    print("Bahor")
elif 7 <= k <= 9:
    print("Yoz")
elif 10 <= k <= 12:
    print("Kuz")
else:
    print("Bunday oy yo'q")



# 4) Oy raqamini berilgan. Shu oyda nechta kun borligini aniqlang.

k = int(input("(1-12):  k = "))
if k == 1 or k == 3 or k == 5 or k == 7 or k == 8 or k == 10 or k == 12:
    print(31)
elif k == 4 or k == 6 or k == 9 or k == 11:
    print(30)
elif k == 2:
    print(28)
else:
    print("Bunday oy yo'q")



# 5) A, B haqiqiy va amal butun soni berilgan. A va B sonlari ustida arifmetik
#    amallar bajaruvchi programma tuzilsin. Amal quydagi qiymatlarni qabul qiladi
#    1-qo'shish, 2-ayirish, 3-bo'lish, 4-ko'paytirish.

A = float(input("A = "))
B = float(input("B = "))
amal = int(input("qaysi amalni tanlaysiz"  '\n'
      "1-qo'shish"  '\n'
      "2-ayirish"   '\n'
      "3-bo'lish"   '\n'
      "4-ko'paytirish"  '\n' ))

if amal == 1:
    print(A,"+",B,"=",A+B)
if amal == 2:
    print(A,"-",B,"=",A-B)
if amal == 3:
    print(A,"/",B,"=",round(A/B,3))
if amal == 4:
    print(A,"*",B,"=",A*B)



# 6) Uzunlik birliklari quydagi tartibda berilgan. 1-km, 2-m, 3-dm, 4-sm, 5-mm
#    Uzunlik birligini bildiruvchi son berilgan. (1-5 oraliqda) va shu birlikdagi
#    kesma uzunligi berilgan(haqiqiy son). Kesmaning uzunligi metrlarda
#    ifodalovchi programma tuzilsin.

son = int(input("Uzunlik - "))
birlik = int(input("1-5 oraliqda"'\n'
                   "1-km"   '\n'
                   "2-m"    '\n'
                   "3-dm"   '\n'
                   "4-sm"   '\n'
                   "5-mm"   '\n'
                   "Kiriting - "))

if birlik == 1:
    print(son*1000,"metr")
elif birlik == 2:
    print(son,"metr")
elif birlik == 3:
    print(son/10,"metr")
elif birlik == 4:
    print(son/100,"metr")
elif birlik == 5:
    print(son/1000,"metr")
else:
    print("1-5 oralig'idagi sonni kiriting.")



# 7) Og'irlik birliklari quydagi tartibda berilgan. 1-kg, 2-mg, 3-g, 4-t, 5-sentner
#    Og'irlik birligini bildiruvchi soni berilgan va shu birlikdagi og'irlik
#    qiymati berilgan. Og'irlikni kg da ifodalovchi programma tuzilsin.

son = int(input("Og'irlik - "))
birlik = int(input("1-5 oraliqda"'\n'
                   "1-kg"   '\n'
                   "2-mg"    '\n'
                   "3-g"   '\n'
                   "4-t"   '\n'
                   "5-sentner"   '\n'
                   "Kiriting - "))

if birlik == 1:
    print(son,"kg")
elif birlik == 2:
    print(son/1000000,"kg")
elif birlik == 3:
    print(son/1000,"kg")
elif birlik == 4:
    print(son*1000,"kg")
elif birlik == 5:
    print(son*100,"kg")
else:
    print("1-5 oralig'idagi sonni kiriting.")



# 8) Sanani bildiruvchi ikkita butun son berilgan. D (kun)  va  M (oy). (Kabisa
#    bo'lmagan yil sanasi kiritiladi). Berilgan sanani ifodalovchi programma
#    tuzilsin. Kabisa yili - 366 kun, Kabisa yili bo'lmasa - 365 kun bor

kun = int(input("kun = "))
oy = int(input("oy = "))
yil = int(input("yil = "))

if yil % 400 == 0:
    kabisa = 1
elif yil % 100 == 0:
    kabisa = 0
elif yil % 4 == 0:
    kabisa = 1
else:
    kabisa = 0

if kabisa == 1 and kun == 29 and oy == 2:
    print("29 . 02 .",yil)
elif kabisa == 0 and kun == 29 and oy == 2:
    print("01 . 03 .",yil)
else:
    print(kun,".",oy,".",yil)



# 9) Ikkita butun son berilgan D (kun) M (oy). (Kabisa bo'lmagan yil sanasi
#    kiritiladi). Berilgan sanadan keyingi sanani ifodalovchi programma tuzilsin.

kun = int(input("kun = "))
oy = int(input("oy = "))
yil = int(input("yil = "))

if yil % 400 == 0:
    kabisa = 1
elif yil % 100 == 0:
    kabisa = 0
elif yil % 4 == 0:
    kabisa = 1
else:
    kabisa = 0


if kabisa == 1 and kun == 28 and oy == 2:
    print(kun+1,oy,yil)
elif kabisa == 1 and kun == 29 and oy == 2:
    print(1,oy+1,yil)
elif kabisa == 0 and kun == 28 and oy == 2:
    print(1,oy+1,yil)
elif kabisa == 0 and kun >= 28 and oy == 2:
    print("Xatolik yuz berdi!!!")
    
elif kun == 31 and (oy == 1 or oy == 3 or oy == 5 or oy == 7 or oy == 8 or oy == 10):
    print(1,oy+1,yil)
elif kun == 30 and (oy == 4 or oy == 6 or oy == 9 or oy == 11):
    print(1,oy+1,yil)
elif kun == 31 and oy == 12:
    print(1,1,yil+1)

elif 1 <= kun <= 30 and 1 <= oy <= 12:
    print(kun+1,oy,yil)
else:
    print("Xatolik yuz berdi!!!")



# 10) Robot faqat 4 tomonga ko'cha oladi.(s-shimol, j-janub, q-sharq, g-g'arb)
#     va uchta raqamli komanda 0-harakatni davom ettir, 1-chapga buril, 2-o'nga
#     buril. Y-robot yo'nalishi va k-kamanda berilgan. Berilgan kamanda 
#     bajarilgandan keyin, robot holatini aniqlovchi programma tuzilsin

yonalish = str(input("Yo'nalishni tanlang" '\n'
                     "s-shimol"  '\n'
                     "j-janub"   '\n'
                     "q-sharq"   '\n'
                     "g-g'arb"   '\n'
                     "kiriting - "))

kamanda = int(input("Kamandani tanlang"  '\n'
                    "0-harakatni davom ettir"  '\n'
                    "1-chapga buril"  '\n'
                    "2-o'nga buril"  '\n'
                    "kiriting - "))
                     
if yonalish == 's':
    if kamanda == 0:
        print("Yo'nalish: shimol,  Kamanda: shimolga harakatni davom ettir")
    elif kamanda == 1:
        print("Yo'nalish: shimol,  Kamanda: g'arbga buril")
    elif kamanda == 2:
        print("Yo'nalish: shimol,  Kamanda: sharqqa buril")

elif yonalish == 'j':
    if kamanda == 0:
        print("Yo'nalish: janub,  Kamanda: janubga harakatni davom ettir")
    elif kamanda == 1:
        print("Yo'nalish: janub,  Kamanda: sharqqa buril")
    elif kamanda == 2:
        print("Yo'nalish: janub,  Kamanda: g'arbga buril")

elif yonalish == 'q':
    if kamanda == 0:
        print("Yo'nalish: sharq,  Kamanda: sharqqa harakatni davom ettir")
    elif kamanda == 1:
        print("Yo'nalish: sharq,  Kamanda: shimolga buril")
    elif kamanda == 2:
        print("Yo'nalish: sharq,  Kamanda: janubga buril")

elif yonalish == 'g':
    if kamanda == 0:
        print("Yo'nalish: g'arb,  Kamanda: g'arbga harakatni davom ettir")
    elif kamanda == 1:
        print("Yo'nalish: g'arb,  Kamanda: janubga buril")
    elif kamanda == 2:
        print("Yo'nalish: g'arb,  Kamanda: shimolga buril")



# 11) Lokatr dunyoning bir tomoniga qaratilgan (s-shimol, j-janub, q-sharq, g-g'arb)
#     va uchta raqamli komanda 0-o'nga buril, 1-chapga buril, 2-burilish 180.C
#     C-lakatrning boshlang'ich holati va K1, K2 - kamandalar berilgan. Berilgan  
#     kamanda bajarilgandan keyin, lakatr holatini aniqlovchi programma tuzilsin

yonalish = str(input("Lokatrning boshlang'ich holati C ni" '\n'
                     "s-shimol"  '\n'
                     "j-janub"   '\n'
                     "q-sharq"   '\n'
                     "g-g'arb"   '\n'
                     "kiriting - "))

kamandak1 = int(input("K1 Kamandani tanlang"  '\n'
                    "0-o'nga buril"  '\n'
                    "1-chapga buril"  '\n'
                    "2-burilish 180.C"  '\n'
                    "kiriting - "))

kamandak2 = int(input("K2 Kamandani tanlang"  '\n'
                    "0-o'nga buril"  '\n'
                    "1-chapga buril"  '\n'
                    "2-burilish 180.C"  '\n'
                    "kiriting - "))



if yonalish == 's':
    if kamandak1 == 0 and kamandak2 == 0:
        print("Start: shimol,  Finish: janub")
    elif kamandak1 == 0 and kamandak2 == 1:
        print("Start: shimol,  Finish: shimol")
    elif kamandak1 == 0 and kamandak2 == 2:
        print("Start: shimol,  Finish: g'arb")

if yonalish == 's':
    if kamandak1 == 1 and kamandak2 == 0:
        print("Start: shimol,  Finish: shimol")
    elif kamandak1 == 1 and kamandak2 == 1:
        print("Start: shimol,  Finish: janub")
    elif kamandak1 == 1 and kamandak2 == 2:
        print("Start: shimol,  Finish: sharq")

if yonalish == 's':
    if kamandak1 == 2 and kamandak2 == 0:
        print("Start: shimol,  Finish: g'arb")
    elif kamandak1 == 2 and kamandak2 == 1:
        print("Start: shimol,  Finish: sharq")
    elif kamandak1 == 2 and kamandak2 == 2:
        print("Start: shimol,  Finish: shimol")




if yonalish == 'j':
    if kamandak1 == 0 and kamandak2 == 0:
        print("Start: janub,  Finish: shimol")
    elif kamandak1 == 0 and kamandak2 == 1:
        print("Start: janub,  Finish: janub")
    elif kamandak1 == 0 and kamandak2 == 2:
        print("Start: janub,  Finish: sharq")

if yonalish == 'j':
    if kamandak1 == 1 and kamandak2 == 0:
        print("Start: janub,  Finish: janub")
    elif kamandak1 == 1 and kamandak2 == 1:
        print("Start: janub,  Finish: shimol")
    elif kamandak1 == 1 and kamandak2 == 2:
        print("Start: janub,  Finish: g'arb")

if yonalish == 'j':
    if kamandak1 == 2 and kamandak2 == 0:
        print("Start: janub,  Finish: sharq")
    elif kamandak1 == 2 and kamandak2 == 1:
        print("Start: janub,  Finish: g'arb")
    elif kamandak1 == 2 and kamandak2 == 2:
        print("Start: janub,  Finish: janub")




if yonalish == 'q':
    if kamandak1 == 0 and kamandak2 == 0:
        print("Start: sharq,  Finish: g'arb")
    elif kamandak1 == 0 and kamandak2 == 1:
        print("Start: sharq,  Finish: sharq")
    elif kamandak1 == 0 and kamandak2 == 2:
        print("Start: sharq,  Finish: shimol")

if yonalish == 'q':
    if kamandak1 == 1 and kamandak2 == 0:
        print("Start: sharq,  Finish: sharq")
    elif kamandak1 == 1 and kamandak2 == 1:
        print("Start: sharq,  Finish: g'arb")
    elif kamandak1 == 1 and kamandak2 == 2:
        print("Start: sharq,  Finish: janub")

if yonalish == 'q':
    if kamandak1 == 2 and kamandak2 == 0:
        print("Start: sharq,  Finish: shimol")
    elif kamandak1 == 2 and kamandak2 == 1:
        print("Start: sharq,  Finish: janub")
    elif kamandak1 == 2 and kamandak2 == 2:
        print("Start: sharq,  Finish: sharq")




if yonalish == 'g':
    if kamandak1 == 0 and kamandak2 == 0:
        print("Start: g'arb,  Finish: sharq")
    elif kamandak1 == 0 and kamandak2 == 1:
        print("Start: g'arb,  Finish: g'arb")
    elif kamandak1 == 0 and kamandak2 == 2:
        print("Start: g'arb,  Finish: janub")

if yonalish == 'g':
    if kamandak1 == 1 and kamandak2 == 0:
        print("Start: g'arb,  Finish: g'arb")
    elif kamandak1 == 1 and kamandak2 == 1:
        print("Start: g'arb,  Finish: sharq")
    elif kamandak1 == 1 and kamandak2 == 2:
        print("Start: g'arb,  Finish: shimol")

if yonalish == 'g':
    if kamandak1 == 2 and kamandak2 == 0:
        print("Start: g'arb,  Finish: janub")
    elif kamandak1 == 2 and kamandak2 == 1:
        print("Start: g'arb,  Finish: shimol")
    elif kamandak1 == 2 and kamandak2 == 2:
        print("Start: g'arb,  Finish: g'arb")



# 12) Doiraning elementlari quydagi tartibda nomerlangan. 1-radius r, 2-diametr
#     d = 2*r, 3-uzunligi l = 2*п*r, 4-yuzi s = п*(r**2). Shu elementlardan
#     bittasi berilganda qolganlarini topuvchi programma tuzilsin  п = 3.14

son = float(input("son = "))
element = float(input("1-radius"   '\n'
                      "2-diametr"  '\n'
                      "3-uzunligi" '\n'
                      "4-yuzi"     '\n'
                      "tanlang - "))

п = 3.14

if element == 1:
    r = son
    d = 2*r
    l = 2*п*r
    s = п*(r**2)

elif element == 2:
    d = son
    r = d/2
    l = п*d
    s = п*(d**2)/4

elif element == 3:
    l = son
    r = l/(2*п)
    d = 2*r
    s = п*(r**2)

elif element == 4:
    s = son
    r = (s/п)**(0.5)
    d = 2*r
    l = 2*п*r

print("R =",r,"\nd =",d,"\nl =",l,"\ns =",s)



# 13) Teng yonli to'g'ri burchakli uchburchakning elementlari quydagi tartibda 
#     nomerlangan. 1-katet a, 2-gipotenuza c = a *(2**0.5), 3-gipotenuzaga 
#     tushirilgan balandlik h = c/2, 4-yuzasi s = a*a/2. Shu elementlardan 
#     bittasi berilganda qolganlarini topuvchi programma tuzilsin.

son = float(input("son = "))
element = float(input("1-katet"      '\n'
                      "2-gipotenuza" '\n'
                      "3-balandlik"  '\n'
                      "4-yuzi"       '\n'
                      "tanlang - "))

if element == 1:
    a = son
    c = a *(2**0.5)
    h = c/2
    s = a*a/2

elif element == 2:
    c = son
    a = c/(2**0.5)
    h = c/2
    s = a*a/2
    
elif element == 3:
    h = son
    c = h*2
    a = c/(2**0.5)
    s = a*a/2
    
elif element == 4:
    s = son
    a = (s*2) ** 0.5
    c = a *(2**0.5)
    h = c/2

print("a =",a,"\nc =",c,"\nh =",h,"\ns =",s)




# 14) Teng tomonli uchburchakning elementlari quydagi tartibda nomerlangan.
#     1-tomoni a, 2-ichki chizilgan aylananing radiusi r = a*(3**0.5)/6, 3-tashqi
#     chizilgan aylananing radiusi R = r*2, 4-yuzasi s = (a**2)*(3**0.5)/4. Shu
#     elementlardan bittasi berilganda qolganlarini topuvchi programma tuzilsin.

son = float(input("son = "))
element = float(input("1-tomon"         '\n'
                      "2-ichki radius"  '\n'
                      "3-tashqi radius" '\n'
                      "4-yuzi"          '\n'
                      "tanlang - "))

if element == 1:
    a = son
    r = a*(3**0.5)/6
    R = r*2
    s = (a**2)*(3**0.5)/4

elif element == 2:
    r = son
    a = r*6/(3**0.5)
    R = r*2
    s = (a**2)*(3**0.5)/4
    
elif element == 3:
    R = son
    r = R/2
    a = r*6/(3**0.5)
    s = (a**2)*(3**0.5)/4
    
elif element == 4:
    s = son
    a = (s*4/(3**0.5))**0.5
    r = a*(3**0.5)/6
    R = r*2
   
print("a =",a,"\nr =",r,"\nR =",R,"\ns =",s)




# 15) O'yin kartasi turlari berilgan 1-g'isht, 2-olma, 3-chillak, 4-qarg'a.
#     10 lik kartadan katta kartalar quydagi qiymatlarni o'zlashtirsin: 11-valet,
#     12-dama, 13-qirol, 14-tuz. Ikkita butun son berilgan. n-karta qiymati
#     (6<=n<=14), m-karta turi (1<=m<=4) kiritilganda karta nomlari (masalan:
#     "olti qarg'a") chiqarib beruvchi programma tuzilsin.

son = int(input("Son kiriting (6-14) - "))
turi = int(input("1-g'isht"   '\n'
                 "2-olma"     '\n'
                 "3-chillak"  '\n'
                 "4-qarg'a"   '\n'
                 "tanlang - "))

if son == 10:
    a = "o'n"
elif son == 11:
    a = 'valet'
elif son == 12:
    a = 'dama'
elif son == 13:
    a = 'qirol'
elif son == 14:
    a = 'tuz'
elif son == 6:
    a = 'olti'
elif son == 7:
    a = 'yetti'
elif son == 8:
    a = 'sakkiz'
elif son == 9:
    a = "to'qqiz"
else:
    a = 10


if turi == 1:
    b = "g'isht"
elif turi == 2:
    b = "olma"
elif turi == 3:
    b = "chillak"
elif turi == 4:
    b = "qarg'a"
else:
    b = 10
    

if a == 10 or b == 10:
    print('xatolik yuz berdi')
else:
    print(a,b)




# 16) Yoshni yillarda aniqlovchi 20-69 gacha butun son berilgan. Son kiritilganda
#     unga mos so'zlarda ifodalovchi programma tuzilsin. (M: 24 = yigirma to'rt)

yosh = int(input("(20-69) - "))

butun = yosh // 10
qoldiq = yosh % 10

if butun == 2:
    a = 'yigirma'
elif butun == 3:
    a = "o'ttiz"
elif butun == 4:
    a = 'qirq'
elif butun == 5:
    a = 'ellik'
elif butun == 6:
    a = 'oltmish'
else:
    a = 10

if qoldiq == 1:
    b = 'bir'
elif qoldiq == 2:
    b = 'ikki'
elif qoldiq == 3:
    b = 'uch'
elif qoldiq == 4:
    b = "to'rt"
elif qoldiq == 5:
    b = 'besh'
elif qoldiq == 6:
    b = 'olti'
elif qoldiq == 7:
    b = 'yetti'
elif qoldiq == 8:
    b = 'sakkiz'
elif qoldiq == 9:
    b = "to'qqiz"
elif qoldiq == 0:
    b = 11
else:
    b = 10

if a == 10 or b == 10:
    print('xatolik yuz berdi')
elif b == 11:
    print(a)
else:
    print(a,b)




# 17) O'quv masalalarini aniqlovchi 10-40 gacha butun son berilgan. Son kiritilganda
#     unga mos so'zlarda ifodalovchi programmatuzilsin. (M: 10-o'nta masala)

masala = int(input("(10-40) - "))

butun = masala // 10
qoldiq = masala % 10

if butun == 1:
    a = "o'n"
elif butun == 2:
    a = 'yigirma'
elif butun == 3:
    a = "o'ttiz"
elif butun == 4:
    a = 'qirq'
else:
    a = 10


if qoldiq == 1:
    b = 'bir'
elif qoldiq == 2:
    b = 'ikki'
elif qoldiq == 3:
    b = 'uch'
elif qoldiq == 4:
    b = "to'rt"
elif qoldiq == 5:
    b = 'besh'
elif qoldiq == 6:
    b = 'olti'
elif qoldiq == 7:
    b = 'yetti'
elif qoldiq == 8:
    b = 'sakkiz'
elif qoldiq == 9:
    b = "to'qqiz"
elif qoldiq == 0:
    b = 11
else:
    b = 10


if a == 10 or b == 10 or (butun == 4 and qoldiq > 0):
    print('xatolik yuz berdi')
elif b == 11:
    print(a+"ta masala")
else:
    print(a,b+"ta masala")




# 18) 100-999 gacha oraliqdagi sonlarni so'zlarda ifodalovchi programma
#     tuzilsin. (M: 177-bir yuz yetmish yetti) 

son = int(input("(100-999) - "))

yuz = son // 100
on = son // 10 % 10
bir = son % 10

if 100 <= son < 1000:
    if yuz == 1:
        a = 'bir yuz'
    elif yuz == 2:
        a = 'ikki yuz'
    elif yuz == 3:
        a = 'uch yuz'
    elif yuz == 4:
        a = "to'rt yuz"
    elif yuz == 5:
        a = 'besh yuz'
    elif yuz == 6:
        a = 'olti yuz'
    elif yuz == 7:
        a = 'yetti yuz'
    elif yuz == 8:
        a = 'sakkiz yuz'
    elif yuz == 9:
        a = "to'qqiz yuz"
    

    if on == 1:
        b = "o'n"
    elif on == 2:
        b = 'yigirma'
    elif on == 3:
        b = "o'ttiz"
    elif on == 4:
        b = "qirq"
    elif on == 5:
        b = 'ellik'
    elif on == 6:
        b = 'oltmish'
    elif on == 7:
        b = 'yetmish'
    elif on == 8:
        b = 'sakson'
    elif on == 9:
        b = "to'qson"
    elif on == 0:
        b = 11


    if bir == 1:
        c = 'bir'
    elif bir == 2:
        c = 'ikki'
    elif bir == 3:
        c = 'uch'
    elif bir == 4:
        c = "to'rt"
    elif bir == 5:
        c = 'besh'
    elif bir == 6:
        c = 'olti'
    elif bir == 7:
        c = 'yetti'
    elif bir == 8:
        c = 'sakkiz'
    elif bir == 9:
        c = "to'qqiz"
    elif bir == 0:
        c = 11


    if yuz == 1 and on == 0 and bir == 0:
        print("yuz")
    elif on == 0 and bir == 0:
        print(a)
    elif on == 0:
        print(a,c)
    elif bir == 0:
        print(a,b)
    else:
        print(a,b,c)

else:
    print('xatolik yuz berdi')



# 19) Sharq kalendarida 60 yillik davr qabul qilingan. Yil muchali 5 ta rang
#     (yashil, qizil, sariq, oq va qora) va 12 ta hayvon (sichqon, sigir, yo'lbars,
#     quyon, ajdar, ilon, ot, qo'y, maymun, tovuq, it va to'ng'islardan) nomlaring
#     kombinatsiyadan kelib chiqadi. Yilning raqamiga qarab uning muchalini
#     aniqlovchi programma tuzilsin. 1984-davr boshi: "yashil sichqon yili"

yil = int(input("Yil = "))
rang = yil % 5
hayvon = yil % 12

if rang == 1:
    color = 'sariq'
elif rang == 2:
    color = 'oq'
elif rang == 3:
    color = 'qora'
elif rang == 4:
    color = 'yashil'
elif rang == 0:
    color = 'qizil'

if hayvon == 1:
    animals = 'tovuq'
elif hayvon == 2:
    animals = 'it'
elif hayvon == 3:
    animals = "to'ng'iz"
elif hayvon == 4:
    animals = 'sichqon'
elif hayvon == 5:
    animals = 'sigir'
elif hayvon == 6:
    animals = "yo'lbars"
elif hayvon == 7:
    animals = 'quyon'
elif hayvon == 8:
    animals = 'ajdar'
elif hayvon == 9:
    animals = 'ilon'
elif hayvon == 10:
    animals = 'ot'
elif hayvon == 11:
    animals = "qo'y"
elif hayvon == 0:
    animals = 'maymun'

print(color,animals,"yili")

"""


# 20) Ikkita burj vaqtlarini aniqlovchi butun son berilgan: d (kun), m (oy).
#     Berilgan sana qaysi burjga kirishini aniqlovchi programma tuzilsin.
#     "Qovg'a (20.1-18.2)", "Baliq (19.2-20.3)", "Qo'y (21.3-19.4)", "Buzoq
#     (20.4-20.5)", "Egizaklar (21.5-21.6)", "Qisqichbaqa (22.6-22.7)", "Arslon
#     (23.7-22.8)", "Parizod (23.8-22.9)", "Tarozi (23.9-22.10)", "Chayon 
#     (23.10-22.11)", "O'qotar (23.11-21.12)", "Echki (22.12-19.1)".

d = int(input("Kun = "))
m = int(input("Oy = "))

if ( m == 12 and 22 <= d <= 31 ) or ( m == 1 and 1 <= d <= 19 ):
    hayvon = "Echki"
elif ( m == 1 and 20 <= d <= 31 ) or ( m == 2 and 1 <= d <= 18 ):
    hayvon = "Qovg'a"
elif ( m == 2 and 19 <= d <= 29 ) or ( m == 3 and 1 <= d <= 20 ):
    hayvon = "Baliq"
elif ( m == 3 and 21 <= d <= 31 ) or ( m == 4 and 1 <= d <= 19 ):
    hayvon = "Qo'y"
elif ( m == 4 and 20 <= d <= 30 ) or ( m == 5 and 1 <= d <= 20 ):
    hayvon = "Buzoq"
elif ( m == 5 and 21 <= d <= 31 ) or ( m == 6 and 1 <= d <= 21 ):
    hayvon = "Egizaklar"
elif ( m == 6 and 22 <= d <= 30 ) or ( m == 7 and 1 <= d <= 22 ):
    hayvon = "Qisqichbaqa"
elif ( m == 7 and 23 <= d <= 31 ) or ( m == 8 and 1 <= d <= 22 ):
    hayvon = "Arslon"
elif ( m == 8 and 23 <= d <= 31 ) or ( m == 9 and 1 <= d <= 22 ):
    hayvon = "Parizod"
elif ( m == 9 and 23 <= d <= 30 ) or ( m == 10 and 1 <= d <= 22 ):
    hayvon = "Tarozi"
elif ( m == 10 and 23 <= d <= 31 ) or ( m == 11 and 1 <= d <= 22 ):
    hayvon = "Chayon"
elif ( m == 11 and 23 <= d <= 30 ) or ( m == 12 and 1 <= d <= 21 ):
    hayvon = "O'qotar"
else:
    hayvon = 'Kun yoki oy xato'

print(hayvon)


"""
kun = int(input("kun = "))
oy = int(input("oy = "))
yil = int(input("yil = "))

if yil % 400 == 0:
    kabisa = 1
elif yil % 100 == 0:
    kabisa = 0
elif yil % 4 == 0:
    kabisa = 1
else:
    kabisa = 0

if kabisa == 1 and oy == 3 and kun == 1:
    print(29,oy-1,yil)
elif kabisa == 0 and oy == 3 and kun == 1:
    print(28,oy-1,yil)

elif kun == 1 and (oy == 2 or oy == 4 or oy == 6 or  oy == 8 or oy == 9 or oy == 11):
    print(31,oy-1,yil)
elif kun == 1 and ( oy == 5 or oy == 7 or oy == 8 or oy == 10 or oy == 12):
    print(30,oy-1,yil)
elif kun == 1 and oy == 1:
    print(31,12,yil-1)

elif kun == 1 and oy == 3:
    print(28,oy-1,yil)
else:
    print(kun-1,oy,yil)






a = int(input("Bo'linuvchini kiriting:  a = "))
b = int(input("Bo'luvchini kiriting:  b = "))

s=0
butun=0
while s <= a:
    s += b
    butun += 1

qol = s - b
qoldiq = a - qol


royxat = []
w = 10
while True:
    if qoldiq != 0 and w != 0:
       
        on=10
        summa = 0

        while on != 0:
            on -= 1
            summa += qoldiq

        yigindi = 0
        butu = 0

        while yigindi <= summa:
            yigindi += b
            butu += 1
        qol = butu - 1
        d = yigindi - b
        qoldiq = summa - d
        royxat.append(qol)
        w -= 1
    else:
        break


print(butun-1,end=".")

for son in royxat:
    print(son,end="")






# 18) 1-999 mln gacha oraliqdagi sonlarni so'zlarda ifodalovchi programma
#     tuzilsin. (M: 177-bir yuz yetmish yetti) 

son = int(input("(100 - 999 000 000) - "))

yuz_million = son // 100000000
on_million = son // 10000000 % 10
million = son // 1000000 % 10
yuz_ming = son // 100000 % 10
on_ming = son // 10000 % 10
ming = son // 1000 % 10
yuz = son // 100 % 10
on = son // 10 % 10
bir = son % 10


if 1 <= son < 1000000000:
    
    if bir == 1:
        a = 'bir'
    elif bir == 2:
        a = 'ikki'
    elif bir == 3:
        a = 'uch'
    elif bir == 4:
        a = "to'rt"
    elif bir == 5:
        a = 'besh'
    elif bir == 6:
        a = 'olti'
    elif bir == 7:
        a = 'yetti'
    elif bir == 8:
        a = 'sakkiz'
    elif bir == 9:
        a = "to'qqiz"
    elif bir == 0:
        a = 11


    if on == 1:
        b = "o'n"
    elif on == 2:
        b = 'yigirma'
    elif on == 3:
        b = "o'ttiz"
    elif on == 4:
        b = "qirq"
    elif on == 5:
        b = 'ellik'
    elif on == 6:
        b = 'oltmish'
    elif yuz == 7:
        b = 'yetmish'
    elif on == 8:
        b = 'sakson'
    elif on == 9:
        b = "to'qson"
    elif on == 0:
        b = 11
        
        
    if yuz == 1:
        c = 'bir yuz'
    elif yuz == 2:
        c = 'ikki yuz'
    elif yuz == 3:
        c = 'uch yuz'
    elif yuz == 4:
        c = "to'rt yuz"
    elif yuz == 5:
        c = 'besh yuz'
    elif yuz == 6:
        c = 'olti yuz'
    elif yuz == 7:
        c = 'yetti yuz'
    elif yuz == 8:
        c = 'sakkiz yuz'
    elif yuz == 9:
        c = "to'qqiz yuz"
    
    
    if ming == 1:
        d = 'bir ming'
    elif ming == 2:
        d = 'ikki ming'
    elif ming == 3:
        d = 'uch ming'
    elif ming == 4:
        d = "to'rt ming"
    elif ming == 5:
        d = 'besh ming'
    elif ming == 6:
        d = 'olti ming'
    elif ming == 7:
        d = 'yetti ming'
    elif ming == 8:
        d = 'sakkiz ming'
    elif ming == 9:
        d = "to'qqiz ming"
    
    
    if on_ming == 1:
        e = "o'n ming"
    elif on_ming == 2:
        e = "yigirma ming"
    elif on_ming == 3:
        e = "o'ttiz ming"
    elif on_ming == 4:
        e = "qirq ming"
    elif on_ming == 5:
        e = "ellik ming"
    elif on_ming == 6:
        e = "oltmish ming"
    elif on_ming == 7:
        e = "yetmish ming"
    elif on_ming == 8:
        e = "sakson ming"
    elif on_ming == 9:
        e = "to'qson ming"
    
    
    if yuz_ming == 1:
        f = 'bir yuz ming'
    elif yuz_ming == 2:
        f = 'ikki yuz ming'
    elif yuz_ming == 3:
        f = 'uch yuz ming'
    elif yuz_ming == 4:
        f = "to'rt yuz ming"
    elif yuz_ming == 5:
        f = 'besh yuz ming'
    elif yuz_ming == 6:
        f = 'olti yuz ming'
    elif yuz_ming == 7:
        f = 'yetti yuz ming'
    elif yuz_ming == 8:
        f = 'sakkiz yuz ming'
    elif yuz_ming == 9:
        f = "to'qqiz yuz ming"
    
    
    if million == 1:
        g = 'bir million'
    elif million == 2:
        g = 'ikki million'
    elif million == 3:
        g = 'uch million'
    elif million == 4:
        g = "to'rt million"
    elif million == 5:
        g = 'besh million'
    elif million == 6:
        g = 'olti million'
    elif million == 7:
        g = 'yetti million'
    elif million == 8:
        g = 'sakkiz million'
    elif million == 9:
        g = "to'qqiz million"
    
    
    if on_million == 1:
        h = "o'n million"
    elif on_million == 2:
        h = 'yigirma million'
    elif on_million == 3:
        h = "o'ttiz million"
    elif on_million == 4:
        h = "qirq million"
    elif on_million == 5:
        h = 'ellik million'
    elif on_million == 6:
        h = 'oltmish million'
    elif on_million == 7:
        h = 'yetmish million'
    elif on_million == 8:
        h = 'sakson million'
    elif on_million == 9:
        h = "to'qson million"
    
    
    if yuz_million == 1:
        j = 'bir yuz million'
    elif yuz_million == 2:
        j = 'ikki yuz million'
    elif yuz_million == 3:
        j = 'uch yuz million'
    elif yuz_million == 4:
        j = "to'rt yuz million"
    elif yuz_million == 5:
        j = 'besh yuz million'
    elif yuz_million == 6:
        j = 'olti yuz million'
    elif yuz_million == 7:
        j = 'yetti yuz million'
    elif yuz_million == 8:
        j = 'sakkiz yuz million'
    elif yuz_million == 9:
        j = "to'qqiz yuz million"
    
# a b c d e f g h j

    if on_million == 0 and million == 0 and yuz_ming==0 and on_ming==0 and ming==0 and yuz==0 and on == 0 and bir == 0:
        print(j)
    elif on == 0 and bir == 0:
        print(a)
    elif on == 0:
        print(a,c)
    elif bir == 0:
        print(a,b)
    else:
        print(j,h,g,f,e,d,c,b,a)

else:
    print('xatolik yuz berdi')
    
    
    
    
kun = int(input("kun = "))
oy = int(input("oy = "))
yil = int(input("yil = "))

if yil % 400 == 0:
    kabisa = 1
elif yil % 100 == 0:
    kabisa = 0
elif yil % 4 == 0:
    kabisa = 1
else:
    kabisa = 0


if kabisa == 1 and kun == 28 and oy == 2:
    print(1,oy+1,yil)
elif kabisa == 1 and kun == 29 and oy == 2:
    print(2,oy+1,yil)
elif kabisa == 0 and kun == 28 and oy == 2:
    print(2,oy+1,yil)
elif kabisa == 0 and kun >= 27 and oy == 2:
    print("Xatolik yuz berdi!!!")
    
elif kun == 31 and (oy == 1 or oy == 3 or oy == 5 or oy == 7 or oy == 8 or oy == 10):
    print(2,oy+1,yil)
elif kun == 30 and (oy == 1 or oy == 3 or oy == 5 or oy == 7 or oy == 8 or oy == 10):
    print(1,oy+1,yil)

elif kun == 30 and (oy == 4 or oy == 6 or oy == 9 or oy == 11):
    print(2,oy+1,yil)
elif kun == 29 and (oy == 4 or oy == 6 or oy == 9 or oy == 11):
    print(1,oy+1,yil)

elif kun == 31 and oy == 12:
    print(2,1,yil+1)

elif 1 <= kun <= 29 and 1 <= oy <= 12:
    print(kun+2,oy,yil)
else:
    print("Xatolik yuz berdi!!!")









a = int(input("Bo'linuvchini kiriting:  a = "))
b = int(input("Bo'luvchini kiriting:  b = "))

s=0
butun=0
while s <= a:
    s += b
    butun += 1

qol = s - b
qoldiq = a - qol


print(butun-1,end=".")
w = 10
while True:
    if qoldiq != 0 and w != 0:
       
        on=10
        summa = 0

        while on != 0:
            on -= 1
            summa += qoldiq

        yigindi = 0
        butu = 0

        while yigindi <= summa:
            yigindi += b
            butu += 1
        qol = butu - 1
        d = yigindi - b
        qoldiq = summa - d
        print(qol,end="")
        w -= 1
    else:
        break











a = int(input("Bo'linuvchini kiriting:  a = "))
b = int(input("Bo'luvchini kiriting:  b = "))

s=0
butun=0
while s <= a:
    s += b
    butun += 1

qol = s - b
qoldiq = a - qol



w = 10
while True:
    if qoldiq != 0 and w != 0:
       
        on=10
        summa = 0

        while on != 0:
            on -= 1
            summa += qoldiq

        yigindi = 0
        butu = 0

        while yigindi <= summa:
            yigindi += b
            butu += 1
        qol = butu - 1
        d = yigindi - b
        qoldiq = summa - d
        if w == 10:
            print(butun-1,end=".")
            print(qol,end="")
        else:
            print(qol,end="")
        w -= 1
    else:
        break


"""
