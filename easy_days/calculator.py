from art import calculator_logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
use_result = False
result = None
while True:
    if use_result:
        n1 = result
    else:
        n1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")[0]
    n2 = float(input("Enter second number: "))
    if operator in calculator_dict.keys():
        result = calculator_dict[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")
    use_result = input(f"Type 'y' to continue calculating with {result} or type n to start again: ").lower()[0] == 'y'
