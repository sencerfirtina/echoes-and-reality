from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

ayarlar = Options()
ayarlar.add_argument('--log-level=3')
ayarlar.add_experimental_option('excludeSwitches', ['enable-logging'])

url = 'https://dev.to/t/csharp'

surucu = webdriver.Edge(options=ayarlar)

surucu.get(url)

print("Siteye girildi, makalelerin yüklenmesi bekleniyor...")

print("DİKKAT: Site acildi!")
print("Giriş yapmaniz (Login) veya cikan engelleri kapatmaniz için 40 saniyeniz var.")
print("Sure dolduğunda kontrolu bot devralacak...\n")

time.sleep(40) 

print("Sure doldu! Klavye ve fareden ellerinizi cekin, bot devraliyor...\n")

kaydirma_sayisi = 150

for i in range(kaydirma_sayisi):
    surucu.execute_script("window.scrollBy(0,1500);")

    print(f"{i+1}. kez en asagi inildi, yeni makalelerin yuklenmesi bekleniyor...")
    time.sleep(2)

print("Toplama islemi bitti.")

dolu_html = surucu.page_source

corba = BeautifulSoup(dolu_html, 'html.parser')

basliklar = corba.find_all(['h2','h3'], class_ = 'crayons-story__title')

toplanan_veriler = []

for baslik in basliklar:
    temiz_baslik = baslik.text.strip()
    toplanan_veriler.append(temiz_baslik)

benzersiz_veriler = list(set(toplanan_veriler))

print(f"Tam olarak {len(benzersiz_veriler)} adet baslik toplandi")

df = pd.DataFrame(toplanan_veriler,columns=["Makale_Basligi"])
df.to_csv("csharp_trendleri.csv", index=False, encoding="utf-8-sig")

surucu.quit()
print("Veriler basariyla kaydedildi")