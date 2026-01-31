#tuple of 5 colours
colors=("blue","orange","yellow","pink","white")
print(type(colors))
for colors in colors:
    print(colors)
    
#update value
# colors[1]="red"
# print(colors)

#TypeError: 'tuple' object does not support item assignment
#Tuples are immutable, so their values cannot be changed after creation.
#print(type(colors))

colours = ("Red", "Blue", "Green", "Yellow", "Purple")
print("Middle values of the tuple:")
print(colours[1:3])


tuple_1=("apple","banana","apple")
print(tuple_1.count("apple"))

#unpack Tuple
no=(20,30,40)
no1,no2,no3=no
print(no1)


###nested
# Create a nested tuple
nested_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
