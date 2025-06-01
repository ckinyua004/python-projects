def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

name = input("Enter your name: ")
greeting = input("Enter a greeting (or press Enter for default): ")
if not greeting:
    greeting = "Hello" 
print(greet_user(name, greeting))