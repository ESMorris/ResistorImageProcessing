from socket import SO_ERROR


class Resistor:
    def __init__(self, list = None):
        self.numOfBands = len(list)
        self.list = list


    def printEachBandInputted(self):
        for index, color in enumerate(self.list):
            print(index, color)

    def calculateResistance(self):
        pass


    def updateValue(self):
        r, t = self.calculateResistance()


        








def main():
    input = ["brown", "black", "brown"]
    resistor1 = Resistor(input)
    resistor1.calculateResistance()



main()


