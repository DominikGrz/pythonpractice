# imports
from time import sleep
import math
import os
import sys
import random
from colorama import Fore as F
from colorama import Back as B
from colorama import Style as S

# hide cursor logic
if os.name == 'nt':
    import ctypes

    class _CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]
def hide_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()
def show_cursor():
    if os.name == 'nt':
        ci = _CursorInfo()
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
        ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
    elif os.name == 'posix':
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
hide_cursor()
# clear junk
os.system('clear')
# spacer
print(f" {F.CYAN}")

#!-------------------------------------------------------------------------
#! Blackjack - 21

#returns the next card
def getNextEntry():
    return str(gamestring[0])

#returns the value of the card
def getValue(entry):
    temp = 0
    for i in entry:
        if temp == 1:
            if i in ('Q', 'K', 'J', '1'):
                return [10, 0]
            if i == 'A':
                return [11, 1]
            return [int(i), 0]
                
        if i == " ":
            temp = 1
            
#del pulled card from the deck
def delEntry():
    gamestring.pop(0)

#user chooses what move to make 
def userMove(doubledown):
    sleep(0.5)
    show_cursor()
    while True:
        show_cursor()
        if doubledown == 0:
            action = input(f"Do you {F.BLUE}double down(D){S.RESET_ALL}{F.CYAN}, {F.BLUE}"\
                +f"hit(H){S.RESET_ALL}{F.CYAN}, {F.BLUE}stand(S){S.RESET_ALL}{F.CYAN}?: ")
        else:
            action = input(f"Do you {F.BLUE}hit(H){S.RESET_ALL}{F.CYAN}, {F.BLUE}"\
                +f"stand(S){S.RESET_ALL}{F.CYAN}?: ")
        hide_cursor()
        if action in ('D','d'):
            return action
        if action in ('H','h'):
            return action
        if action in ('S','s'):
            return action

#displays total cards and aces to console
def printNumbers(total,ace,who):
    if who == "Player":    
        print(f"{F.YELLOW}{who}{S.RESET_ALL}{F.CYAN} ➤ {F.LIGHTBLACK_EX}"\
            +str(total)+f"{S.RESET_ALL}{F.CYAN}", end="")
        if ace == 1:
            print(f"{F.LIGHTBLACK_EX}/"+str(total-10)+f"{S.RESET_ALL}{F.CYAN}", end="")
    if who == "Dealer":
        print(f"{F.MAGENTA}{who}{S.RESET_ALL}{F.CYAN} ➤ {F.LIGHTBLACK_EX}"\
            +str(total)+f"{S.RESET_ALL}{F.CYAN}", end="")
        if ace == 1:
            print(f"{F.LIGHTBLACK_EX}/"+str(total-10)+f"{S.RESET_ALL}{F.CYAN}", end="")
    print("")

#displays all cards on hand
def displayCards(cards):
    for i in cards:
        displayOne(i)
    
#display one card
def displayOne(card):
    sleep(0.1)
    if card[0:1] in ("♥","♦"):
        print(f"{F.RED}{B.WHITE} "+ card +f" {S.RESET_ALL}", end=f"{F.CYAN} ")
    else:
        print(f"{F.BLACK}{B.WHITE} "+ card +f" {S.RESET_ALL}", end=f"{F.CYAN} ")
    sleep(0.2)

#fancy turn display
def turnOf(who):
    sleep(0.5)
    if who == "Dealer":
        print(f"{F.MAGENTA}{who}{S.RESET_ALL} {F.CYAN}turn...")
    if who == "Player":
        print(f"{F.YELLOW}{who}{S.RESET_ALL} {F.CYAN}turn...")

#append the players/dealers hand
def appendCardOnHand(card, who):
    if who == "Player":
        thePlayerCards.append(card)
    else:
        theDealerCards.append(card)

#pulls a card
def cardPull(who):
    sleep(0.2)
    print("The "+ who +" pulls: ", end="")
    displayOne(getNextEntry())
    appendCardOnHand(getNextEntry(),who)
    print("")
    delEntry()

