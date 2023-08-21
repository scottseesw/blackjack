
import random

suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

cards_values = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


def generateDeck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
    random.shuffle(deck)
    return deck



def getCardValue(card):
    key = card[0]
    value = cards_values[key]
    return value

def turn(deck, current_score):
    card = deck.pop(0)
    print(">> ", card)
    cardValue = getCardValue(card)
    new_score = current_score + cardValue
    print("Score: ", new_score)
    return new_score

def playGame():

    
    deck = generateDeck()
    dealerScore = 0
    playerScore = 0

    print("------------------Dealers Hand --------------------")
    dealerScore = turn(deck, dealerScore)
    dealerScore = turn(deck, dealerScore)
    print("Dealers score: ", dealerScore)

    print("--------------------Players Hand----------------------")
    playerScore = turn(deck, playerScore)
    playerScore = turn(deck, playerScore)
    print("Your score:", playerScore)

    keepPlaying = True
    while keepPlaying:
        userChoice = input("HIT or STAND: ")
        if userChoice == "HIT":
            playerScore = turn(deck, playerScore)
            print("Your total: ", playerScore)
            print("Dealer total: ", dealerScore)
            if playerScore > 21:
                print("----------------You bust, dealer wins!----------------")
                keepPlaying = False
        elif userChoice == "STAND":
            print("----------------Dealers Hand------------------------")
            dealerScore = turn(deck, dealerScore)
            print("Your total: ", playerScore)
            print("Dealer total: ", dealerScore)
            if dealerScore > 21:
                print("--------------DEALER BUSTS!!!, YOU WIN!!!!-----------------")
            elif dealerScore == playerScore:
                print("--------------------TIE!!!!!!!---------------------------")
            elif dealerScore > playerScore:
                print("-------------YOU LOSE!, DEALER WINS!!!!--------------------")
            else:
                print("------------DEALER LOSES, YOU WIN!!!!!!--------------------")
            keepPlaying = False
        else:
            print("Please enter a valid input: 'HIT' or 'STAND'")

playGame()
