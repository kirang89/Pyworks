import marshal
from urllib import urlopen

response = urlopen('http://learncodethehardway.org/words.txt').readlines()
word_list = [line.strip() for line in response if line]

print len(word_list)

mdata = marshal.dumps(word_list)
print len(mdata)
print "-"*10
print repr(mdata)
print "-"*10
print marshal.loads(mdata)

