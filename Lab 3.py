#Ask the user to input a number.
#Use a for loop to sum the numbers from 1 to the user’s input number.
#Print the total sum.

num=int(input("Enter a number: "))#Gets the users input
total=0 #Sets total to 0 
for i in range(1,num): #The for loop i starts at 1 and goes to num
    total+=i#Total adds the i's togeter each time the loop goes through 
print(total)#Prints the total 