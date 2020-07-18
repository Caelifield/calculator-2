"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def calculator():
    while True:
        input_string = input('Enter string:')
        token = input_string.split(' ')
        oper = token[0]
        try:
            num1 = token[1]
        except:
            num1 = token[0]
        try:
            num2 = token[2]
        except:
            num2 = token[0]
    #token is a list
        if oper == 'q':
            quit()
        elif oper == "+":
            print(add(int(num1),int(num2)))
        elif oper == "-":
            print(subtract(int(num1),int(num2)))
        elif oper == "*":
            print(multiply(int(num1),int(num2)))
        elif oper == "/":
            print(divide(int(num1), int(num2)))
        elif oper == "square":
            print(square(int(num1)))
        elif oper == "cube":
            print(cube(int(num1)))
        elif oper == "pow":
            print(power(int(num1),int(num2)))
        elif oper == "mod":
            print(mod(int(num1),int(num2)))
        

calculator()