#checks for validity of each hand
def r_state(total,ace,who): #round over not chosen
    if total>21 and ace==0:
        return "bust"
    if total==21 and who=="Dealer" and len(theDealerCards)==2:
        return "blackjack"
    if total==21 and who=="Player" and len(thePlayerCards)==2:
        return "blackjack"
    if total==21:
        return "twentyone"
    return r_state2(total,ace,who)

def r_state2(total,ace,who): #round over but chosen
    if total == 17 and who == "Dealer":
        return "s"
    if total>16 and ace==0 and who == "Dealer":
        return "s"
    if total>17 and ace>0 and who == "Dealer":
        return "s"
    if total<21:
        return "inplay"

#check a hand for its values / prints what is total at the end(incl. aces) and returns what
#happens (bust etc)
def checkHand(who):
    sleep(0.35)
    total = 0
    ace = 0
    if who == "Player":
        global player_max
        for card in thePlayerCards:
            hand = getValue(card)
            total += hand[0]
            ace += hand[1]
            if total>21 and ace>0:
                total -= 10
                ace -= 1
            player_max = total
        printNumbers(total,ace,who)
        return r_state(total,ace,who)
    
    if who == "Dealer":
        global dealer_max
        for card in theDealerCards:
            hand = getValue(card)
            total += hand[0]
            ace += hand[1]
            if (total > 21) and (ace>0):
                total -= 10
                ace-= 1
            dealer_max = total
        printNumbers(total,ace,who)
        return r_state(total,ace,who)
#win condition checks
dealer_max = 0
player_max = 0
def checkWin():
    sleep(0.75)
    if (player_max == dealer_max) or ((player_max>21)and(dealer_max>21)):
        return f"{F.LIGHTBLACK_EX}draw!{S.RESET_ALL}{F.CYAN}"
    if 22 > player_max > dealer_max:
        return f"{F.YELLOW}Player{S.RESET_ALL}{F.CYAN} wins!"
    if 22 > dealer_max > player_max:
        return f"{F.MAGENTA}Dealer{S.RESET_ALL}{F.CYAN} wins!"
    if dealer_max > 21 >= player_max:
        return f"{F.YELLOW}Player{S.RESET_ALL}{F.CYAN} wins!"
    if player_max > 21 >= dealer_max:
        return f"{F.MAGENTA}Dealer{S.RESET_ALL}{F.CYAN} wins!"

gameover = False
while gameover is False:  

    #deck
    card = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    variant = ["♣", "♦", "♥", "♠"]

    #reset the game
    gamestring = []
    deckstring = []
    theDealerCards = []
    thePlayerCards = []

    #generate deck
    for i in card:
        for j in variant:
            deckstring.append(str(j+" "+i))

    #generate the whole game
    for i in range(0,6):
        random.shuffle(deckstring)
        gamestring += deckstring

    #gamestart
    turn = "Dealer"
    turnOf(turn)
    cardPull("Dealer")
    cardPull("Dealer")
    dummy = checkHand("Dealer")
    turn = "Player"
    turnOf(turn)
    cardPull("Player")
    cardPull("Player")
    doubledown = 0
    #player starts off
    while (turn == "Player"):
        
        usermove = ""
        status = checkHand(turn)
        if status != dummy == "blackjack":
            print("Dealer blackjack!")
            turn = "Dealer"
            break
        if status == "blackjack":
            print("Player blackjack!")
            turn = "Dealer"
            break
        if status == "twentyone":
            print("Player 21!")
            turn = "Dealer"
            break
        if status == "bust":
            print("Player busts")
            turn = "Dealer"
            break
        if status == "inplay":
            usermove = userMove(doubledown)
        doubledown = 1
        if usermove == "s":
            print("Player stands")
            turn = "Dealer"
            break
        if usermove == "d":
            print("Player double down")
            cardPull(turn)
            turn = "Dealer"
            break
        if usermove == "h":
            print("Player hits")
            cardPull(turn)
        

    #dealers turn
    while turn == "Dealer" and dummy != "blackjack":
        turnOf(turn)
        status = checkHand(turn)
        if status == "inplay":
            cardPull(turn)
        if status == "s":
            print("Dealer stands")
            break
        if status == "blackjack":
            print("Dealer blackjack!")
            break
        if status == "twentyone":
            print("Dealer twentyone!")
            break
        if status == "bust":
            print("Dealer busts")
            break

    #display results
    print("The round is over! Hands:")
    print(f"{F.MAGENTA}Dealer{S.RESET_ALL}{F.CYAN} ➤",end="")
    displayCards(theDealerCards)
    print("")
    print(f"{F.YELLOW}Player{S.RESET_ALL}{F.CYAN} ➤",end="")
    displayCards(thePlayerCards)
    print("")
    result = checkWin()
    print(result)
    sleep(0.6)
    show_cursor()
    playAgain = input("Play again? (default:y/n): ")
    hide_cursor()
    if playAgain not in ["","y","ye","yes"]:
        gameover = True
    os.system('clear')
    print("")

