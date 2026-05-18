import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

def populer_kelimeleri_bul(dosya_yolu,sutun_adi):
    df = pd.read_csv(dosya_yolu)
    basliklar = df[sutun_adi].dropna().tolist()

    ing_cop_kelimeler = set(stopwords.words('english'))

    ekstra_copler = {'how','use','using','build','building','create','creating','guide','tutorial','c#','net',
                    'vs','10','part','dev','digest','issue','built','day','pdf','code','core',
                    'visual', 'studio', 'engine', 'project', 'cnet', 'de', 'library', 'pattern','api', 'data', 'web', 'aspnet', 'ef', 'blazor', 'microsoft', 'development', 'developers',
                    'app', 'file', 'get', 'type', 'class', 'application', 'object', 'windows', 'server', 'property', 'way', 'work', 'value', 'method', 'multiple', 'function', 'service',
                    'framework','without','azure','unity','maui'}
    cop_tam = ing_cop_kelimeler.union(ekstra_copler)

    temizlenmis_kelimeler = []

    for baslik in basliklar:
        kucuk_baslik = str(baslik).lower()

        kucuk_baslik = kucuk_baslik.translate(str.maketrans('','',string.punctuation))

        kelimeler = word_tokenize(kucuk_baslik)

        for kelime in kelimeler:
            if kelime not in cop_tam and len(kelime) > 1 and kelime.isalpha():
                temizlenmis_kelimeler.append(kelime)
        
    frekans = nltk.FreqDist(temizlenmis_kelimeler)
    en_populer_25 = frekans.most_common(25)
    populer_kelime_seti = set()
    for kelime,sayi in en_populer_25:
        populer_kelime_seti.add(kelime)
    
    return populer_kelime_seti


if __name__ == "__main__":
    devto_kelimeleri = populer_kelimeleri_bul("veriler/csharp_trendleri.csv","Makale_Basligi")
    so_kelimeleri = populer_kelimeleri_bul("veriler/stackoverflow_basliklari.csv","Makale_Basligi")
    truva_atlari = devto_kelimeleri & so_kelimeleri
    print("\n--- DEV.TO'DA SU AN EN POPULER 25 KAVRAM ---")
    print(devto_kelimeleri)
    print("\n--- STACK OVERFLOW'DA SU AN EN ÇOK GECEN 25 KAVRAM ---")
    print(so_kelimeleri)
    print("\n--- COPE EKLENECEK KELİMELER ---")
    print(truva_atlari)