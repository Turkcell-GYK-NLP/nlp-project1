## Haber Başlıkları Üzerine NLP Analizi

Bu projede, haber başlıkları üzerinde metin ön işleme, vektörleştirme, duygu analizi ve konu modelleme teknikleri uygulanmıştır. Amaç, metinlerden anlamlı yapılar çıkarmak ve doğal dil işleme yöntemlerinin haber verisi üzerindeki etkilerini gözlemlemektir.

## Proje Özeti

Bu proje, **Kaggle'ın News Category Dataset**'inden alınan **209.527 haber başlığı** üzerinde gelişmiş NLP analizleri gerçekleştirir. Analizler şunları içerir:

- **Duygu Analizi** (TextBlob ile)
- **Konu Modelleme** (LDA ve NMF algoritmaları)
- **Metin Ön İşleme** (POS etiketleme ile geliştirilmiş)
- **Özellik Mühendisliği** (TF-IDF vektörleştirme)

## Özellikler

- **Çoklu Algoritma ile Konu Modelleme**: Hem LDA hem NMF uygulanır
- **Gelişmiş Metin İşleme**: POS etiketleme ile doğruluk artırılır
- **Kapsamlı Duygu Analizi**: Haberler Pozitif/Negatif/Nötr olarak sınıflandırılır
- **Ölçeklenebilir Pipeline**: 200K+ doküman verimli şekilde işlenir
- **Kıyaslamalı Analiz**: Algoritmalar yan yana değerlendirilir

## Veri Kümesi

