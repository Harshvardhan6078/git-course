# if file is not present
f=open('hello.txt','w')  # w for write txt file
f.write('hello')
f.close()
# f.write('hello')

f=open('hello.txt','r')
x=f.read()
print(x)
f.close()