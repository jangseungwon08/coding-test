str = input()
temp = ''
for i in str:
    if i.isupper():
        temp += i.lower()
    else:
        temp += i.upper()
print(temp)