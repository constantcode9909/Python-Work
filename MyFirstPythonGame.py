# a simple game to take a number from the user and an oepration sign then let him guess the result
print("Welcome to the calculator Game" )
userinput = input("please provide a number:  ")
while userinput.isdigit() == False :
    userinput = input("please provide a valid number  ")
useropeartionsign = input("please provide an operation sign:  ")
import random
K = int(userinput)
computerchoice = random.randrange(K,K*3)
print("The computer chose",computerchoice)
useranswer = input("what do you think the result will be?")
if useropeartionsign == "+":
    realanswer = userinput + computerchoice
    if realanswer == useranswer :
        print('you have won!')
    else :
        print("you have lost!")
elif useropeartionsign == "*":
    realanswer = userinput * computerchoice
    if realanswer == useranswer :
        print('you have won!')
    else :
        print("you have lost!")
elif useropeartionsign == "-":
    realanswer = userinput - computerchoice
    if realanswer == useranswer :
        print('you have won!')
    else :
        print("you have lost!")
elif useropeartionsign == "/":
    realanswer = userinput / computerchoice
    if realanswer == useranswer :
        print('you have won!')
    else :
        print("you have lost!")
