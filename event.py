class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venueAddress = venueAddress
        self.client = None
        self.guests = []
        self.venue = None
        self.suppliers = []

    def addGuest(self, guest):
        self.guests.append(guest)

    def assignSupplier(self, supplier):
        self.suppliers.append(supplier)

    def generateInvoice(self):
        pass
