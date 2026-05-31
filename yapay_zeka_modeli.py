import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

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

joblib.dump(model,"models/model.joblib")
joblib.dump(vektor_donusturucu,"models/vektor.joblib")