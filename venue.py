class Venue:
    def __init__(self, venueID, name, address, contactDetails, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    def checkAvailability(self, date, time):
        pass

    def bookVenue(self, date, time):
        pass
