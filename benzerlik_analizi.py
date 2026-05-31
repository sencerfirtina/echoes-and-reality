import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

df = pd.read_csv('veriler/ml_icin_etiketli_veri.csv')
vektor_donusturucu = TfidfVectorizer()
X_matematiksel = vektor_donusturucu.fit_transform(df['Makale_Basligi'])

X_hype = X_matematiksel[(df['Etiket'] == 1).to_numpy()]
X_reality = X_matematiksel[(df['Etiket'] == 0).to_numpy()]

hype_merkez = np.asarray(X_hype.mean(axis=0))
reality_merkez = np.asarray(X_reality.mean(axis=0))

test_basligi = ["NullReferenceException when binding List to WPF DataGrid"]
test_vektoru = vektor_donusturucu.transform(test_basligi)

hype_benzerlik_skoru = cosine_similarity(test_vektoru,hype_merkez)[0][0]
reality_benzerlik_skoru = cosine_similarity(test_vektoru,reality_merkez)[0][0]

joblib.dump(hype_merkez,"models/hype_merkez.joblib")
joblib.dump(reality_merkez,"models/reality_merkez.joblib")

print(f"Hype merkezine acisal benzerlik (cosine similarity): {hype_benzerlik_skoru:.2%}")
print(f"Reality merkezine acisal benzerlik (cosine similarity): {reality_benzerlik_skoru:.2%}")