import art

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

def calculator():

    print(art.logo)

    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)

    should_continue = True

    while should_continue:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        checker = input(f"Type 'y' to coninue calculating with {answer}, or type 'n' to start a new calculation: ")

        if checker == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

