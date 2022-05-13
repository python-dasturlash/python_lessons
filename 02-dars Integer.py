
# 1) Uzunlik L sm da berilgan. Undagi to'liq metrlar sonini aniqlovchi
#    programma tuzilsin.  ( 1m = 100sm )

sm = int(input("Necha sm kiritmoqchisiz - "))
metr = sm // 100
santimetr = sm % 100
print(metr,"metr",santimetr,"santimetr")



# 2) Og'irlik m kg da berilgan. Undagi to'liq tonnalar sonini aniqlovchi
#    programma tuzilsin.  ( 1t = 1000kg )

kg = int(input("kg = "))
t = kg // 1000
kilo = kg % 1000
print(t,"tonna",kilo,"kilogramm")



# 3) Faylning hajmi baytlarda berilgan bo'lib, butunni olish operatsiyasidan
#    foydalanib fayl hajmining  to'liq kilobaytlarda ifodalovchi 
#    programma tuzilsin.   ( 1kb = 1024bayt )

bayt = int(input("Bayt = "))
kb = bayt // 1024
b = bayt % 1024
print(kb,"kilobayt",b,"bayt")



# 4) A va B (A>B) musbat sonlari berilgan. A kesmada B kesmani necha marta
#    joylashtirish mumkinligini aniqlovchi programma tuzilsin.

A = int(input("A = "))
B = int(input("B = "))
AB = A // B
print(AB,"marta")



# 5) A va B (A>B) musbat sonlar berilgan. A kesmada B kesmani necha marta
#    joylashtirish mumkin. A kesmada B kesmaning joylashmagan qismini
#    aniqlovchi programma tuzilsin.

A = int(input("A = "))
B = int(input("B = "))
AB = A // B
BA = A % B
print(AB,"marta joylashtirish mumkin. Joylashmagan qismi",BA)



# 6) Ikki honali son berilgan. oldin uning o'nliklar honasidagi raqamni,
#    so'ng birlar honasidagi raqamni chiqaruvchi programma tuzilsin.

son = int(input("Ikki honali son kiriting - "))
on = son // 10
bir = son % 10
print("O'nlar honasidagi son -",on,"\nBirlar honasidagi son -",bir)



# 7) Ikki honali son berilgan. Uning raqamlari yig'indisini aniqlang.

son = int(input("Ikki honali son kiriting - "))
bir = son // 10
ikki = son % 10
yigindi = bir + ikki
print(bir,"+",ikki,"=",yigindi)



# 8) Ikki honali son berilgan. Uning raqamlari o'rnini almashtirishdan 
#    hosil bo'lgan sonni aniqlovchi programma tuzilsin.

son = int(input("Ikki honali son kiriting - "))
bir = son // 10
ikki = son % 10
almashtirish = ikki*10 + bir
print(almashtirish)



# 9) Uch honali son berilgan. Uning yuzlar honasidagi raqamini aniqlang.

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
print(yuz)



# 10) Uch honali son berilgan. Oldin uni birliklar honasidagi raqamni so'ng
#     o'nliklar honasidagi raqamni chiqaruvchi programma tuzilsin.

son = int(input("Uch honali son kiriting - "))
bir = son % 10
on = son // 10 % 10
print("Birlar honasidagi son -",bir,"\nO'nlar honasidagi son -",on)



# 11) Uch honali son berilgan. Uning raqamlar yig'indisini aniqlang.

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
on = son // 10 % 10
bir = son % 10
yigindi = yuz + on + bir
print(yuz,"+",on,"+",bir,"=",yigindi)



# 12) Uch honali son berilgan. Uning raqamlarini teskari tartibda yozishdan
#     hosil bo'lgan sonni aniqlovchi programma tuzilsin.

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
on = son // 10 % 10
bir = son % 10
teskari = bir*100 + on*10 + yuz
print(teskari)



# 13) Uch honali son berilgan. Uning chapdan birinchi raqamini o'chirib o'ng
#     tarafiga yozishdan hosil bo'lgan sonni aniqlovchi programma tuzilsin.

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
on = son % 100
yoz = on*10 + yuz
print(yoz)



# 14) Uch honali son berilgan. Uning ongdan birinchi raqamini o'chirib chap
#     tarafiga yozishdan hosil bo'lgan sonni aniqlovchi programma tuzilsin.

son = int(input("Uch honali son kiriting - "))
bir = son % 10
on = son // 10
yoz = bir*100 + on
print(yoz)



# 15) Uch honali son berilgan. Uning o'nliklar honasidagi raqam bilan yuzliklar
#     xonasidagi raqamni almashtirishdan hosil bo'lgan sonni aniqlovchi
#     programma tuzilsin.  ( 524 -- 254 )

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
on = son // 10 % 10
bir = son % 10
almashtirish = on*100 + yuz*10 + bir
print(almashtirish)



# 16) Uch honali son berilgan. Uning o'nliklar honasidagi raqam bilan birliklar
#     xonasidagi raqamni almashtirishdan hosil bo'lgan sonni aniqlovchi
#     programma tuzilsin.  ( 524 -- 254 )

son = int(input("Uch honali son kiriting - "))
yuz = son // 100
on = son // 10 % 10
bir = son % 10
almashtirish =  yuz*100 + bir*10 + on
print(almashtirish)



# 17) 999 dan katta bo'lgan son berilgan. Bir marta bo'lib butunni va bo'lib
#     qoldiqni olish operatsiyasidan foydalanib berilgan sonni yuzliklar
#     honasidagi sonni aniqlovchi programma tuzilsin.

son = int(input("999 dan katta son kiriting - "))
yuz = son % 1000
a = yuz // 100
print(a)



