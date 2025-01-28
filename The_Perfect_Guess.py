import random

randno = random.randint(1, 100)
user_guess = None
guesses = 0

while (user_guess != randno):
    user_guess = int(input("Enter any number bw 1 to 100 : "))
    guesses +=1
    if (user_guess==randno):
        print("You guessed it right!!")
    else:
        if user_guess>randno:
            print("You guessed it wrong! Enter smaller number")
        else:
            print("You guessed it wrong! Enter larger number")

print(f"You guessed the number in {guesses} guesses.")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if (guesses<hiscore):
    print("You have broken the hiscore!!")
    with open("hiscore.txt","w") as f:
        f.write(str(guesses))

