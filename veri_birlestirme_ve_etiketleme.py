import pandas as pd
import string

df_devto = pd.read_csv('veriler/csharp_trendleri.csv',usecols=['Makale_Basligi'])
df_so = pd.read_csv('veriler/stackoverflow_basliklari.csv',usecols=['Makale_Basligi'])

df_birlesik = pd.concat([df_devto,df_so])

hype_dedektor = ['ai','agent','pattern','architecture','stop','complete','practical','new','first','clean','patterns','performance','actually','modern', 'heres', 'explained', 'every','model']
real_dedektor = ['.net', 'blazor','maui','wpf','winforms','webapi', 'error', 'exception', 'fix', 'null', 'bug', 'deployment', 'crash','fails','sql','cant','json','doesnt']

def etiketle(baslik):
    kucuk_baslik = str(baslik).lower()
    temiz_baslik = kucuk_baslik.translate(str.maketrans('','',string.punctuation))
    kelimeler = temiz_baslik.split()

    for kelime in hype_dedektor:
        if kelime in kelimeler : 
            return 1
            
    for kelime in real_dedektor:
        if kelime in kelimeler:
            return 0
            
    return -1

df_birlesik['Etiket'] = df_birlesik['Makale_Basligi'].apply(etiketle)

etkili_veri = df_birlesik[df_birlesik['Etiket'] != -1]

print(f"Toplam birleşik veri: {len(df_birlesik)}")
print(f"Etiketlenebilen (Modele gidecek) etkili veri: {len(etkili_veri)}")

etkili_veri.to_csv("veriler/ml_icin_etiketli_veri.csv", index=False, encoding="utf-8-sig")
print("Veri birlestirme ve etiketleme tamamlandi")