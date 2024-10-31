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
        
menuler = browser.find_elements(By.XPATH, "//div[contains(@class,'ListHeader__TabbarItem-sc-1phw84n-2')]" )

for menu in menuler:
    menu.click()
    
    asagiGel()
    linkCek()


