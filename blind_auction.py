logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

name= input("What is your name?")
money =int( input("What is your bid?"))

bidding = {}
bidding[name] = money

decision= input("Are there any other bidders? Type 'yes or 'no'.")
while decision.lower() == "yes":
    print("\n"*20)
    name = input("What is your name? ")
    money = int(input("What is your bid? "))

    bidding[name] = money

    decision = input("Are there any other bidders? Type 'yes' or 'no': ")



highest_bid = max(bidding.values())
for bidder in bidding:
    if bidding[bidder] == highest_bid:
        print(f"The winner is {bidder} with a bid of {highest_bid}.")
