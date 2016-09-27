# Put your code here
import random

print "Hello, welcome to our number guessing game!"
print "What's your name?" 
name = raw_input("----->")

chosen_number = random.randint(1,100)

while True:
	
	guess = int(input("Enter a number: "))

	
	if chosen_number == guess:
		
		print "Congratulations, you guessed the correct number!"
		break

	elif guess>chosen_number:
		print "Guess a lower number than %d" %guess

	else:
		print "Guess a higher number than %d." %guess




