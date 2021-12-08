from art import logo
print(logo)
name = ""
bid = 0
end = False
all_bides = {}
while not end:
    name = input("What is Your Name? ")
    bid = float(input("What is you bif $"))
    all_bides.update({name:bid})
    if input("is there someone else yes or no").lower() == "yes":
        pass
    else:
        highest_bid = 0
        highest_bidder = ""
        for name, bid in all_bides.items():
            if bid > highest_bid:
                highest_bid = bid
                highest_bidder = name
        print(f"{highest_bidder} won the bid with the bid of ${highest_bid}")
        end = True