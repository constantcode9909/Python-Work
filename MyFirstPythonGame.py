# a simple game to take a number from the user and an oepration sign then let him guess the second number after showing the result
# current problem how to make the computer check the data type of the user input properly
print("Welcome to the calculator Game")
userinput = input("please provide a number")
try :
    int(userinput)
except :
    print("please give a valid number")
    userinput = input("please provide a number")
else:
    useropeartionsign = input("please provide an operation sign")
    import random
    print(random.randrange(int(userinput)))
