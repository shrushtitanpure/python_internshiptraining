#create dict as personal info

personal_info={
    "Name":"Shrushti",
    "age":"20",
    "city":"ahilyanagar",
    "skills":"Python",
    }
print(personal_info)

#for keys-inwhich only keys are printed
for keys in personal_info.keys():
    print(keys)
    
#For values-in which only values are printed
for values in personal_info.values():
    
    print(values)
    
#for both keys-values USE items-both are printed
for x in personal_info.items():
    
    print(x)

#Add new key email 
personal_info["email"]="shrushti14@gmail.com"
print("\nAdded new key As Email:")
print(personal_info)

# Update city
personal_info.update({"city":"Newasa"})
print("\nUpdated City:")
print(personal_info)

#Delete Age
del personal_info["age"]
print("\nDeleted age:")
print(personal_info)

#Nested dictionary for two students
students = {
    "Student1":{
    
    "Name":"Shrushti",
    "skill":"python",
    },
"Student2":{
    "Name":"Disha",
    "skill":"React JS",
    
    },
    
}
print("\nNested dictionary of students:")
print(students)

#Check if key skills exists
if "skills" in personal_info:
    print("\n'skills' key exists")
else:
    print("\n'skills' key does not exist")

#  Use a loop to print all key–value pairs
print("\nAll key-value pairs:")
for key, value in personal_info.items():
    print(key, ":", value)

