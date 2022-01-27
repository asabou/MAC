class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__cards = []

    def addCard(self, card):
        self.__cards.append(card)
    
    def setCards(self, cards):
        self.__cards = cards

    def getCards(self):
        return self.__cards

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password
    
    def __str__(self):
        s = "username: " + self.__username + " password: " + self.__password + "\n"
        for card in self.__cards:
            s = s + str(card) + "\n"
        return s + "\n"