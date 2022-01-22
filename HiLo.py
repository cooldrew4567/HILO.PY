#Author: Andrew Jones
#Assignment: Make a HiLo game

import random



class Deal:
    def __init__(self):
        # default score
        self.score = 300
        self.cards = []

    def getScore(self):
        return self.score
    def newCard(self):
        card = random.randint(1,13)
        self.cards.append(card)
        return card
        #Points that can be earned depending on if player is correct or wrong
    def compare(self,guess):
        prevScore = self.cards[len(self.cards)-2]
        curScore = self.cards[len(self.cards)-1]
        if curScore >= prevScore and guess == 'H':
            self.score = self.score + 100
        elif curScore < prevScore and guess == 'L':
            self.score = self.score + 100
        else:
            self.score = self.score - 75

class Hilo:
    def __init__(self):
        pass
#game code below
    def start(self):
        deal = Deal()
        card = deal.newCard()
        while deal.getScore() > 0:
            print("The card is: ",card)
            guess = input("Higher or lower? [H/L]").lower()
            card = deal.newCard()
            deal.compare(guess)
            print("Your card was ")
            print("Your score is: ",deal.getScore())
            choice = input("Keep playing? [Y/N]").lower()
            if choice == 'N':
                 print("Thanks for playing!")
            return

if __name__ == "__main__":
    game = Hilo()
    game.start()
