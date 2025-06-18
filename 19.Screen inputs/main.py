def add(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def calculator(n1, n2 ,func):
    return func(n1, n2)

result = calculator(9, 3, add(2, 3))
print(result)