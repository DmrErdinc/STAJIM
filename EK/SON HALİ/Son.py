import csv  # CSV dosyaları ile okuma/yazma işlemleri için kütüphane
import re  # Regüler ifadelerle string manipülasyonu için kütüphane
import urllib.parse  # URL'leri çözümlemek için kütüphane
from selenium import webdriver  # Selenium'un tarayıcı otomasyonu için ana sınıfı
from selenium.webdriver.chrome.service import Service as ChromeService  # ChromeDriver servisi için sınıf
from webdriver_manager.chrome import ChromeDriverManager  # ChromeDriver'ı otomatik güncelleme için kütüphane
from selenium.webdriver.common.by import By  # Elementleri bulmak için kullanılır
from selenium.webdriver.chrome.options import Options  # Chrome tarayıcı ayarları için sınıf
from selenium.webdriver.support import expected_conditions as EC  # Beklenen koşulları tanımlamak için sınıf
from selenium.webdriver.support.ui import WebDriverWait  # Belirli bir süre boyunca bekleme işlemi için sınıf
from selenium.common.exceptions import TimeoutException, NoSuchElementException  # Hata yönetimi için özel istisnalar
import time  # Zamanlama ve gecikme işlemleri için kütüphane
import random  # Rastgele sayı üretimi için kütüphane

# Brave tarayıcı ayarları
option = Options()
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave"

option.add_argument('--disable-notifications')  # Bildirimleri devre dışı bırak
option.binary_location = brave_path  # Brave tarayıcısının yolunu belirt

option.add_argument("--profile-directory=Default")  # Tarayıcı profilini kullan
option.add_argument('--ignore-ssl-errors')  # SSL hatalarını yoksay
option.add_argument("--disable-popup-blocking")  # Pop-up engellemeyi devre dışı bırak
option.add_argument("--disable-save-password-bubble")  # Şifre kaydetme balonunu devre dışı bırak
option.add_argument('--headless')  # Tarayıcıyı görünmez çalıştır (arka planda)

# ChromeDriver'ı başlatma
options = webdriver.ChromeOptions()

# ChromeDriver'ı güncelle ve başlat
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.maximize_window()  # Tarayıcı penceresini maksimum boyutta aç

# Kampüs Ulaşım Pusula web sitesine git
browser.get("https://kampp.in/kamp-alanlari")
print("Bekleniyorrrr")
time.sleep(random.randint(3, 10))  # Sayfanın yüklenmesi için rastgele bir süre bekle

def asagiGel():
    last_height = browser.execute_script("return document.body.scrollHeight")  # Sayfanın mevcut yüksekliğini al
    while True:
        # Sayfanın sonuna kadar kaydır
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Sayfanın yüklenmesi için bekleyin
        time.sleep(random.randint(3, 5))  # Rastgele bir süre bekle
        
        # Yeni yüksekliği kontrol edin
        new_height = browser.execute_script("return document.body.scrollHeight")
        
        # Yüksekliğin değişip değişmediğini kontrol edin (daha fazla içerik yoksa)
        if new_height == last_height:
            break  # Yeni yükseklik değişmediyse döngüden çık
        last_height = new_height  # Yeni yüksekliği güncelle

def linkCek():
    print(linkCek)  # linkCek fonksiyonunu çağırıyor
    dosya_adi = "./linklerr3.txt"  # Linkleri kaydetmek için dosya adı

    file = open(dosya_adi, 'a', encoding="utf-8")  # Dosyayı ekleme modunda aç

    alanlar = browser.find_elements(By.XPATH, "//div[contains(@class,'BszUz')]")  # İlgili alanları bul

    print(len(alanlar))  # Bulunan alanların sayısını yazdır

    # baslik, telefon, websitesi, hakkında, adres, konumLink
    for alan in alanlar:
        link = alan.get_attribute("href")  # Her alanın 'href' özelliğini al
        file.write(link + '\n')  # Linki dosyaya yaz

