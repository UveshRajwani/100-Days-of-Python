############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
end = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while not end:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
        pass
    else:
        end = True
    print(logo)
    game_over = False
    user_score = 0
    user_cards = []
    comp_score = 0
    comp_cards = []
    while not game_over:
        for _ in range(0, 2):
            user_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))
        for card in user_cards:
            user_score += card
        for card in comp_cards:
            comp_score += card
            if comp_score <= 16:
                comp_cards.append(random.choice(cards))
        while not game_over:
            print(f"Your Cards: {user_cards}, current score = {user_score}")
            print(f"Computer's first card: {comp_cards[0]}")
            if input("Type 'y' to get another card, type 'n' to pass:") == "y":
                new_card = random.choice(cards)
                user_cards.append(new_card)
                user_score +=new_card
            else:
                print(f"Your Cards: {user_cards}, current score = {user_score}")
                print(f"Computer's Cards: {comp_cards},Computer's score = {comp_score} ")
            if user_score == comp_score:
                print("you tied")
                game_over = True
                break
            if user_score > 21:
                print("You went over. You lose 😭")
                game_over = True
                break
            if comp_score > 21:
                print("you win")
                game_over = True
                break
            if user_score < 21 and user_score > comp_score:
                print("you win")
                game_over = True
                break
            if user_score < 21 and user_score < comp_score:
                print("you lose")
                game_over = True
                break


