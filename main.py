# This is a simple application to determine the bargaining positions for negotiating prices
# The rule states that:
# You first need to establish the target price, then
# as a Buyer, you propose offers that are at 65 - 85 - 95 - 100% of the target price
# as a Seller, you propose  offers that are at 135 - 115 - 105 - 100% of the offered price


# Determine the starting position (buyer or seller)

while True:
    try:
        position_type = str(input("Are you a buyer or a seller? Type B or S: "))
    except ValueError:
        continue
    if position_type != "B" and position_type != "S" and position_type != "b" and position_type != "s":
        print(position_type + " is not a known position")
        continue
    else:
        break

target_price = float(input("What is the target price: "))


offer_steps_buyer = [target_price * 0.65, target_price * 0.85, target_price * 0.95, target_price]
offer_steps_seller = [target_price * 1.35, target_price * 1.15, target_price * 1.05, target_price]

def offers_buyer():
    print("First offer: " + str(int(offer_steps_buyer[0])))
    print("Second offer: " + str(int(offer_steps_buyer[1])))
    print("Third offer: " + str(int(offer_steps_buyer[2])))
    print("Fourth offer: " + str(int(offer_steps_buyer[3])))

def offers_seller():
    print("First offer: " + str(int(offer_steps_seller[0])))
    print("Second offer: " + str(int(offer_steps_seller[1])))
    print("Third offer: " + str(int(offer_steps_seller[2])))
    print("Fourth offer: " + str(int(offer_steps_seller[3])))

if position_type == "B":
    offers_buyer()
else:
    offers_seller()










