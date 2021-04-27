stack=[]
string=[]
def append(string,add):
    string.extend(add)
def delete(string,k):
    for _ in range(k):
        string.pop()
def undo(stack,string):
    o,arr=stack.pop()
    if o=='1':
        delete(string,len(arr))
    if o=='2':
        append(string,arr)

for _ in range(int(input())):
    operation=input().split()
    if operation[0]=='1':
        add=[x for x in operation[1]]
        stack.append(('1',add))
        append(string,add)
    if operation[0]=='2':
        k=int(operation[1])        
        stack.append(('2',string[len(string)-k:]))
        delete(string,k)
    if operation[0]=='3':
        print(string[int(operation[1])-1])
    if operation[0]=='4':
        undo(stack,string)
    
    

