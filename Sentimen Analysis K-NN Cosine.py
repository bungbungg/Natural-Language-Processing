# -*- coding: utf-8 -*-
"""Fix Merdeka.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_DSbSN9xY-7RE_kpqHtPFsnFBSLQELxv
"""

import pandas as pd
import numpy as np

#memanggil data
data = pd.read_excel('/content/data_april.xlsx')
data.head()

#menghilangkan kolom yang tidak diperlukan
data.drop(['created_at','id_str','quote_count','reply_count','retweet_count','favorite_count','lang', 'user_id_str', 'conversation_id_str','tweet_url','username'],

        axis=1,

        inplace=True)
data.head(5)

"""## **Cleansing Data**"""

import re

def remove_pattern(tweet, pattern):
    r = re.findall(pattern, tweet)
    for i in r:
        tweet = re.sub(i, '', tweet)
    return tweet
data['full_text']=data['full_text'].apply(str)
data['full_text'] = np.vectorize(remove_pattern)(data['full_text'], "@[\w]*")
data['full_text'] = np.vectorize(remove_pattern)(data['full_text'], "#[\w]*")

"""## **Case Folding**"""

import pickle


#Buat fungsi untuk langkah case folding
def casefolding(text):
  text = text.lower() #untuk merubah huruf jadi huruf kecil
  text = re.sub(r'https?://\S+|www\.\S+', '', text) #untuk menghapus link
  text = re.sub(r'[-+]?[0-9]+', '', text) #untuk tanda - + dan numerik
  text = re.sub(r'[^\w\s]','', text) #menghapus tanda baca
  text = text.strip()
  return text

sample = data['full_text'].iloc[2] #sample data baris kelima atau data kelima
case_folding = casefolding(sample)

print('data\t: ', sample)
print('Case folding\t: ', case_folding)

"""## **Word** **Normalization**"""

#Download corpus singkatan
#untuk mendownload melalui link pake !wget
!wget https://raw.githubusercontent.com/ksnugroho/klasifikasi-spam-sms/master/data/key_norm.csv

normal_key = pd.read_csv('https://raw.githubusercontent.com/ksnugroho/klasifikasi-spam-sms/master/data/key_norm.csv')

def text_normalize(text):
  text = ' '.join([normal_key[normal_key['singkat'] == word]['hasil'].values[0] if (normal_key['singkat'] == word).any() else word for word in text.split()])
  text = str.lower(text)
  return text

sample = data['full_text'].iloc[2]
case_folding = casefolding(sample)
word_normalization = text_normalize(case_folding)

print('Raw data\t\t: ', sample)
print('Case folding\t\t: ', case_folding)
print('Word normalization\t\t: ', word_normalization)

"""## **Filtering (Stopword Removal)**"""

#install library natural language toolkit
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

stopwords_ind = stopwords.words('indonesian') #kamus kata untuk menyaring kata yang tidak diperlukan dalam pemprosesan
stopwords_ind.remove("tidak")
stopwords_ind.append("ya")

len(stopwords_ind) #melihat jmlh daftar kata yang diabaikan

stopwords_ind #melihat stopwords yang disediakan nltk

#membuat fungsi untuk langkah stopword removal
def remove_stop_words(text):
  clean_words = []
  text = text.split()
  for word in text:
    if word not in stopwords_ind:
      clean_words.append(word)
  return " ".join(clean_words)

sample = data['full_text'].iloc[2]
case_folding = casefolding(sample)
word_normalization = text_normalize(case_folding)
stopword_removal = remove_stop_words(word_normalization)

print('Raw data\t\t: ', sample)
print('Case folding\t\t: ', case_folding)
print('Word normalization\t\t: ', word_normalization)
print('Stopword removal\t: ', stopword_removal)

"""## **Stemming**"""

!pip -q install sastrawi #menginstall beda dengan import (memanggil)
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Membuat fungsi untuk langkah stemming bahasa Indonesia
def stemming(text):
  text = stemmer.stem(text)
  return text

sample = data['full_text'].iloc[2]
case_folding = casefolding(sample)
word_normalization = text_normalize(case_folding)
stopword_removal = remove_stop_words(word_normalization)
text_stemming = stemming(stopword_removal)

print('Raw data\t\t: ', sample)
print('Case folding\t\t: ', case_folding)
print('Word normalization\t\t: ', word_normalization)
print('Stopword removal\t: ', stopword_removal)
print('Stemming\t\t: ', text_stemming)

"""# **Tokenizing**"""

import nltk
nltk.download('punkt')

def tokenizingText(text): # Tokenizing or splitting a string, text into a list of tokens
    text = word_tokenize(text)
    return text

