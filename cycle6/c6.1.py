f = open("D:bin.txt" , 'r')
list = []
for x in f:
    list.append(x)

print(list)
f.close()
