# dictionary are used to store values in KEY:VALUE format
# tuples are immutable
# order is not fixed
'''
dict={
    "name" : " harsh"
    "cgpa" : 9.5
    "marks": [88,76,78]
}
'''

dict1={
    "name":"harshvardhan",
    "CGPA": 9.5,
    "marks":[88,76,78]

}

# accessing method
print(dict1["name"])
print(dict1["marks"])

# changing values
dict1["CGPA"]=80.05
print(dict1)

# value inserction

dict1['age']=23
print(dict1)

#-----------------------------------------------------------------------------------------

# nested dictionary
student={
    
    'name':"harshvardhan",
    'class':"1styear",
    # nesting
    'subjects':{
        "phy":75,
        "che":88,
        "marathi":95
    },
    "rank":"topper"
    
}
print(student["subjects"]["phy"])
print(student.keys())
print(student.values())
print(student.items())
print(student.get("phy"))
student.update({'city':'delhi'})
print(student)
student['village']="mane jawalga"
print(student)
new_dict={
    "name":'basude',
    "school":"shreeyash",
    "CGPA":9.4
}
student.update(new_dict)
print(student)
print(new_dict.pop("name"))
