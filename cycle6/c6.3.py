f = open('D:\csvfile.csv','r')
f_contents=f.readlines()
list1=list(f_contents)
print(list1)
f.close()