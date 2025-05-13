keywords = 'intfloatcharreturnifelseelifforwhile'
operators = '+-*/%='
delimeters = ',;{}[]()'

code = input("enter the code:\n").split()

for i in code:
  if i in keywords:
    print(i," : keyword")
  elif i in operators:
    print(i," :operators")
  elif i in delimeters:
    print(i," :delimeters")
  elif i.isdigit():
    print(i,"number")
  else:
    print(i ," : identifier")