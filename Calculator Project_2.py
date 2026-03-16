def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Enter 'A' for addition")
print("Enter 'S' for subtraction")
print("Enter 'M' for multiplication")
print("Enter 'D' for division")



while True:
    choice= input("Enter choic (A,S,M,D):")
    
    if choice.upper () in ('A','ADD','ADDITION','S','SUBTRACT', 'SUBTRACTION','M','MULTIPLY','MULTIPLICATION','D','DIVIDE','DIVISION'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    if choice.upper() in ('A','ADD','ADDITION'):
            print('Result:' ,(num1, '+', num2, '=', add(num1,num2))
                
    elif choice.upper() in ('S','SUBTRACT', 'SUBSTRACTION'):
            print('Result:',(num1, '-', num2, '=', subtract(num1,num2))
                
    elif choice.upper() in ('M','MULTIPLY','MULTIPLICATION'):
            print('Result:',(num1, '*', num2, '=', multiply(num1,num2))
                
    elif choice.upper() in ('D','DIVIDE','DIVISION'):
            print('Result:',(num1, '/', num2, '=', divide(num1,num2))
                
else:
    print("Please input a correct choice")

next_calculation =input("Want toi do another calculation? (yes/no?): ")
if next_calculation.lower() in ('no','n','nope'):
    break