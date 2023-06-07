# Today Dr. Yu was more interactive with what the calculator should look like
# Answer is more or less the exact same as hers.


from art import logo
#addition
def add(n1, n2):
  return n1 + n2

#Subtraction
def subtract(n1, n2):
  return n1 - n2

#Multiplaction
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():

  print(logo)

  num1 = float(input("What's the first number? "))
  for item in operations:
      print(item)
  should_continue = True
  
  while should_continue:
  
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the second number? "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
      
    print(f'{num1} {operation_symbol} {num2} = {answer}')
  
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to continue with new calculation : ") == 'y':
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
  