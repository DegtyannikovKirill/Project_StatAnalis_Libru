#статистический анализ текста любого автора с сайта lib.ru.
#На основе полученных данных должны определяться фразы, характерные именно для этого автора.
#Далее берется другие тексты и проверяются, использовали ли они фразы этого автора

from nltk import ngrams
from collections import Counter
import re
import pymorphy2

# Анализатор типа слова
def pos(word, morth=pymorphy2.MorphAnalyzer()): 
      return morth.parse(word)[0].tag.POS

with open("1.txt") as f:
    text = f.read()
a = re.sub(r'[^\w\s]',' ',text)
a = a.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}

# Разделение на n-gramms
threegrams = ngrams((word for word in a.split() if pos(word) not in  
                    functors_pos), n)                               
s = []
for grams in threegrams:
    s.append(grams)
#print(Counter(s))

with open("2.txt") as f:
    text = f.read()
b = re.sub(r'[^\w\s]',' ',text)
b = b.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in b.split() if pos(word) not in  
                    functors_pos), n)
t = []

for grams in threegrams:
    t.append(grams)

result1=list(set(s) & set(t))
print (result1)

print('\n__________________')
print('__________________\n')
    

with open("3.txt") as f:
    text = f.read()
c = re.sub(r'[^\w\s]',' ',text)
c = c.lower()
n = 3
threegrams = ngrams(c.split(), n)
p = []

for grams in threegrams:
    p.append(grams)

result2=list(set(s) & set(p))
print (result2)

print('\n__________________')
print('__________________\n')



with open("4.txt") as f:
    text = f.read()
d = re.sub(r'[^\w\s]',' ',text)
d = d.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in d.split() if pos(word) not in  
                    functors_pos), n)

k = []

for grams in threegrams:
    k.append(grams)

result3=list(set(s) & set(k))
print(result3)

print('\n__________________')
print('__________________\n')

with open("5.txt") as f:
    text = f.read()
e = re.sub(r'[^\w\s]',' ',text)
e = e.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in e.split() if pos(word) not in  
                    functors_pos), n)
g = []

for grams in threegrams:
    g.append(grams)

result4=list(set(s) & set(g))
print(result4)

print('\n__________________')
print('__________________\n')

with open("6.txt") as f:
    text = f.read()
r = re.sub(r'[^\w\s]',' ',text)
r = r.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in r.split() if pos(word) not in  
                    functors_pos), n)
y = []

for grams in threegrams:
    y.append(grams)

result5=list(set(s) & set(y))
print(result5)

print('\n__________________')
print('__________________\n')

with open("7.txt") as f:
    text = f.read()
u = re.sub(r'[^\w\s]',' ',text)
u = u.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in u.split() if pos(word) not in  
                    functors_pos), n)
l = []

for grams in threegrams:
    l.append(grams)

result6=list(set(s) & set(l))
print(result6)

print('\n__________________')
print('__________________\n')

with open("8.txt") as f:
    text = f.read()
h = re.sub(r'[^\w\s]',' ',text)
h = h.lower()
n = 3
functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
threegrams = ngrams((word for word in h.split() if pos(word) not in  
                    functors_pos), n)
v = []

for grams in threegrams:
    v.append(grams)

result7=list(set(s) & set(v))
print(result7)