- **Kaynak**: [Kaggle News Category Dataset v3](https://www.kaggle.com/datasets/rmisra/news-category-dataset)
- **Boyut**: 209.527 haber başlığı
- **Dil**: İngilizce
- **Dönem**: Modern haber medyası (2016-2020)
- **Format**: JSON Lines

## Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip paket yöneticisi

### Kurulum Adımları

1. **Depoyu klonlayın**

git clone https://github.com/yourusername/news-nlp-analysis.git
cd news-nlp-analysis


2. **Sanal ortam oluşturun**

python3 -m venv nlp_env
source nlp_env/bin/activate  # Windows: nlp_env\Scripts\activate


3. **Bağımlılıkları yükleyin**

pip install -r requirements.txt


4. **Veri kümesini indirin**
   - [Kaggle](https://www.kaggle.com/datasets/rmisra/news-category-dataset) üzerinden `News_Category_Dataset_v3.json` dosyasını indirin
   - Proje ana dizinine yerleştirin

-----

## **Veri Kümesi Analizi**

# **Veri Kümesi Özellikleri:**
- **Kaynak:** Kaggle News Category Dataset v3
- **Toplam Kayıt:** 209.527 haber başlığı
- **Dil:** İngilizce
- **Zaman Aralığı:** Modern haber medyası (2016-2020)
- **Veri Kalitesi:** Temiz, eksik veri yok denecek kadar az

# **Veri Dağılımı İçgörüleri:**
Veri kümesi, Amerikan medyasının politikadan yaşam tarzına, teknolojiden eğlenceye kadar dengeli bir dağılım sunar.

-----

##  **Metin Ön İşleme Pipeline Analizi**

# Uygulanan Ön İşleme Teknikleri:

Doğal dil işleme süreçlerinde metnin doğru şekilde temsil edilebilmesi için öncelikle temizlenmesi ve sadeleştirilmesi gerekir. Bu akış, metni sadeleştirip zenginleştirerek analiz için hazırlar. Bu projede uygulanan adımlar aşağıdaki sırayla gerçekleştirilmiştir:

1. Küçük harfe çevirme: 
   Aynı kelimenin farklı yazım biçimlerinin (örneğin “News” ve “news”) tekilleştirilmesini sağlar.

2. Noktalama işaretlerinin ve sayıların temizlenmesi:  
   Yazım işaretleri ve sayılar çoğu analizde anlam taşımadığı için çıkarılmıştır.

3. Tokenization (kelimelere ayırma): 
   Başlıklar, kelime bazlı analiz yapabilmek adına parçalara ayrılmıştır.

4. Stopword temizliği: 
   Anlam taşımayan sık geçen kelimeler (örneğin “the”, “and”, “is”) çıkarılmıştır.

5. Lemmatizasyon:
   Kelimeler, kök hallerine indirgenerek benzer anlamlı sözcükler tek biçimde değerlendirilmiştir (örneğin “running” → “run”).

6. POS (Part-of-Speech) etiketleme:  
   Her kelimenin türü (isim, fiil, sıfat vb.) belirlenmiş ve bu bilgi, metin temsilini zenginleştirmek amacıyla kelimelere eklenmiştir (örneğin “run_VB”).

Bu sıralama sadeleştir → anlamlaştır → zenginleştir mantığıyla kurgulanmıştır. Her adım, bir sonraki adıma uygun veri sağlamaktadır.

-----

## **Vektörleştirme Yöntemleri Karşılaştırması**

1. CountVectorizer (Bag-of-Words):
   Metni, kelimelerin sıklıklarına göre sayısal bir forma dönüştürür. Yöntem basit ve hızlıdır ancak kelimenin bağlam içindeki önemini dikkate almaz.

2. TF-IDF (Term Frequency – Inverse Document Frequency): 
   Hem kelimenin belge içindeki geçiş sıklığını hem de veri kümesindeki yaygınlığını hesaba katar. Daha ayırt edici kelimelere yüksek ağırlık verir.

Her iki yöntem de POS etiketli metinlerde kullanılarak daha ayrıntılı temsiller elde edilmiştir.

-----

## **Duygu Analizi Değerlendirmesi**

Duygu analizi, TextBlob kütüphanesi ile gerçekleştirilmiş ve haber başlıkları Pozitif, Negatif ve Nötr olarak sınıflandırılmıştır.

# TextBlob Sonuçları:

Nötr:   126.829 (%60,7)
Pozitif:   58.739 (%28,1)
Negatif:   23.959 (%11,4)


# Değerlendirme:  

Haber metinlerinin büyük oranda nötr kalması beklenen bir durumdur. Pozitif başlıklar genellikle yaşam ve kültür haberlerine aitken, negatif olanlar daha çok siyasi ve kriz içerikli başlıklarda görülmektedir.

-----

## **Konu Modelleme Derinlemesine Analiz**

LDA (Latent Dirichlet Allocation) ve NMF (Non-negative Matrix Factorization) yöntemleri kullanılarak başlıklar anlamsal olarak kümelendirilmiştir. Anahtar kelimeler ve temalar:

LDA Çıktısı:

- Konu 1: trump, woman, health, clinton → Politika ve toplumsal temalar  
- Konu 2: trump, say, photo, video, new → Medya içerikli siyasi başlıklar  
- Konu 3: day, way, year, new, photo → Zaman temelli yaşam haberleri  
- Konu 4: photo, new, best, food, week → Yaşam tarzı ve içerik önerileri  
- Konu 5: trump, new, photo, donald, video → Trump gündemi ve medya

NMF Çıktısı:

- Konu 1: photo, best, world, home, style → Stil, kültür, yaşam  
- Konu 2: trump, donald, clinton, say → Amerikan siyaseti  
- Konu 3: new, year, york, resolution, time → Yeni yıl ve şehir hayatı  
- Konu 4: day, way, thing, life, one → Kişisel içerikler ve yorumlar  
- Konu 5: woman, week, tweet, funniest, parent → Mizah ve ebeveynlik

LDA, daha geniş içerikli ve örtüşen konu kümeleri üretirken NMF daha keskin ve belirgin konular ortaya çıkarmıştır.

-----

## **Algoritma Performans Karşılaştırması**

LDA vs NMF Analizi:

# LDA Güçlü Yönleri:
- Olasılıksal modelleme yaklaşımı
- Konular arası geçişleri modeller
- Doküman-konu dağılımı sunar

# NMF Avantajları:
- Daha net konu ayrımı
- Negatif olmayan kısıt sayesinde yorumlanabilirlik
- Daha belirgin konu sınırları


## Genel Değerlendirme

- Başlıkların kısa olması sınırlı bağlam sunsa da yapılan ön işlemler metinleri analiz için uygun hale getirmiştir.  
- TF-IDF ve POS etiketleme birlikte kullanıldığında konu modelleme sonuçları daha ayrışabilir olmuştur.  
- Duygu analizi çıktısı, haber dilinin genelde tarafsız olmasına paralel olarak nötr sınıfların ağırlıklı çıktığını göstermiştir.  
- LDA ve NMF çıktıları anlamlı konu başlıklarıyla yorumlanabilmiş ve kıyaslanabilir farklılıklar ortaya koymuştur.

## Kullanılan Kütüphaneler

- pandas  
- numpy
- nltk  
- scikit-learn  
- textblob  
- re

## Hazırlayanlar

- Bilgesu Miray Karakoç  
- Esra Kaya  
- Zeynep Öztürk 