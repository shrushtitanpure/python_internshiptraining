def square(num):
    return num * num

print(square(5))



def max_of_three(a, b, c):
    return max(a, b, c)

print(max_of_three(10, 25, 15))





def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))





def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(7))




def table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

table(5)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Shrushti"))

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)



def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Shrushti")




def sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg

s, a = sum_and_average([10, 20, 30])
print("Sum:", s)
print("Average:", a)





def total_marks(*marks):
    return sum(marks)

print(total_marks(80, 75, 90, 85))

