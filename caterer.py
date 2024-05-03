from supplier import Supplier

class Caterer(Supplier):
    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        super().__init__(catererID, name, address, contactDetails)
        self.menu = menu
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def receiveOrder(self, event):
        pass

    def fulfillOrder(self, event):
        pass
