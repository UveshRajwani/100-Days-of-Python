print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
split = int(input("How many people to split the bill?"))
answer = (bill_amount/100*tip + bill_amount)/split
print(f"Each person should pay: ${answer}")
