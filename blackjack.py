firstHand = int(input('Enter the value of the first hand: '))
secondHand = int(input('Enter the value of the second hand: '))

def validBlackjackHand(hand):
    return hand > 0 and hand <= 21

listOfHands = [firstHand, secondHand]
sortedListOfHands = sorted(listOfHands, reverse=True)
filtered = list(filter(validBlackjackHand, sortedListOfHands))
if len(filtered) == 0:
    print(0)
else:
    print(filtered[0])
