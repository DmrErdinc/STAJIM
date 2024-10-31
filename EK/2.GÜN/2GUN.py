# 1'den 10'a kadar olan sayılar arasında 5'i atlayarak yazdırma.
for i in range(1, 11):
    if i == 5:
        continue  # 5'i atla
    print(i)

# 1'den 10'a kadar olan sayılar arasında 5'e ulaştığında döngüyü durdurma.
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break  # 5'e ulaşınca döngüyü sonlandır.
    i += 1

# İlk çift sayıya ulaşınca döngüyü durdurma.
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} çift sayıdır. Döngü durduruluyor.")
        break
    print(i)   

# 1'den 10'a kadar olan sayılar arasında 3'ü atla ve devam et.
i = 1
while i <= 10:
    if i == 3:
        i += 1
        continue  # 3'ü atla
    print(i)
    i += 1    

# 1'den 10'a kadar olan sayılar arasında çift olanları atla, 7'de döngüyü durdur.
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Çift sayıları atla
    print(i)
    if i == 7:
        break  # 7'ye ulaştığında döngüyü durdur.    