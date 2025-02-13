
 
num_words = 0
num_lines = 0
 
with open('sample.txt', 'r') as f:
    for line in f:
        num_lines += 1
        words = line.split()
        num_words += len(words)
print("Number of words : ",num_words)
print("Number of lines : ",num_lines)
