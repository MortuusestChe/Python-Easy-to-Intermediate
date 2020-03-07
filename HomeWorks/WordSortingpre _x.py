list=[]
listx=[]
while 1<2:
    temp = input("")
    if (temp == ''):
        break
    elif(temp[0]=='x'):
        listx.append(temp)
    else:
        list.append(temp)
list.sort()
listx.sort()
listx.extend(list)
print(listx)