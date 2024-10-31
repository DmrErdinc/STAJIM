                                                                        #STRİNG İFADELERİ 
Soyadı = "Demir"
print(Soyadı[0])
Soyadı = "Demir"
print(Soyadı[-1])

ornek_a = "kasaba"
print(ornek_a)

ornek_a = "yeni değer"
print(ornek_a)

a = "Merhaba"
b = "Dünya!"
c = a + " " + b
print(c)

yas = 24
metin = "Benim adım Erdinc, ve ben {} yaşındayım!"
print(metin.format(yas))

                                                                         #input(), format()


sayi1 = input("Birinci sayıyı girin :")
sayi2 = input("İkinci sayıyı girin :")

topla = sayi1+sayi2

print("Toplam :",topla)
isim = input("İsminiz :")
yas = input("Yaşınız :")

print("Merhaba {} bey yaşınız {} hala çok gençsiniz".format(isim,yas))

                                                                            ##if-else-elif 

vize1 = float(input('vize 1: '))
vize2 = float(input('vize 2: '))
final = float(input('final : '))

ortalama = ((vize1+vize2)/2)*0.6 + (final * 0.4)

result = (ortalama>=50) and (final>=50)
result = (ortalama >=50) or (final>=70)

##durum-1

if (ortalama>=50):
     if (final>=50):
          print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
     else:
          print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız. Finalden en az 50 almalısınız.')
else:
     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')

##durum-2

if (ortalama >=50):
    print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı')
else:
    if (final>=70):
        print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarılı. Finalden en az 70 aldığınız için geçtiniz.')
    else:
     print(f'öğrencinin ortalaması: {ortalama} ve geçme durumu: başarısız')