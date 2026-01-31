
# age calculator
# raise- your own error

try:
    age=int(input("Enter Your Age..."))

    def Demo(a):
        if a<=0:
            raise ValueError("Age cannot be negavtive...")
        
        print("Your Age Is ",a)


    Demo(age)

except Exception as e:
    print("Error", e)





# try:
#     a=20
#     b="name"
#     print(a+b)
# except:
#     print("Errror occured")
    
    
try:
    def calci(a,b):
         return a/b
    print(calci(5,5))
    res=(calci(50,0))
    print(res)
except Exception as err:
    print("error occured",err)
    
    
print("hello")





# try:
#     num=int(input("enter number:"))
# except ValueError

try:
    username = input("Enter username: ")

    if username == "":
        raise ValueError("Username cannot be empty")

    if len(username) < 4:
        raise ValueError("Username must be at least 4 characters long")

    if " " in username:
        raise ValueError("Username must not contain spaces")

    print("Valid username:", username)

except ValueError as e:
    print("Error:", e)

