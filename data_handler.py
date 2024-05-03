import pickle

class DataHandler:
    @staticmethod
    def saveData(data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def loadData(filename):
        with open(filename, 'rb') as file:
            data = pickle.load(file)
        return data
