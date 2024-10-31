import urllib.request

# URL'ler
url1 = "https://miro.medium.com/v2/resize:fit:720/format:webp/1*jsgLaIkhgF7SzQS1FWIPug.jpeg"
url2 = "https://datascientest.com/en/files/2024/02/python.png"  
url3 = "https://muratcicek.net/wp-content/uploads/2021/06/python_logo-2048x1152.png" 

urllistesi = [url1, url2, url3]
say = 1

# User-Agent tanımlıyoruz
headers = {'User-Agent': 'Mozilla/5.0'}

for url in urllistesi:
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req) as response:
            # Gelen veriyi dosyaya yazıyoruz
            with open("Resim" + str(say) + ".jpg", 'wb') as f:
                f.write(response.read())
        
        print(f"Resim{say}.jpg başarıyla indirildi.")
    
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason} - {url}")
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    
    say += 1