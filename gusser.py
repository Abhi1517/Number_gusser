import random as rn
a = int(input(print("ENTER A GUESS FROM 1 TO 100: ")))
n = rn.randint(1,100)
s = 0
while(a != n):
    s +=1
    if(a > n):
        print("Please guess the smaller number")
    elif(a<n):
        print("Please guess the higher number") 
    a = int(input(print("Enter the number:")))
 
print(f"""Congradulation you Guess the correct answer
    Your no.of guesses is '{s}'""")
print("Thanks for playing")