def isletmeOku(link):
    browser.get("https://kampp.in/" + link)  # Verilen linke git
    time.sleep(random.randint(3, 5))  # Sayfanın yüklenmesi için bekle

    # İl ve ilçe bilgilerini alma
    ililce = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[2]/div[1]/div/span[2]'))
    ).text  # Belirtilen XPATH ile il ve ilçe bilgisini al

    print(ililce)
    if ililce:
        ililce = ililce.split(" / ")  # "İl / İlçe" formatında ise ayır

        il = ililce[0]  
        ilce = ililce[1]

    # Başlık alma işlemi
    try:
        baslik = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[2]/div[1]/span'))
        ).text  # Başlık bilgisini al
        print(baslik)
    except TimeoutException:
        print("Başlık bulunamadı")  # Başlık bulunamazsa hata mesajı
        return
    except NoSuchElementException:
        print("Başlık bulunamadı, yok belirtilmemiş")  # Başlık elemanı yoksa hata mesajı
        return

    # Hakkında bilgisi alma
    hakkindatext = ''
    try:
        hakkında = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[3]/span'))
        ).text  # Hakkında bilgilerini al
        if hakkında:
            print(hakkında)
        else:
            print("Hakkında bilgisi yok")
    except TimeoutException:
        print("Hakkında bilgisi yok")  # Hakkında bilgisi alınamazsa hata mesajı
    except NoSuchElementException:
        print("Hakkında bilgisi yok, belirtilmemiş")  # Hakkında elemanı yoksa hata mesajı

    # Konum bilgisi alma
    try:
        Konum = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class,'slug__StyledMap-sc-1e6v0q9-5')]"))
        ).get_attribute('src')  # Konum bilgilerini içeren iframe kaynağını al
        if Konum:
            print(Konum)
            q_param = re.search(r'q=([^&]+)', Konum).group(1)  # Konum parametresini al
            konum = q_param.split(",")  # Enlem ve boylamı ayır

            lat = konum[0]  # Enlem
            lng = konum[1]  # Boylam
            print(q_param)
        else:
            print("Konum bilgisi yok")
    except TimeoutException:
        print("Konum bilgisi yok")  # Konum bilgisi alınamazsa hata mesajı

    # Verileri CSV dosyasına yazma
    veriler = [baslik, hakkında, il, ilce, Konum, lat, lng]  # Alınan verileri bir listeye koy
    with open('Dosya.csv', mode='a', newline='', encoding='utf-8') as file:  # CSV dosyasını ekleme modunda aç
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  # CSV yazıcı oluştur
        writer.writerow(veriler)  # Verileri dosyaya yaz

def tarama():
    with open('./linklerr3.txt') as file:
        lines = file.readlines()  # Dosyadaki tüm satırları oku
        line_count = len(lines)  # Satır sayısını al

    print(line_count)

    i = 1

    while i < line_count:
        # Dosyadan ilk satırı okuyoruz
        read = open('./linklerr3.txt', 'r', encoding="utf8") 
        ilksatir = read.readline()  # İlk satırı al
        data = read.read().splitlines(True)  # Kalan satırları oku
        read.close()

        # Dosyadan ilk satırı siliyoruz
        write = open('./linklerr3.txt', 'w', encoding="utf-8")
        write.writelines(data[0:])  # Kalan satırları dosyaya yaz
        write.close()

        # Silinen ilk satırı paylaşılan gönderiler dosyasına yazdırıyoruz
        writegonderi = open('./acilanlinklerr3.txt', 'a', encoding="utf-8")
        writegonderi.write(ilksatir)  # İlk satırı ayrı bir dosyaya yaz
        writegonderi.close()

        isletmeOku(ilksatir)  # İlk satırı oku ve işle
        i += 1  

# Menülerin elemanlarını bul
menuler = browser.find_elements(By.XPATH, "//div[contains(@class,'ListHeader__TabbarItem-sc-1phw84n-2')]")

# Her bir menü elemanına tıklayıp işlemleri gerçekleştir
for menu in menuler:
    menu.click()
    
    asagiGel()  # Sayfanın sonuna kadar kaydır
    linkCek()  # Linkleri çek

tarama()  # Tüm bağlantıları oku ve işle