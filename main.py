from socket import SO_ERROR


class Resistor:
    def __init__(self, list = None):
        self.numOfBands = len(list)
        self.list = list


    def printEachBandInputted(self):
        for index, color in enumerate(self.list):
            print(index, color)

    def calculateResistance(self):
        resistorDict = {
            "black" : [0, 0, 0, 0, None, "250 ppm/K"],
            "brown" : [1, 1, 1, 1, u"\u00B11%(F)", "100 ppm/K"],
            "red" : [2, 2, 2, 2, u"\u00B12%(G)", "50 ppm/K"],
            "orange" : [3, 3, 3, 3, None, "15 ppm/K"],
            "yellow" : [4, 4, 4, 4, None, "25 ppm/K"],
            "green" : [5, 5, 5, 5, u"\u00B10.50%(D)", "20 ppm/K"],
            "blue" : [6, 6, 6, 6, u"\u00B10.25%(C)", "10 ppm/K"],
            "violet" : [7, 7, 7, 7, u"\u00B10.10%(B)", "5 ppm/K"],
            "grey" : [8, 8, 8, 8, u"\u00B10.05%", "1 ppm/K"],
            "white" : [9, 9, 9, 9, None, None],
            "gold" : [None, None, None, -1, u"\u00B15%", None],
            "silver" : [None, None, None, -2, u"\u00B110%", None],
        }
        output = ""









def main():
    input = ["brown", "black", "brown"]
    resistor1 = Resistor(input)
    resistor1.calculateResistance()



main()


