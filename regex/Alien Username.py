import re
p=r'^[_\.]\d{1,}[a-zA-Z]*[_]{0,1}$'
for i in range(int(input())):
    s=input()
    if re.findall(p,s):
        print('VALID')
    else:
        print('INVALID')
