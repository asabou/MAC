class Card:
    def __init__(self, number, expiration, cvc): 
        self.__number = number
        self.__expiration = expiration
        self.__cvc = cvc
    
    def getNumber(self):
        return self.__number
    
    def getExpiration(self):
        return self.__expiration

    def getCVC(self):
        return self.__cvc
    
    def __str__(self):
        return "card number: " + self.__number + " expiration: " + self.__expiration + " cvc: " + self.__cvc
 