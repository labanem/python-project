#Advanced Calculator version 2
def calculate(num1,num2,operator):
    try:
        if operator == "+":
            return float(num1) + float(num2)
        elif operator == "-":
            return  float(num1) - float(num2)
        elif operator == "/":
            return float(num1) / float(num2)
    except ValueError as err:
        print(err)
        
num1 = input ("Enter value of num1: ")
operator = input("Enter operator: ")
num2 = input("Enter value of num2: ")

print("The answer is: " + str(calculate(num1,num2,operator)))