# ## **Recap**

# - Comments → Make code readable
# - Variables → Store values (dynamic typing)
# - Identifiers → Naming rules
# - Data Types → int, float, str, list, tuple, dict, bool, None
# - Escape Sequences → `\n`, `\t`, `\"`

# ### **Type Casting (Type Conversion)**

# Convert one type into another:

# ##``python
# int()
# float()
# str()
# bool()

# ```

# Example:

# #python
# x = "5"
# print(int(x) + 5)

# ## **String Concatenation**

# String concatenation simply means **joining two or more strings together**.

# Python gives multiple ways to join strings:

# ---

# ### ✅ **1. Using `+` (String Concatenation Operator)**

# The `+` operator joins **only strings**.

# ### ✅ Example:

# #python
# name="John"
# print("Your Name Is " , name)

# first = "Hello"
# second = "World"
# print(first + " " + second)



# #Output:Hello World



# ### ✅ **2. Using Comma ( , ) inside `print()`**

# Comma is very useful when printing **multiple values**.

# ### ✅ Python automatically:

# ✔ Adds a space

# ✔ Converts numbers → string automatically

# ### Example:

# #python
# # name = "Pratik"
# # age = 24

# # print(name,age)
# # # or
# # print("Name:", name, "Age:", age)



# ✅ Output:
# Name: Pratik Age: 24


# ### ✅ Why is comma better sometimes?

# - No type errors
# - Faster to write
# - More readable for beginners


# ## **Using f-Strings (Most Recommended)**

# # **f-strings** (formatted string literals) are the **modern, fastest, and cleanest** way to combine text and variables in Python.

# # Just add **`f`** before the string and place variables inside **`{ }`**.

# # ### Example:

# # ```python
# # name = "Pratik"
# # age = 24
# # print(f"My name is {name} and I am {age} years old.")

# # ```

# # ✅ Output:


# # My name is Pratik and I am 24 years old.



# # 👉 No need to convert `age` to string.

### **4. Using `.format()` Method**

# Older but still used.

# ### Example:

# ```python
# print("Welcome {}, year {}".format("Pratik", 2025))

# ```

# ---

# ## ✅ **Quick Summary**

# - **`+` → joins only strings (needs conversion)**
# - **`,` → joins any value inside print (auto conversion)**
# - **`f"{}"` → best, clean, modern**
# - **`.format()` → older method but work**

# ```python

# ```

# ---

# ### **Small Memory Concept**

# Every variable points to a memory location.

# ```python
# a = 5
# b = a
# print(id(a), id(b))

# ```

# ✅ Same ID means both variables point to same memory.

# ⚠️ If value changes → new memory is created.

# ---

# ### ✅ **Constants in Python**

# Python does NOT have true constants.

# Rule:

# Use capital letters when you *want* to treat something as constant:

# ```python
# PI = 3.14
# ```