from art import logo
from random import randint

end = False
guess = 0
while not end:
    print(logo)
    number = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    print(number)
    if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == "easy":
        guess = 10
    else:
        guess = 5
    print(f"You have {guess} attempts remaining to guess the number.")

    while guess > 0:
        user_guess = int(input("Make a guess: "))
        if user_guess == number:
            print(f"You got it! The Answer was {number}")
            break
        if user_guess > number:
            guess -= 1
            print("Too High")
            print("Guess Again")
            print(f"You have {guess} attempts remaining to guess the number.")
        if user_guess < number:
            guess -= 1
            print("Too Low")
            print("Guess Again")
            print(f"You have {guess} attempts remaining to guess the number.")
    print("Game Over")
    end = True
    break