# 18) 999 dan katta bo'lgan son berilgan. Bir marta bo'lib butunni va bo'lib
#     qoldiqni olish operatsiyasidan foydalanib berilgan sonni mingliklar
#     honasidagi sonni aniqlovchi programma tuzilsin.

son = int(input("999 dan katta son kiriting - "))
ming = son % 10000
a = ming // 1000
print(a)



# 19) Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha
#     minut to'la o'tganligini aniqlovchi programma tuzilsin.

sekund = int(input("Sekundni kiriting - "))
minut = sekund // 60
print(minut,"minut")



# 20) Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha
#     to'la soat o'tganligini aniqlovchi programma tuzilsin.

sekund = int(input("Sekundni kiriting - "))
soat = sekund // 3600
print(soat,"soat")



# 21) Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha
#     minut va sekund o'tganligini aniqlovchi programma tuzilsin.

sekund = int(input("Sekundni kiriting - "))
minut = sekund // 60
qoldiq = sekund - minut*60
print(minut,"minut",qoldiq,"sekund")



# 22) Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha
#     soat va sekund o'tganligini aniqlovchi programma tuzilsin.

sekund = int(input("Sekundni kiriting - "))
soat = sekund // 3600
qoldiq = sekund - soat*3600
print(soat,"soat",qoldiq,"sekund")



# 23) Kun boshidan boshlab N sekund vaqt o'tti. Kun boshidan boshlab qancha
#     soat, minut va sekund o'tganligini aniqlovchi programma tuzilsin.

sekund = int(input("Sekundni kiriting - "))
soat = sekund // 3600
minut = (sekund - soat*3600) // 60
qoldiq = sekund - soat*3600 - minut*60
print(soat,"soat",minut,"minut",qoldiq,"sekund")



# 24) # Hafta kunlari quydagi tartibda berilgan. 0-yakshanba, 1-dushanba,
#     2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba. 1-365 oraliqda
#     yotuvchi k soni berilgan. Agar 1-yanvar dushanba bo'lsa, kiritilgan
#     k-kun haftaning qaysi kuniga to'g'ri kelishini aniqlang.

k = int(input("k ni kiriting (1-365)   k = "))
kun = k % 7
yakshanba = 0
dushanba = 1
seshanba = 2
chorshanba = 3
payshanba = 4
juma = 5
shanba = 6
print(kun)



# 25) # Hafta kunlari quydagi tartibda berilgan. 0-yakshanba, 1-dushanba,
#     2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba. 1-365 oraliqda
#     yotuvchi k soni berilgan. Agar 1-yanvar payshanba bo'lsa, kiritilgan
#     k-kun haftaning qaysi kuniga to'g'ri kelishini aniqlang.

k = int(input("k ni kiriting (1-365)   k = "))
kun = k % 7
kuni = (kun + 3) % 7
print(kuni)



# 26) # Hafta kunlari quydagi tartibda berilgan. 1-dushanba, 2-seshanba, 
#     3-chorshanba, 4-payshanba, 5-juma, 6-shanba, 7-yakshanba, . 1-365 oraliqda
#     yotuvchi k soni berilgan. Agar 1-yanvar seshanba bo'lsa, kiritilgan
#     k-kun haftaning qaysi kuniga to'g'ri kelishini aniqlang.

k = int(input("k ni kiriting (1-365)   k = "))
kun = k % 7
kuni = kun + 1
print(kuni)



# 27) # Hafta kunlari quydagi tartibda berilgan. 1-dushanba, 2-seshanba, 
#     3-chorshanba, 4-payshanba, 5-juma, 6-shanba, 7-yakshanba, . 1-365 oraliqda
#     yotuvchi k soni berilgan. Agar 1-yanvar yakshanba bo'lsa, kiritilgan
#     k-kun haftaning qaysi kuniga to'g'ri kelishini aniqlang.

k = int(input("k ni kiriting (1-365)   k = "))
kun = k % 7
kuni = (kun + 6) % 7
print(kuni)



# 28) Hafta kunlari quydagi tartibda berilgan. 1-dushanba, 2-seshanba, 
#     3-chorshanba, 4-payshanba, 5-juma, 6-shanba, 7-yakshanba(n 1-7 gacha bo'lgan
#     hafta kunlari soni). 1-365 oraliqda yotuvchi k soni berilgan. Agar 1-yanvar
#     n-kunga to'g'ri kelsa, kiritilgan k-kun haftaning qaysi kuniga to'g'ri
#     kelishini aniqlang.

k = int(input("k ni kiriting (1-365)   k = "))
n = int(input("n ni kiriting (1-7)     n = "))
kun = k % 7
kuni = (kun + n - 1) % 7 
print(kuni)



# 29) A,B,C butun sonlar berilgan. Tomonlari A va B bo'lgan to'g'ri to'rtburchakka
#     tomoni C bo'lgan kvadrat eng ko'p joylashtirilsin. To'g'ri to'rtburchakka
#     eng ko'p joylashgan kvadratlar soni va joylashmay qolgan qismi yuzasini
#     aniqlovchi programma tuzilsin.

print("A, B va C larni kiriting")
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
joylashgan = (A // C) * (B // C)
joylashmagan = A * B - joylashgan * C * C
print(joylashgan,"ta kvadrat to'g'ri to'rtburchak ichiga joylashgan.")
print(joylashmagan,"- to'g'ri to'rtburchakka joylashmagan qismining yuzi")



# 30) Qaysidir yil berilgan. Berilgan yilning qaysi yuz yillikka kirishini
#     aniqlovchi programma tuzilsin.

yil = int(input("Yilni kiriting - "))
asr = yil // 100 + 1
print(asr,"- asr") 



