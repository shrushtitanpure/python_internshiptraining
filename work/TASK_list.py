# 1️ Create a list of 5 subjects and print them one by one
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]

print("Subjects list:")
for subject in subjects:
    print(subject)

# 2️ Add a new subject in the middle using insert()
subjects.insert(2, "Computer Science")
print("\nAfter inserting a new subject:")
print(subjects)

# 3️ Remove one subject using remove()
subjects.remove("Biology")
print("\nAfter removing a subject:")
print(subjects)

# 4️ Sort the list alphabetically
subjects.sort()
print("\nAfter sorting alphabetically:")
print(subjects)

# 5️ Create a new list and print squares using list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("\nSquares of numbers:")
print(squares)

# 6️ Create a nested list of students and print the 2nd student’s name
students = [
    ["Rutuja", 20],
    ["Shrushti", 21],
    ["Gita", 22]
]

print("\n2nd student's name:")
print(students[1][0])
