import random
print("Number Guessing Game")
number = random.randint(1,9)
chances=0
print("Guess a number between 1 & 9:")
while chances<5:
    guess = int(input("Enter your guess:-"))
    if guess == number:
        print("CONGRATS YOU WIN!!!")
        break

    elif guess < number:
        print("Your guess was low please guess a higher number", guess)
        
    
    else:
        print("Your guess was high please guess a lower number", guess)
       
    
if not chances< 5:
    print("YOU LOSE!! The number is,")
    print(number)
