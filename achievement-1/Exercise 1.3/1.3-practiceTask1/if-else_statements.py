a = int(input("Enter a number: "))
b = int(input("Enter another number to be added to the first: "))
operator = input(" Enter '+' for addition or, '-' for substraction: ")

if operator == '+':
    print("The sum of these numbers is " + str(a + b))

elif operator == '-':
    print("The difference of these numbers is " + str(a - b))

else: 
    print("unknown operator")