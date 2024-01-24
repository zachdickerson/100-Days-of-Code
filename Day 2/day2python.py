'''
Data Types

#String
"Hello"[1] = e
print('123' + '456') = '123456'

#Integers

They can be separated like this 123_456_789 = 123456789

PEMDAS - unlike pemdas Multiplation, Division and Addition and Subtraction are equal, but it is read left to right
for what comes first. So if 3 / 3 * 3 then the division is first.
()
**
* /
+ -

'''
print("Welcome to the tip calculator.")
total = float(input('What was the total bill? $'))
percent = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

percent_price = total * (percent/100)

total_tip = total + percent_price

the_split = round(total_tip / people,2)

print(f'Each person should pay: ${the_split}')

