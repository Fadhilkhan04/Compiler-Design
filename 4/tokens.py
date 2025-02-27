import re

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
tokens = re.findall(r'\w+', text)
print(tokens)
