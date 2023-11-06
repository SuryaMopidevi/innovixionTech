import random

# function for guessing game 
def NumberGuess(compNum):
    # initialising limit 
    count,pin=1,1
    while count<4:
        try:
            print(f"{count})" ,end="")
            # number guessing 
            userGuess = input("Guess Number : ")
            userGuess = int(userGuess)
            if userGuess >= 0:
                if userGuess == compNum :
                    pin=0
                    break
            else:
                # message for invalid numerical input 
                print("Invalid input. Please enter a numeric value between 0-10 only")
        except ValueError:
            # message for invalid input (other than numeric value)
            print("Invalid input. Please enter a numeric value.")
        count+=1

    # output generation 
    if pin==0:
        print(f"Congo you guessed the number")
    else:
        print(f"Computer Number : {compNum}")
        print(f"You lost ")



print(f"Guess number between 0-10 within 3 times.")
compNum=random.randrange(10)
NumberGuess(compNum)

