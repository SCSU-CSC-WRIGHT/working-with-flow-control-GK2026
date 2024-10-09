#Use random.randint(1, 10) to generate a random number.
#Create a loop that allows the user to guess the number up to 3 times.
#After each guess, tell the user whether their guess is too high, too low, or correct.
#If the user guesses the number or runs out of attempts, print an appropriate message.
#Concepts Used:
#input(), while loop, if-else statement, import random, flow control

import random #Lets us use random 
num=random.randint(1, 10) #Gets the random number
attempts=3 #Sets the number of guesses
count=1 #SET THE ITERATOR 
while count<=attempts: #The while loop  condition
    guess=int(input("Guess a number between 1 and `10: ")) #Gets the users guesses
    if(guess>num):
        print("Your guess is to high") #Tells the user the number is to big
    elif(guess<num):
        print("Your guess is to low") #Tells the user the number is to small
    else:
        print("Your guess is correct") #Tells the user is correct and that they win 
        print ("YOU WIN!!!!!")
        break
    count+=1

else:
    print("You are out of attempts") #Tells the user they are out of attempts
    print("The number was", num)
