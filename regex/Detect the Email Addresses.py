import re
text='\n'.join(input() for _ in range(int(input())))
res=list(set(re.findall(r'[\w\.]+@(?:\w+\.)+\w+',text)))
res.sort()
string=';'.join(res)
print(string)
