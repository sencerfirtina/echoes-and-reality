# Yazılım Ekosisteminde 'Hype' ve 'Realite' İkilemi: İki Farklı Platformun Metin Madenciliği ile Sınıflandırma ve Benzerlik Analizi

Bu proje, blog platformlarındaki içerik üreticilerinin yönlendirdiği pazarlama trendleri ("Hype") ile sahadaki geliştiricilerin karşılaştığı gerçek mühendislik sorunları ("Reality") arasındaki istatistiksel makası ölçmek için geliştirilmiş uçtan uca bir **Doğal Dil İşleme (NLP)** ve **Makine Öğrenmesi** boru hattıdır (pipeline).

## 🎯 Projenin Felsefesi ve Amacı
Günümüz yazılım dünyasında "AI Agents", "Clean Architecture" gibi kavramlar sürekli köpürtülürken; sahadaki geliştiriciler `NullReferenceException`, bellek sızıntıları ve "Legacy" sistemlerle boğuşmaktadır. Bu proje, metin madenciliği kullanarak teknoloji dünyasındaki bu algı ve gerçeklik ikilemini matematiksel olarak kanıtlamayı hedefler.

## 🏗️ Mimari ve Boru Hattı (Pipeline)

Sistem 5 ana fazdan oluşmaktadır:

1. **Veri Toplama (Data Ingestion):**
   * **Hype Verisi:** Dev.to platformundan Selenium kullanılarak güncel C# makale başlıkları kazınmıştır.
   * **Reality Verisi:** Stack Exchange API aracılığıyla StackOverflow'daki en güncel ve en çok etkileşim alan C# soru başlıkları çekilmiştir.
2. **Ön İşleme (NLP Preprocessing):** HTML etiketlerinin temizlenmesi (`html.unescape`), noktalama işaretlerinin izolasyonu ve "Domain-Specific Stopwords" (her iki platformda da sık geçen 'app', 'class', 'method' gibi kelimeler) tespiti yapılmıştır.
3. **Zayıf Etiketleme (Weak Supervision):** Etiketli veri eksikliğini gidermek için kurallar tabanlı (Rule-based) bir etiketleme algoritması geliştirilmiş ve ham veriler otomatik olarak sınıflandırılmıştır.
4. **Sınıflandırma (Classification):** Metinler TF-IDF ile vektörel uzaya taşınmış ve `Multinomial Naive Bayes` modeli, veri dengesizliğini önleyen tabakalı örnekleme (`stratify`) ile eğitilmiştir.
5. **Açısal Benzerlik Analizi (1 vs All):** Sınıflandırmanın ötesinde, yeni gelen bir başlığın "Saf Hype" ve "Saf Reality" ağırlık merkezlerine (Centroid) olan uzaklığı **Kosinüs Benzerliği (Cosine Similarity)** ile ölçülmektedir.

## 📊 Model Performansı

Gürültülü (noisy) gerçek dünya verileriyle eğitilen model, ezberlemeden (overfitting) kaçınarak aşağıdaki kararlı sonuçları üretmiştir:
* **Test Seti Doğruluk Oranı (Accuracy):** ~%84
* **Veri Büyüklüğü:** 1000+ Doğrulanmış Başlık

## 🚀 Kurulum ve Çalıştırma

Modeli kendi makinenizde test etmek için aşağıdaki adımları izleyebilirsiniz:

1. Depoyu klonlayın:
   ```bash
   git clone [TODO: GITHUB_REPO_LINKI_BURAYA]

   ```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas numpy scikit-learn nltk requests selenium

```


3. NLTK kelime dağarcığını indirin (Eğer yüklü değilse):
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')

```


4. Yeni bir başlığı analiz etmek için `benzerlik_analizi.py` veya `yapay_zeka_modeli.py` dosyalarını çalıştırın.

---

*Bu proje Sencer Fırtına tarafından geliştirilmiştir.*
