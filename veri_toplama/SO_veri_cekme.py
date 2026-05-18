import requests
import time
import pandas as pd
import html

so_basliklari = []

for sayfa in range(1, 26):
    print(f"{sayfa}. sayfa isteniyor...")
    
    api_linki = f"https://api.stackexchange.com/2.3/questions?page={sayfa}&pagesize=100&order=desc&sort=creation&tagged=c%23&site=stackoverflow"
    
    cevap = requests.get(api_linki)
    
    if cevap.status_code == 200:
        saf_veri = cevap.json()
        sorular = saf_veri['items']
        
        for soru in sorular:
            ham_soru_basligi = soru['title']
            temiz_baslik = html.unescape(ham_soru_basligi)
            so_basliklari.append(temiz_baslik)


    else:
        print(f"Hata! {sayfa}. sayfa çekilemedi. Kod: {cevap.status_code}")
        break

    time.sleep(1)

print("\nButun sayfalar cekildi! Veriler isleniyor...")

benzersiz_basliklar = list(set(so_basliklari))

df = pd.DataFrame(benzersiz_basliklar, columns=["Makale_Basligi"])

df.to_csv("stackoverflow_basliklari.csv", index=False, encoding="utf-8-sig")

print(f"\nToplam {len(benzersiz_basliklar)} farkli teknoloji tespit edildi.")
print("Veriler basariyla kaydedildi")