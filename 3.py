#статистический анализ текста любого автора с сайта lib.ru.
#На основе полученных данных должны определяться фразы, характерные именно для этого автора.
#Далее берется другие тексты и проверяются, использовали ли они фразы этого автора

import nltk
from nltk import ngrams
nltk.download('stopwords')
from collections import Counter
import re
import pymorphy2
from nltk.corpus import stopwords

# скачивание стоп-слов
stop_words = list(stopwords.words('russian'))
# добавление доп. стоп-слов
stop_words.extend(('это', 'э' , 'тебе' , 'своих' , 'тех')) 


with open("1.txt") as f:
    text = f.read()
a = re.sub(r'[^\w\s]',' ',text)
a = a.lower()
n = 3

# Разделение на n-gramms
threegrams = ngrams((w for w in a.split() if w not in stop_words), n)                               
list_ngrams = []
for grams in threegrams:
    list_ngrams.append(grams)

# часто( > 2 раз) встречаемые фразы первого песателя
frazi = dict.keys(dict(Counter(list_ngrams).most_common(28)))
print('\nЧасто ( > 2 раз) встречаемые фразы Дугласа Адамса\n\n', *frazi, '\n')

with open("2.txt") as f:
    text = f.read()
b = re.sub(r'[^\w\s]',' ',text)
b = b.lower()
n = 3

# Разделение на n-gramms
threegrams = ngrams((w for w in b.split() if w not in stop_words), n)
t = []

for grams in threegrams:
    t.append(grams)

result1=list(set(frazi) & set(t))
print ('1) Сравнение частых фраз Дугласа Адамса с первым произведение Рэя Брэдбери\n\n',result1)

print('\n__________________')
print('__________________\n')
    

with open("3.txt") as f:
    text = f.read()
c = re.sub(r'[^\w\s]',' ',text)
c = c.lower()
n = 3
threegrams = ngrams((w for w in c.split() if w not in stop_words), n)
p = []

for grams in threegrams:
    p.append(grams)

result2 = list(set(frazi) & set(p))
print ('2) Сравнение частых фраз Дугласа Адамса со вторым произведением Рэя Брэдбери\n\n',result2)

print('\n__________________')
print('__________________\n')



with open("4.txt") as f:
    text = f.read()
d = re.sub(r'[^\w\s]',' ',text)
d = d.lower()
n = 3
threegrams = ngrams((w for w in d.split() if w not in stop_words), n)

k = []
for grams in threegrams:
    k.append(grams)

result3 = list(set(frazi) & set(k))
print ('3) Сравнение частых фраз Дугласа Адамса с третьим произведением Рэя Брэдбери\n\n',result3)

print('\n__________________')
print('__________________\n')

with open("5.txt") as f:
    text = f.read()
e = re.sub(r'[^\w\s]',' ',text)
e = e.lower()
n = 3
threegrams = ngrams((w for w in e.split() if w not in stop_words), n)
g = []

for grams in threegrams:
    g.append(grams)

result4 = list(set(frazi) & set(g))
print('4) Сравнение частых фраз Дугласа Адамса с четвертым произведением Рэя Брэдбери\n\n',result4)

print('\n__________________')
print('__________________\n')

with open("6.txt") as f:
    text = f.read()
r = re.sub(r'[^\w\s]',' ',text)
r = r.lower()
n = 3
threegrams = ngrams((w for w in r.split() if w not in stop_words), n)
y = []

for grams in threegrams:
    y.append(grams)

result5 = list(set(frazi) & set(y))
print('5) Сравнение частых фраз Дугласа Адамса с пятым произведением Рэя Брэдбери\n\n',result5)

print('\n__________________')
print('__________________\n')

with open("7.txt") as f:
    text = f.read()
u = re.sub(r'[^\w\s]',' ',text)
u = u.lower()
n = 3

threegrams = ngrams((w for w in u.split() if w not in stop_words), n)
l = []

for grams in threegrams:
    l.append(grams)

result6=list(set(frazi) & set(l))
print('6) Сравнение частых фраз Дугласа Адамса с шестым произведением Рэя Брэдбери\n\n',result6)

print('\n__________________')
print('__________________\n')

with open("8.txt") as f:
    text = f.read()
h = re.sub(r'[^\w\s]',' ',text)
h = h.lower()
n = 3
threegrams = ngrams((w for w in h.split() if w not in stop_words), n)
v = []

for grams in threegrams:
    v.append(grams)

result7=list(set(frazi) & set(v))
print('7) Сравнение частых фраз Дугласа Адамса с седьмым произведением Рэя Брэдбери\n\n',result7)

#print(stop_words)




