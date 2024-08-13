from cards import Card
from ranks import Rank
from suit import Suit
from ranks import Enum



import random
dealer = []
player = []
deck = Card.new_deck()
dPoints = 0
pPoints = 0
def main():
    for i in range(2):
        player.append(random.choice(deck))
    print(player)
    move = (input("Hit or Stand: "))
    while move != "Stand":
        if move == "Hit":
            player.append(random.choice(deck))
            print(player)
            move = input("Hit or Stand: ")
        elif move != "Hit" or "Stand":
            print("invalid input")  
            move = input("Hit or Stand: ")
        elif move == "Stop":
            break
        else:
            break
    dealerChoice = ["Hit", "Stand"]
    for i in range(2):
        dealer.append(random.choice(deck))
    
    while random.choice(dealerChoice) == "Hit":
        dealer.append(random.choice(deck))
    else:
        print("showing dealer's hand")
        print(dealer)

    playerSum = 0
    dealerSum = 0
    for card in dealer:
        dealerSum += card.rank
    print("Dealer had :", dealerSum)
    for card in player:
        playerSum += card.rank
    print("Player had :", playerSum)
    if 21 >= playerSum > dealerSum:
        print("Player wins")
    else: 
        print("Dealer wins")


        
    
    


    

    

if __name__ == "__main__":
    main()