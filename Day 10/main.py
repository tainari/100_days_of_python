#sorry, the secret auction seemed super boring so I skipped it
#this one is creating a calculator. Huzzah!
from art import logo

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

def exponent(n1,n2):
    return n1 ** n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": exponent
}

print(logo)
newstring  = "\n"
num1 = int(input("What is the first number? "))
operation = input(f"Which operation do you want? Options: {' '.join(calc_dict.keys())}\n")
num2 = int(input("What is the second number? "))
result = calc_dict[operation](num1,num2)
print(f'{num1} {operation} {num2} = {result}')
keep_going = input(
    "Keep going? Type yes to do another calculation. Type no to quit.\n").lower()
keep_going = True if keep_going == 'yes' else False

while keep_going == True:
    num3 = int(input("What's the next number? \n"))
    operation = input(
        f"Which operation do you want? Options: {' '.join(calc_dict.keys())}\n")
    #note to self: you can join with a newstring by using newstring.join(list)
    # operation = input(f"Which operation do you want?\n {newstring.join(calc_dict.keys())}\n")
    new_result = calc_dict[operation](result, num3)
    print(f'{result} {operation} {num3} = {new_result}')
    result = new_result
    keep_going = input(
        "Keep going? Type yes to do another calculation. Type no to quit.\n").lower()
    keep_going = True if keep_going == 'yes' else False

print("Goodbye.")