#! todo - compare the hands determine if theres a draw or whot #done
#! todo - player bets (default values, or player specific)
#! todo - upgrade logic to the traditional rules (blackjack 3:2 21 2:1 etc)




# rules: 
# dealer and player pull 2 cards in the beginning
# dealer starts then the player
# the player then needs to be checked firstly for a blackjack (in case of ace + 10) 
# then its dealers turn
#
# if no bj, then the player decides to either double down, stand or hit until he stands busts or 21
# when player is completely done, its dealers turn
# dealer has to pull until atleast 17 and has to be checked if he busts
# at the end the greater <22 hand wins 

# !old bad bad stuff--------------------------------------

#displays the whole game
# def displayStandings():
#     print("DEALER:")
#     print("Cards: ",end="")
#     displayCards(theDealerCards)
#     calcHand(theDealerCards, "Dealer")
#     print("PLAYER:")
#     print("Cards: ",end="")
#     displayCards(thePlayerCards)
#     calcHand(theDealerCards, "Player")

#pulls a card
# def cardPull(who):
#     print("The "+ who +" pulls: ", end="")
#     displayOne(getNextEntry())

#     if who == "Player":
#         thePlayerCards.append(getNextEntry())
#         calcHand(thePlayerCards, who)
#     else:
#         theDealerCards.append(getNextEntry())
#         calcHand(theDealerCards, who)
  
#     delEntry()

# #calculate a hand and print to user
# def calcHand(cards, who):
#     aceCounter = 0
#     handValue = 0
    
#     for i in cards:
#         values = getValue(i)
#         handValue += values[0]
#         aceCounter += values[1]
#     if handValue > 21 and aceCounter != 0:
#         handValue -= 10
#         aceCounter -= 1
#     printPoints(handValue,aceCounter,who)

# #check for bust bj etc
# def checkState(state, who):
#     if state in ("bust","blackjack","stand") and who == "Player":
#         pass
#     elif state ("bust","blackjack","stand") and who == "Dealer":
#         pass


#check for aces and tell user #!needs expansion in case of multiple aces # # wtf did i do here
# def printPoints(value, isAce, who):
#     if value > 21 and isAce == 0:
#         print("total = "+value+" "+who+" BUST!")
#         return "bust", who
#     if value == 21:
#         print("total = "+value+" "+who+" BLACKJACK!")
#         return "blackjack", who
#     if value >= 17 and isAce == 0 and who == "Dealer":
#         print("total = "+value+" "+who+" Stands!")
#         return "stand", who
#     action = userMove()
#     if who == "Player" and action in ("S", "s"):
#         pass
#     if isAce == 1:
#         print("total = "+value)
#         print("/"+str(value-10), end="")
#     print(" ")
#     print("total = "+value+" "+who)
#     return "play", who

print(" ")
