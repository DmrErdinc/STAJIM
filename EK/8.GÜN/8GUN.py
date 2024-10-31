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
# Google giriş yap
browser.get("https://google.com")
print("Bekleniyorrrr")
time.sleep(random.randint(3, 10))