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
operation = input(
    f"Which operation do you want?\n {newstring.join(calc_dict.keys())}\n")
num2 = int(input("What is the second number? "))
result = calc_dict[operation](num1,num2)
print(f'{num1} {operation} {num2} = {result}')
keep_going = False
go = input("Keep going? Press any key + enter to keep going, or enter to quit")
if go:
    keep_going = True
else:
    

while keep_going = True:

num3 = int(input("What's the next number? \n"))