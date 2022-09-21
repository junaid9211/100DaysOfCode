from art import logo
import os, platform

def clear():
   if platform.system() == 'Windows':
      os.system('cls')
   else:
      os.system('clear')

# add
def add(n1, n2):
    return n1+n2

# subtract
def subtract(n1,n2):
    return n1-n2

# multiply
def multiply(n1,n2):
    return n1*n2 

# divide
def divide(n1,n2):
    return n1/n2 

operations = {
    '+':add, 
    '-':subtract, 
    '*':multiply, 
    '/':divide
    }



# a recursive function for calculation
def calculation(num1, num2, symbol):
    func = operations[symbol]
    answer = func(num1, num2)
    print(f'{num1} {symbol} {num2} = {answer}')
    continue_calculation = input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ")
    if continue_calculation == 'y':
        new_symbol = input('Pick an operation: ')
        num3 = float(input("What's the next number?: "))
        calculation(answer, num3, new_symbol)
    else:
        clear()
        print(logo)


clear()
print(logo)
while True:
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input('Pick an operation: ')

    num2 = float(input("What's the second number?: "))

    calculation(num1, num2, operation_symbol)

