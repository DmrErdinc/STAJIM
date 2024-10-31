import csv
import re
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException ,NoSuchElementException
import time
import random

option = Options()
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave"

option.add_argument('--disable-notifications')
option.binary_location = brave_path

option.add_argument("--profile-directory=Default")
option.add_argument('--ignore-ssl-errors')
option.add_argument("--disable-notifications")
option.add_argument("--disable-popup-blocking")
option.add_argument("--disable-save-password-bubble")
option.add_argument('--headless')

# Tarayıcı seçeneklerini ayarlama
options = webdriver.ChromeOptions()

# ChromeDriver'ı güncelle ve başlat
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.maximize_window()

# Kampüs Ulaşım Pusula'ya giriş yap
browser.get("https://kampp.in/kamp-alanlari")
print("Bekleniyorrrr")
time.sleep(random.randint(3, 10))



def asagiGel():
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        # Sayfanın sonuna kadar kaydır
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Sayfanın yüklenmesi için bekleyin
        time.sleep(random.randint(3, 5))
        
        # Yeni yüksekliği kontrol edin
        new_height = browser.execute_script("return document.body.scrollHeight")
        
        # Yüksekliğin değişip değişmediğini kontrol edin (daha fazla içerik yoksa)
        if new_height == last_height:
            break
        last_height = new_height

def linkCek():
    print(linkCek)
    dosya_adi = "./linklerr3.txt"

    file = open( dosya_adi, 'a',encoding="utf-8")


    alanlar = browser.find_elements(By.XPATH, "//div[contains(@class,'BszUz')]")

    print(len(alanlar))

    # baslik, telefon,websitesi,hakkinda,adres,konumLink
    for alan in alanlar:
        link = alan.get_attribute("href")
        file.write(link+'\n')

def isletmeOku(link):
    browser.get("https://kampp.in/"+link)
    time.sleep(random.randint(3, 5))

    '''
    İl ve İlçe Alma İşlemi
    '''
    ililce = WebDriverWait(browser, 10).until(
          EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[2]/div[1]/div/span[2]'))
        ).text

    print(ililce)
    if ililce:
            ililce = ililce.split(" / ")

            il = ililce[0]  
            ilce = ililce[1]

    '''
    Başlık Alma İşlemi
    '''
    try:
        baslik = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[2]/div[1]/span'))
        ).text
        print(baslik)
    except TimeoutException:
        print("Başlık bulunamadı")
        return
    except NoSuchElementException:
        print("Başlık bulunamadı yok belirtilmemiş ")
        return
    '''
    Hakkında
    '''
    hakkindatext = ''
    try:
        hakkında = WebDriverWait(browser, 10).until(
            
             EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[5]/div/div/div[3]/span'))
        ).text
        if hakkında:
            print(hakkında)
        else:
            print("Hakkında bilgisi yok")
    except TimeoutException:
        print("Hakkında bilgisi yok")
    except NoSuchElementException:
        print("Hakkında bilgisi yok belirtilmemiş ")
          
    '''
    Konum Bilgisi
    '''
    try:
        Konum = WebDriverWait(browser, 10).until(
            
             EC.presence_of_element_located((By.XPATH, "//iframe[contains(@class,'slug__StyledMap-sc-1e6v0q9-5')]"))
        ).get_attribute('src')
        if Konum:
            print(Konum)
            q_param = re.search(r'q=([^&]+)', Konum).group(1)
            konum = q_param.split(",")

            lat = konum[0]
            lng = konum[1]
            print(q_param)
        else:
            print("Konum bilgisi yok")
    except TimeoutException:
        print("Konum bilgisi yok")
   
    ## Verileri CSV dosyasına yazma
    veriler = [baslik,il,ilce,Konum,hakkında]
    with open('Bilgiler.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(veriler)


menuler = browser.find_elements(By.XPATH, "//div[contains(@class,'ListHeader__TabbarItem-sc-1phw84n-2')]" )


for menu in menuler:
    menu.click()
    
    asagiGel()
    linkCek()
