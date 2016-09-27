# Put your code here
import random

def game():

    print "Hello, welcome to our number guessing game!"
    print "What's your name?" 
    name = raw_input("----->")

    chosen_number = random.randint(1,100)
    #print chosen_number
    count = 0
    while True:

  
        try:
            guess = int(input("Enter a number: "))
        except NameError:
            print "You Silly Goose! Enter a valid number from the range 1 to 100"
            continue

        if guess < 1 or guess > 100:
            print "You Silly Goose! Enter a valid number from the range 1 to 100."
            continue

        elif chosen_number == guess:
            count = count + 1

            print "Congratulations, you guessed the correct number! You've guessed in %d tries!" % count

            print "Do you want to play another game? yes/no: "
            response = raw_input(">>>>>" )
            if response.lower() == "yes":
                game()
            elif response.lower() == "no":
                break
            else:
                print "Not a valid response, you are now exiting the game."    
                break
        elif guess > chosen_number:
            count = count + 1
            print "Guess a lower number than %d" % guess
            

        else:
            count = count + 1
            print "Guess a higher number than %d." % guess
        
            
game()
