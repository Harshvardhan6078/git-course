i=1
while i<=100:
    print(i,end=" ")
    i=i+1
print("\nThe end of while loop")

i=100
while i>=1:
    print(i,end=" ")
    i=i-1
print("\nThe end of while loop")

#--------------------------------------------------------------------------------------
list1=[]
i=1
while i<=10:
    print(i**2,end=" ")
    list1.append(i**2)
    i=i+1
print("\n",list1)

#------------------------------------------------------------------------
 
tup=(2,3,5,6,4,7,8,9,0,78,64,68,34,76,78)
i=0
while tup[i]!=78:
    i=i+1
    continue
print(i)

# break and continue