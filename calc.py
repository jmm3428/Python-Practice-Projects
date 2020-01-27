"""
Calculator trial
"""
print("Welcome to Jimmie's dopeass calculator")
print("Please put on your head condom so you don't catch and STDs during this mindfuck")
print("You ready to get going?")
num1 = float(input("Gimme that first number of yours:"))
print ("Nice choice, what you feelin like doing with it? Type one of the numbers below")
user_input=input("1.Add 2.Subtract 3.Multiply 4.Divide :")
if user_input == "1":
    num2 = float(input("Enter another number:"))
    result = str(num1+num2)
    print("The answer is" + result)
if user_input == "2":
    num2 = float(input("Enter another number:"))
    result = str(num1-num2)
    print("The answer is" + result)
if user_input == "3":
    num2 = float(input("Enter another number:"))
    result = str(num1*num2)
    print("The answer is" + result)
if user_input == "4":
    num2 = float(input("Enter another number:"))
    result = str(num1/num2)
    print("The answer is" + result)
print("We all done here, or we need to keep it goin?")
feedback = input("Type proceed to continue :")
num1 = float(result)
if feedback == "proceed":
    print ("Nice choice, what you feelin like doing with it? Type one of the numbers below")
    user_input=input("1.Add 2.Subtract 3.Multiply 4.Divide :")
    if user_input == "1":
        num2 = float(input("Enter another number:"))
        result = str(num1+num2)
        print("The answer is" + result)
    if user_input == "2":
        num2 = float(input("Enter another number:"))
        result = str(num1-num2)
        print("The answer is" + result)
    if user_input == "3":
        num2 = float(input("Enter another number:"))
        result = str(num1*num2)
        print("The answer is" + result)
    if user_input == "4":
        num2 = float(input("Enter another number:"))
        result = str(num1/num2)
        print("The answer is" + result)
    elif feedback != "proceed":
        print("Way to go Mathtermind")
print("We all done here, or we need to keep it goin?")
feedback = input("Type proceed to continue :")
if feedback != "proceed":
        print("Way to go Mathtermind")
