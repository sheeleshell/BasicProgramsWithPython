import random

sayi = random.randint(1, 100) 
can=int(input('kaç can kullanmak istersiniz?: '))
hak = can
sayac = 0

while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac} defada  bildiniz.Toplam puanınız: {100-(100/can)*(sayac-1)}')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('asagi')

    if hak == 0:
        print(f'hakkiniz bitti.Tutulan sayi: {sayi}')
