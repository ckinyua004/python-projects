def add(*args):
    sum = 0
    for n in args:
        sum += n

    return sum

print(add(1, 2, 3, 4,5, 5)) 

def students(name, **kwargs):
    for key, value in kwargs.items():
        print(name ,f"{key} = {value}")


students("Peter", age=20, city="New York", grade="A")