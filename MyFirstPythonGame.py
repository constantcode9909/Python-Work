# a simple game to take a number from the user and an oepration sign then let him guess the result
# always put the import keyword at the beginning
import random


print("Welcome to the calculator Game" )

# get the user's first number with a validation test
userinput = input("please provide a number:  ")
while userinput.isdigit() == False :
    userinput = input("please provide a valid number  ")


# get the operation sign from the user
useropeartionsign = input("please provide an operation sign:  ")
K = int(userinput)

# print the choice of the computer
computerchoice = random.randrange(K,K*3)
print("The computer chose",computerchoice)

# calculate the true result
useranswer = input("what do you think the result will be?")
if useropeartionsign == "+":
    realanswer = K + computerchoice
elif useropeartionsign == "*":
    realanswer = K * computerchoice
elif useropeartionsign == "-":
    realanswer = K - computerchoice
elif useropeartionsign == "/":
    realanswer = K / computerchoice

# check the real answer and the user's answer
if realanswer == float(useranswer) :
        print('you have won!')
else :
        print("you have lost!")
