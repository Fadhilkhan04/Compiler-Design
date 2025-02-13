
vowels = 'aeiouAEIOU'
consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

vowel_count = 0
consonant_count = 0

f = open('sample.txt','r')
input_string = f.read()

for char in input_string:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1


print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")