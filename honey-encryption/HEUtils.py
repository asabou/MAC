from random import randint
from datetime import date

from Card import Card
from User import User

'''
first 6 digits: BIN (bank identification number)
next 9 digits: OIN (owner identification number) owner account 
last digit: checksum -> Luhm algorithm
'''
class HEUtils:
    def __init__(self, nrCards):
        self.__maxNrCards = nrCards

    def createUser(self, username, password, bins):
        user = User(username, password)
        user.setCards(self.generateCards(bins))
        return user
    
    def generateCards(self, bins):
        nrCards = randint(1, self.__maxNrCards)
        cards = []
        for _ in range(nrCards):
            cardNumber = self.generateCard(self.__getFavoriteBin(bins))
            cardCVC = self.generateCVC()
            cardExpiration = self.generateExpirationDate()
            cards.append(Card(cardNumber, cardExpiration, cardCVC))
        return cards

    def generateCard(self, bin):
        card = ""
        while (len(card) != 16):
            card =  bin + self.__generateOIN()
            for i in range(0,9):
                cc = card + str(i)
                if self.__checksum(cc):
                    card = cc
                    break
        return card

    def generateCVC(self):
        cvc = ""
        for _ in range(3):
            d = randint(0,9)
            cvc = cvc + str(d)
        return cvc
    
    def generateExpirationDate(self):
        currentYear = date.today().year
        month = randint(1, 12)
        month = "0" + str(month) if month < 10 else str(month)
        validity = randint(1, 5)
        year = str(currentYear + validity)
        return month + "/" + year
    
    '''
    Luhm algorithm
    '''
    def __checksum(self, card):
        nDigits = len(card)
        nSum = 0
        isSecond = False
        for i in range(nDigits - 1, -1, -1):
            d = ord(card[i]) - ord('0')
            if (isSecond == True):
                d = d * 2
            # We add two digits to handle
            # cases that make two digits after
            # doubling
            nSum += d // 10
            nSum += d % 10
            isSecond = not isSecond
        return nSum % 10 == 0

    def __generateOIN(self):
        oin = ""
        for _ in range(9):
            d = randint(0,9)
            oin = oin + str(d)
        return oin

    def __generateBIN(self):
        bin = ""
        for _ in range(6):
            d = randint(0, 9)
            bin = bin + str(d)
        return bin
    
    def __getFavoriteBin(slef, bins):
        r = randint(0, 28)
        if (r <= 5):
            return bins[0]
        elif r <= 11:
            return bins[1]
        elif r <= 16:
            return bins[2]
        elif r <= 19:
            return bins[3]
        elif r <= 22:
            return bins[4]
        elif r <= 24:
            return bins[5]
        elif r <= 26:
            return bins[6]
        else:
            return bins[7]

    def generateBINS(self):
        bt = self.__generateBIN()  # 0 - 5
        bcr = self.__generateBIN() # 6 - 11
        brd = self.__generateBIN() # 12 - 16
        rf = self.__generateBIN()  # 17 - 19
        ing = self.__generateBIN() # 20 - 22
        cec = self.__generateBIN() # 23 - 24
        alpha = self.__generateBIN() # 25 -26
        otp = self.__generateBIN() # 27 - 28
        return [bt, bcr, brd, rf, ing, cec, alpha, otp]

    def printCards(self, cards):
        for card in cards:
            print(card)
    