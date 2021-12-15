#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(3,7)
nr_symbols = random.randint(3,7)
nr_numbers = irandom.randint(3,7)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
answer = []
password = ""
for _ in range(0, nr_letters):
    answer.append(random.choice(letters))

for _ in range(0, nr_symbols):
    answer.append(random.choice(symbols))

for _ in range(0, nr_numbers):
    answer.append(random.choice(numbers))

for i in answer:        
    password = password+i
print(f"password: {password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ''
random.shuffle(answer)
for i in answer:
    hard_password = hard_password+i
print(f"Hard password: {hard_password}")
