from art import logo, vs
from random import randint
from game_data import data
end = False
names = []
follower_counts = []
descriptions = []
countrys = []
for info in data:
    names.append(info["name"])
    follower_counts.append(info["follower_count"])
    descriptions.append(info["description"])
    countrys.append(info['country'])
while not end:
    index1 = randint(0, 50)
    index2 = randint(0, 50)
    if index1 == index2:
        index2 = randint(0, 50)
    score = 0
    game_end = False
    while not game_end:
        if score <= 0:
            pass
        else:
            print(f"You're right! Current score: {score}.")
        print(f"Compare A: {names[index1]}, {descriptions[index1]}, from {countrys[index1]} .")
        print(vs)
        print(f"Compare B: {names[index2]}, {descriptions[index2]}, from {countrys[index2]}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == "a" and follower_counts[index1] >= follower_counts[index2] or guess == "b" and follower_counts[index1] <= follower_counts[index2]:
            print("noice")
            score += 1
            if follower_counts[index1] <= follower_counts[index2]:
                index1 = index2
                index2 = randint(0, 50)
            else:
                index2 = randint(0, 50)
        else:
            game_end = True
            end = True
            break