sample = data['full_text'].iloc[11]
case_folding = casefolding(sample)
word_normalization = text_normalize(case_folding)
stopword_removal = remove_stop_words(word_normalization)
text_stemming = stemming(stopword_removal)
tokenizing = tokenizingText(text_stemming)

print('Raw data\t\t: ', sample)
print('Case folding\t\t: ', case_folding)
print('Word normalization\t\t: ', word_normalization)
print('Stopword removal\t: ', stopword_removal)
print('Stemming\t\t: ', text_stemming)
print('Tokenizing\t\t: ', tokenizing)

"""## **Text Preprocessing Pipeline**"""

# Membuat fungsi untuk menggabungkan seluruh langkah text preprocessing
def text_preprocessing_process(text):
  text = casefolding(text)
  text = text_normalize(text)
  text = remove_stop_words(text)
  text = stemming(text)
  return text

# Commented out IPython magic to ensure Python compatibility.
# %%time
# data['clean_teks'] = data['full_text'].apply(text_preprocessing_process)

data

data.to_csv('data_clean_april.csv',sep=';', index=False)

data['text_preprocessed'] = data['clean_teks'].apply(tokenizingText)
data

data.to_csv('clean_data.csv')

"""## **Persiapan Data**"""

import pandas as pd
import numpy as np

data_ready = pd.read_excel('/content/clean_data_fix.xlsx')
data_ready

#memisahkan x (feature) dan y (target)
X = data_ready['clean_teks'].astype(str)
y = data_ready['Sentimen']

y.count()

"""## **Feature Extraction**"""

#Mengonversi kumpulan dokumen mentah menjadi matriks fitur TF-IDF
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html


from sklearn.feature_extraction.text import TfidfVectorizer

tf_idf = TfidfVectorizer(ngram_range=(1,1))
tf_idf.fit(X)

X_tf_idf = tf_idf.transform(X)

# Melihat Jumlah Fitur
print(len(tf_idf.get_feature_names_out()))

tf_idf.vocabulary_

# Melihat fitur-fitur apa saja yang ada di dalam corpus
print(tf_idf.get_feature_names_out())

# Melihat matriks jumlah token menggunakan TF IDF, lihat perbedaannya dengan metode BoW
# Data ini siap untuk dimasukkan dalam proses pemodelan (machine learning)

X_tf_idf = tf_idf.transform(X).toarray()

X_tf_idf

data_tf_idf = pd.DataFrame(X_tf_idf, columns=tf_idf.get_feature_names_out())
data_tf_idf

"""## **Feature Selection**"""

# Mengubah nilai data tabular tf-idf menjadi array agar dapat dijalankan pada proses seleksi fitur
X = np.array(data_tf_idf)
Y = np.array(y)

#Pilih fitur sesuai dengan k skor tertinggi.
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html

#Hitung statistik chi-squared antara setiap fitur dan kelas non-negatif.
#https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# 10 fitur dengan statistik chi-kuadrat tertinggi dipilih
chi2_features = SelectKBest(chi2, k = 5000)
X_kbest_features = chi2_features.fit_transform(X, Y)

print('Original feature number:', X.shape[1])
print('Reduced feature number:', X_kbest_features.shape[1])

data_chi2 = pd.DataFrame(chi2_features.scores_, columns=['nilai'])
data_chi2

# Menampilkan fitur beserta nilainya
feature = tf_idf.get_feature_names_out()
data_chi2['fitur'] = feature
data_chi2

# Mengurutkan fitur terbaik
data_chi2.sort_values(by='nilai', ascending=False)

#Menampilkan mask pada feature yang diseleksi
#False berarti fitur tidak terpilih dan True berarti fitur terpilih
mask =chi2_features.get_support()
mask

# Menampilkan fitur-fitur terpilih berdasarkan mask atau nilai tertinggi yang sudah dikalkulasi pada Chi-Square
new_feature = []
for bool, f in zip(mask, feature):
    if bool:
        new_feature.append(f)
    selected_feature = new_feature
selected_feature

# Membuat vocabulary baru berdasarkan fitur yang terseleksi

new_selected_features = {}

for (k,v) in tf_idf.vocabulary_.items():
    if k in selected_feature:
        new_selected_features[k] = v
new_selected_features

#Menyimpan vektor dari vocabulary di atas dalam bentuk pickle (.pkl)
import pickle
pickle.dump(new_selected_features,open("selected_feature_tf-idf2.pkl","wb"))

# Menampilkan fitur-fitur yang sudah diseleksi
# Beserta nilai vektornya pada keseluruhan data untuk dijalankan pada proses machine learning

# Hanya k fitur yang terpilih sesuai parameter k yang ditentukan sebelumnya

data_selected_feature = pd.DataFrame(X_kbest_features, columns=new_selected_features)
data_selected_feature

