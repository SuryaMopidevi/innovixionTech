import random

def NumberGuess(compNum):
    count=1
    while count<4:
        try:
            print(f"Chance number : {count}")
            userGuess = input("Guess Number : ")
            userGuess = int(userGuess)
            pin=1
            if userGuess >= 0:
                if userGuess == compNum :
                    pin=0
                    break

            else:
                print("Invalid input. Please enter a numeric value between 0-10 only")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

        count+=1
    if pin==0:
        print(f"Congo you guessed the number")
    else:
        print(f"You lost ")



print(f"Guess number between 0-10 within 3 times.")
compNum=random.randrange(10)
NumberGuess(compNum)
