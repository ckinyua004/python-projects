def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide
}

def calculator():
    continue_calculating = True
    n1 = float(input("Input a number: "))
    while continue_calculating:
        operand = input("Choose an operation: (+ - * /) : ")
        n2 = float(input("Input a number: "))

        if operand == "+":
            output = operations["+"](n1, n2)
            print(f"{n1} {operand} {n2} = {output}")
        elif operand == "-":
            output = operations["-"](n1, n2)
            print(f"{n1} {operand} {n2} = {output}")
        elif operand == "*":
            output = operations["*"](n1, n2)
            print(f"{n1} {operand} {n2} = {output}")
        elif operand == "/":
            output = operations["/"](n1, n2)
            print(f"{n1} {operand} {n2} = {output}")
        else:
            print("Input a valid symbol.")
        
        continue_calculation = input(f"Type Y to continue calculating with {output}. N to start a new calculation. Z to exit: ").lower()
        if continue_calculation == "y":
            n1 = output
        elif continue_calculation == "n":
            continue_calculating = False
            calculator()
        else:
            break

calculator()