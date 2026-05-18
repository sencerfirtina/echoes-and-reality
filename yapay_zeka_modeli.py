import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('veriler/ml_icin_etiketli_veri.csv')

X = df['Makale_Basligi']
y = df['Etiket']

vektor_donusturucu = TfidfVectorizer()
X_matematiksel = vektor_donusturucu.fit_transform(X)

X_egitim, X_test, y_egitim, y_test = train_test_split(X_matematiksel,y,test_size=0.2,random_state=42,stratify=y)
print(f"Toplam Veri: {X.shape[0]} | Eğitim Icin Ayrilan: {X_egitim.shape[0]} | Sinav Icin Ayrilan: {X_test.shape[0]}")

model = MultinomialNB()
model.fit(X_egitim,y_egitim)

tahminler = model.predict(X_test)

dogruluk_orani = accuracy_score(y_test,tahminler)

print(f"Dogruluk Orani (Accuracy): %{dogruluk_orani * 100:.2f}\n")

print(classification_report(y_test, tahminler, target_names=["Reality (0)", "Hype (1)"]))

# --- KULLANIM ÖRNEĞİ (TEST) ---

test_basliklari = [
    "Mastering Clean Architecture with AI Agents in .NET", #HYPE
    "How to bind a DataGrid in WPF using C#", #REALITY
    "The Ultimate Framework for Building Autonomous AI Systems", #HYPE
    "Troubleshooting Memory Leaks in legacy WinForms applications", #REALITY
    "Deploying an ASP.NET Core WebAPI to Azure App Service" #REALITY
]

test_matematiksel = vektor_donusturucu.transform(test_basliklari)

sonuclar = model.predict(test_matematiksel)

for i in range(len(test_basliklari)):
    baslik = test_basliklari[i]
    karar = sonuclar[i]
    
    if karar == 1:
        print(f"HYPE (ABARTI)-> {baslik}")
    else:
        print(f"REALITY (GERCEKCI)-> {baslik}")