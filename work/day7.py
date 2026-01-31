#MATCH_CASE
#Used to handle multiple cases at same time
#handle multiple operations at a same time

#syntax




######CALUTATOR
##a=int(input("enter no" ))
#int(input("enter no2"))

#print("Addition ",a+b)
######################TASK

#day = input("Enter a day: ")

sum = 0

for i in range(1, 51):
    if i % 2 == 0:
        sum = sum + i

print("Sum of even numbers between 1 and 50 is:", sum)
###################################################


no=int(input("enter the number"))




data=[20,40,60,100,30,"OM","Aditya","Sanmesh",True,None,23.5]

# Membership Operator

# in and not in= check whether element is present or not
print("OM" in data) # True
print("ABC" not in data) # True


# Identity Opertor
# is and is not- check whether same object memory or not


a=10
b=a
c=[10,20,30]
print(a is b)
print(a is c) # False
print(a is not b) # False
