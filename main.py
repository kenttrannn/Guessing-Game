#Kent Tran, Viktor Silaie
#August 26, 2025
#Lab #1, Randomized Number Guessing Game
import check_input
import random
def main():
    print("- Guessing Game -")
    randomizedNumber = random.randint(1, 100) #creates a random number and stores it under randomizedNumber
    guessCount = 0
    guess = 0
    #print(randomizedNumber) #for testing purposes
    
    while (guess != randomizedNumber):#checking if the guess is right
        guess = check_input.get_int_range("I'm thinking of a number. Make a guess (1-100): ", 1, 100)
        if (guess < randomizedNumber):
            print("Too low")
            guessCount += 1
        elif (guess > randomizedNumber):
            print("Too high")
            guessCount += 1
        else:
            guessCount += 1
            if guessCount == 1:
                print("Correct! You got it in " + str(guessCount) + " try")
            else:
                print("Correct! You got it in " + str(guessCount) + " tries")
            

main()
