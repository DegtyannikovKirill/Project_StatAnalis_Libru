from nltk import ngrams
from collections import Counter
import re

with open("1.txt") as f:
    text = f.read()
a = re.sub(r'[^\w\s]',' ',text)
a = a.lower()
n = 3
sixgrams = ngrams(a.split(), n)
s = []

for grams in sixgrams:
    s.append(grams)


with open("2.txt") as f:
    text = f.read()
b = re.sub(r'[^\w\s]',' ',text)
b = b.lower()
n = 3
sixgrams = ngrams(b.split(), n)
t = []

for grams in sixgrams:
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
sixgrams = ngrams(c.split(), n)
p = []

for grams in sixgrams:
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
sixgrams = ngrams(d.split(), n)
k = []

for grams in sixgrams:
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
sixgrams = ngrams(e.split(), n)
g = []

for grams in sixgrams:
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
sixgrams = ngrams(r.split(), n)
y = []

for grams in sixgrams:
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
sixgrams = ngrams(u.split(), n)
l = []

for grams in sixgrams:
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
sixgrams = ngrams(h.split(), n)
v = []

for grams in sixgrams:
    v.append(grams)

result7=list(set(s) & set(v))
print(result7)




