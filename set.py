# set in python {}
# set is a collection of unique elements
# set is an unordered collection
# set is an not iterable
# neglect the duplicate elements
# set is an mutable data type
# indexing and slicing is not possible
# set is an unordered collection
set1={1,2,3,4,5}
print(set1)
set1.add(6)
print(set1)

# operatins on sets
set1.update({7,8,9}) #add multiple elements
set1.remove(8) #remove an element
print(set1)
#set1.clear() #remove all elements
#print(set1)

# we can perform various operations on set
# add, remove,clear, pop
#set is an unordered collection
# set is an iterable
 # we ca add  boolean, float,complex, tuple, string ,int in set
 # BUT we cant add list, dictionary in set
 
# empyt set
empty_set=set()
print(len(set1))

# set union and intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)