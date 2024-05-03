class Client:
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

    def viewEventDetails(self):
        pass

    def updateBudget(self, newBudget):
        self.budget = newBudget
