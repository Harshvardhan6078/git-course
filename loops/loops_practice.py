# program to print prime numbers
list1=[]
for i in range(2,100):   
    for j in range(2,i):
        if i%j==0:
            # print(i,'not prime')
            list1.append(i)
            break  
        
# print(list1)   

list2=[i for i in range(2,100) if i not in list1]
print('prime numbers are',list2)
             
             
#--------------------------------------------------

# use of pass statement
for i in range(10,30):
    if i%2==0:
        pass
    else :
        print(i)
