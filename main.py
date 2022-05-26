import numpy as np
import cv2 as cv

class Band:
    digit = {
        "black" : 0,
        "brown" : 1,
        "red" : 2,
        "orange" : 3,
        "yellow" : 4,
        "green" : 5,
        "blue" : 6,
        "violet" : 7,
        "grey" : 8,
        "white" : 9, 
    }
    multiplier = {
        "black" : 1,
        "brown" : 10,
        "red" : 100,
        "orange" : 1_000,
        "yellow" : 10_000,
        "green" : 100_000,
        "blue" : 1_000_000,
        "violet" : 10_000_000,
        "grey" : 100_000_000,
        "white" : 9,
        "gold" : 0.1,
        "silver" : 0.01
    }
    tolerance = {
        "brown" : 1,
        "red" : 2,
        "green" : 0.5,
        "blue" : 0.25,
        "violet" : 0.10,
        "grey" : 0.05,
        "gold" : 5,
        "silver" : 10
    }

    def justinCase():
        pass

class Resistor:
    def __init__(self, list = None):
        self.numOfBands = len(list)
        self.list = list

    def printFinalResistance(self):
        r, t = self.calculateResistance()
        r = self.updateFinalValue(r)
        print(f"{r}\u03A9 \u00B1{t}%")
    
    def updateFinalValue(self, r):
        if r >= 1_000_000:
            r = r // 1_000_000
            return str(r) + "M"
        elif r >= 1_000:
            r = r // 1_000
            return str(r) + "k"
        else:
            return r


    def calculateResistance(self):
        if self.checkForCorrectBand():
            resistance = ((10 * Band.digit[self.list[0]]) + Band.digit[self.list[1]]) * Band.multiplier[self.list[2]]
            tolerance = Band.tolerance[self.list[3]]
            return resistance, tolerance
        
    def checkForCorrectBand(self):
        if self.list[0] in Band.digit and self.list[1] in Band.digit and self.list[2] in Band.multiplier and self.list[3] in Band.tolerance:
            return True


        


# idea: use opencv and a webcam to recognise a resistor and their respective band colors





def main():
    # implementing a testing image processing features
    pass



main()


