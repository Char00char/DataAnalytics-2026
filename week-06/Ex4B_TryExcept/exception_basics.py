# exception_basics.py


# -----------------------------
# ValueError Example
# -----------------------------
try:
    number = int("hello")

except ValueError:
    print("ValueError: You cannot convert letters into an integer.")

else:
    print(number)

finally:
    print("Let's try another one...\n")


# Another ValueError Example
try:
    age = int(input("Enter your age: "))

except ValueError:
    print("ValueError: Please enter a whole number.")

else:
    print(f"You entered age {age}")

finally:
    print("Let's try another one...\n")


# -----------------------------
# NameError Example
# -----------------------------
try:
    m = banana

except NameError:
    print("NameError: Oops, looks like you used a variable that does not exist.")

else:
    print(m)

finally:
    print("Let's try another one...\n")


# Another NameError Example
try:
    print(score)

except NameError:
    print("NameError: 'score' has not been defined.")

finally:
    print("Let's try another one...\n")


# -----------------------------
# TypeError Example
# -----------------------------
try:
    result = "5" + 5

except TypeError:
    print("TypeError: You cannot add a string and an integer together.")

else:
    print(result)

finally:
    print("Let's try another one...\n")


# Another TypeError Example
try:
    total = len(10)

except TypeError:
    print("TypeError: len() cannot be used on an integer.")

finally:
    print("Let's try another one...\n")


# -----------------------------
# SyntaxError Example
# -----------------------------
try:
    eval("if True print('Hello')")

except SyntaxError:
    print("SyntaxError: Your code syntax is incorrect.")

finally:
    print("Let's try another one...\n")


# Another SyntaxError Example
try:
    eval("for i in range(5) print(i)")

except SyntaxError:
    print("SyntaxError: Missing punctuation or incorrect structure in the code.")

finally:
    print("Let's try another one...\n")