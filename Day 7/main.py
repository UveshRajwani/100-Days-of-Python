import random
from art import logo,stages
from words import word_list

end_game = False
life = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(logo)


# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while end_game == False:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        life -= 1
        print(stages[life])
    if life <= 0:
        end_game = True
        print("You Lose")
    if "_" not in display:
        end_game = True
        print("You win")

