vcount = 0
ccount = 0

vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvxywzBCDFGHJKLMNPQRSTVXYWZ'

f = open('sample.txt','r')
text = f.read()
for char in text :
  if char in vowels:
    vcount +=1
  elif char in consonants:
    ccount +=1
  else :
    pass

print(vcount)
print(ccount)