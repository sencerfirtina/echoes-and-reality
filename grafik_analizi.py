import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("veriler/ml_icin_etiketli_veri.csv")

kelime_sayisi = df['Makale_Basligi'].apply(lambda x: len(str(x).split()))

plt.figure(figsize=(8,6))

sns.boxplot(x="Etiket",y=kelime_sayisi,data=df)

plt.title("Hype ve Reality Başlıklarının Kelime Sayısı Dağılımı")
plt.xticks([0, 1], ['Reality (StackOverflow)', 'Hype (Dev.to)'])
plt.ylabel("Kelime Sayısı")

plt.savefig("kutu_grafigi.png")

print("Grafik basariyla kaydedildi")