selected_x = X_kbest_features
selected_x

"""## **SMOTE-ENN**"""

X = selected_x
Y = data_ready.Sentimen

Y.value_counts()

pip install imblearn --user

from imblearn.combine import SMOTEENN
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import preprocessing
from collections import Counter
from matplotlib import pyplot

over_sample = SMOTEENN(sampling_strategy='auto')
le = preprocessing.LabelEncoder()
Y = le.fit_transform(Y)

print(f"Initial set observations {X.shape[0]}")
print(f"Initial set target classes {len(set(Y))}")
print('dataset shape {}'.format(Counter(Y)))

from collections import Counter
from matplotlib import pyplot
counter = Counter(Y)
pyplot.bar(counter.keys(), counter.values())
pyplot.show()

X, Y = over_sample.fit_resample(X, Y)                       # jika error berarti rasio antar kelas sudah seimbang


print(f"Modified set observations {X.shape[0]}")
print(f"Modified set target classes {len(set(Y))}")
print('Resample data {}'.format(Counter(Y)))

X_smoteenn= np.array(X)       # jadikan X.todense() jika error
X_smoteenn

Y_smoteenn = np.array(Y)
Y_smoteenn

from collections import Counter
from matplotlib import pyplot
counter = Counter(Y_smoteenn)
pyplot.bar(counter.keys(), counter.values())
pyplot.show()



"""## **Split Data**"""

#Import Library
import random
from sklearn.model_selection import train_test_split

#Memisihkan data training dan data testing dengan perbandingan 80:20
X_train, X_test, y_train, y_test = train_test_split(X_smoteenn,Y_smoteenn,test_size=0.2, random_state=57)

print('Banyak data x_train :',len(X_train))
print('Banyak data x_test  :',len(X_test))
print('Banyak data y_train :',len(y_train))
print('Banyak data y_test  :',len(y_test))

"""## **KNN**"""

#Algoritme

from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix, make_scorer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns

def training_knn(X_train, X_test, y_train, y_test, preproc):

    clf = KNeighborsClassifier(n_neighbors=1, metric='cosine')
    clf.fit(X_train, y_train)

    res = pd.DataFrame(columns = ['Preprocessing', 'Model', 'Precision', 'Recall', 'F1-score', 'Accuracy'])

    y_pred = clf.predict(X_test)
    cf_matrix = confusion_matrix(y_test, y_pred)
    print(cf_matrix)

    sns.heatmap(cf_matrix, annot=True, cmap='Blues', fmt='g')
    f1 = f1_score(y_pred, y_test, average = 'weighted')
    pres = precision_score(y_pred, y_test, average = 'weighted')
    rec = recall_score(y_pred, y_test, average = 'weighted')
    acc = accuracy_score(y_pred, y_test)




    res = res.append({'Preprocessing': preproc, 'Model': 'K-NN', 'Precision': pres,
                     'Recall': rec, 'F1-score': f1, 'Accuracy': acc}, ignore_index = True)

    return res

clf = KNeighborsClassifier(n_neighbors=1, metric='cosine')
model = clf.fit(X_train, y_train)

# menyimpan model
from joblib import dump
dump(model, filename="model_knn_k8.joblib")

y_test = pd.DataFrame(y_test, columns=['y_test'])
y_test.to_excel('y_test_k8.xlsx', index=False)
y_test

y_predict= clf.predict(X_test)
y_predict = pd.DataFrame(y_predict, columns=['y_predict'])
y_predict.to_excel('y_predict_k8.xlsx', index=False)
y_predict

"""## **Model Evaluation**"""

result = pd.DataFrame(columns = ['Preprocessing', 'Model', 'Precision', 'Recall', 'F1-score', 'Accuracy'])
result = result.append(training_knn(X_train, X_test, y_train, y_test, 'TF-IDF 1-grams'), ignore_index = True)

result

"""## **LDA**"""

import pandas as pd
import numpy as np

data_token = pd.read_excel('/content/data_token.xlsx')
data_token

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

def word_tokenize_wrapper(text):
    return word_tokenize(text)
data_token['text_data_token'] = data_token['clean_teks'].apply(word_tokenize_wrapper) #menghilangkan pembungkus token
data_token

import gensim
from gensim import corpora

doc = data_token['text_data_token']

dic = corpora.Dictionary(doc)
print(dic)

doc_term_matrix = [dic.doc2bow(doc) for doc in doc]

!pip install --upgrade gensim==3.8

import os       #importing os to set environment variable
def install_java():
  !apt-get install -y openjdk-8-jdk-headless -qq > /dev/null      #install openjdk
  os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"     #set environment variable
  !java -version       #check java version
install_java()

!wget http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip
!unzip mallet-2.0.8.zip

