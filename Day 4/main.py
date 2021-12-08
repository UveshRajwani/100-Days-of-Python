from random import randint
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
actions = [rock, paper, scissors]
comp = randint(0, 2)
print(actions[user])
print(actions[comp])
if user == comp:
    print("You Tied")
if user == 0 and comp == 1 or user == 1 and comp == 2 or user == 2 and comp == 0:
    print("You Lose")
if user == 0 and comp == 2 or user == 1 and comp == 0 or user == 2 and comp == 1:
    print("You Win")
