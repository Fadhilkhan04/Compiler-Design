lcount = 0
wcount = 0 
f = open('sample.txt','r')

for line in f:
  lcount += 1
  word = line.split()
  wcount += len(word)

print(lcount)
print(wcount)