os.environ['MALLET_HOME'] = '/content/mallet-2.0.8'
mallet_path = '/content/mallet-2.0.8/bin/mallet'

import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models.wrappers import LdaMallet
from gensim.models.coherencemodel import CoherenceModel
from gensim import similarities

import os.path
import re
import glob

#Model LDA

number_of_topics=30 # sesuaikan ini untuk mengubah jumlah topik
words=20 #sesuaikan ini untuk mengubah jumlah kata yang dihasilkan untuk topik di bawah ini
model = LdaMallet(mallet_path, corpus=doc_term_matrix, num_topics=number_of_topics, id2word=dic, alpha = 0.5)
model.show_topics(num_topics=number_of_topics,num_words=words)

"""## **Deployment Klasifikasi Sentimen**"""

from joblib import load
from sklearn.feature_extraction.text import TfidfVectorizer

pipeline = load("/content/model_knn_k1.joblib")

data = input(" Masukan kata:\n")
data = text_preprocessing_process(data)

#load
tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("/content/selected_feature_tf-idf2.pkl", "rb"))))
hasil = pipeline.predict(loaded_vec.fit_transform([data]))
print("Hasil Prediksi:\n", hasil)

# Download gambar masking
!wget https://raw.githubusercontent.com/ksnugroho/klasifikasi-spam-sms/master/img/cloud.jpg

import cv2
originalImage = cv2.imread('cloud.jpg')
grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
(thresh, cloud_mask) = cv2.threshold(grayImage, 100, 255, cv2.THRESH_BINARY)

from matplotlib import pyplot as plt

# WordCloud Label review negatif

import cv2
from wordcloud import WordCloud

tweet_neg = data_ready[data_ready.Sentimen == 'Negatif']
negatif_string = []

for t in tweet_neg.clean_teks:
    negatif_string.append(t)

negatif_string = pd.Series(negatif_string).str.cat(sep=' ')
wordcloud = WordCloud(width=1600, height=800, margin=10,
                      background_color='white', colormap='turbo',
                      max_font_size=200, min_font_size=25,
                      mask=cloud_mask, contour_width=10, contour_color='DeepSkyBlue',
                      max_words=100).generate(negatif_string)
plt.figure(figsize=(10,8))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()

# WordCloud Label review netral

import cv2
from wordcloud import WordCloud

tweet_neu = data_ready[data_ready.Sentimen == 'Neutral']
neutral_string = []

for t in tweet_neu.clean_teks:
    neutral_string.append(t)

neutral_string = pd.Series(neutral_string).str.cat(sep=' ')
wordcloud = WordCloud(width=1600, height=800, margin=10,
                      background_color='white', colormap='turbo',
                      max_font_size=200, min_font_size=25,
                      mask=cloud_mask, contour_width=10, contour_color='DeepSkyBlue',
                      max_words=100).generate(neutral_string)
plt.figure(figsize=(10,8))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()

# WordCloud Label review positif

import cv2
from wordcloud import WordCloud

tweet_pos = data_ready[data_ready.Sentimen == 'Positif']
positif_string = []

for t in tweet_pos.clean_teks:
    positif_string.append(t)

positif_string = pd.Series(positif_string).str.cat(sep=' ')
wordcloud = WordCloud(width=1600, height=800, margin=10,
                      background_color='white', colormap='turbo',
                      max_font_size=200, min_font_size=25,
                      mask=cloud_mask, contour_width=10, contour_color='DeepSkyBlue',
                      max_words=100).generate(positif_string)
plt.figure(figsize=(10,8))
plt.imshow(wordcloud)
plt.axis("off")

plt.show()

"""## **LDA**"""

!pip -q install lda
!pip -q install sklearn
from lda import LDA

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import fetch_20newsgroups

# download 20newsgroups dataset
dataset = fetch_20newsgroups(remove=('headers','footers','quotes'))

# extract term-doc matrix of top 5000 words with 3 or more characters
pattern = '(?u)\\b[a-zA-Z]{3,}\\b'
cv = CountVectorizer(stop_words='english', max_features=5000, token_pattern=pattern)
doc_term = cv.fit_transform(dataset.data)
vocab = cv.get_feature_names_out()

# 15 topic LDA model
n_topics = 15
lda = LDA(n_topics)

# fit the model
lda.fit(doc_term)

# extract the two distributions we learned
user_topic = lda.theta
topic_word = lda.phi

from ctypes import cdll, POINTER, c_int, c_double
from os.path import abspath

# set up for future calls to c
_fit = cdll.LoadLibrary(abspath("lda_gibbs.so")).fit
_fit.argtypes = (c_int, *([POINTER(c_int)]*5), *([c_int]*4), *([c_double]*2))