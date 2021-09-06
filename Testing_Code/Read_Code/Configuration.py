import math

#Contains all of the constants
class Configuration:


    #Converts the unit into m
    def UnitConverter(self, radius, radUnit):
        self.radius = radius
        self.radUnit = radUnit


        #If radUnit in millimeters
        if radUnit == 'mm':
            convertedRadius = 0.001 * radius

        #If radUnit in centimeters
        if radUnit == 'cm':
            convertedRadius = 0.01 * radius

        #If radUnit in decimeters
        if radUnit == 'dm':
            convertedRadius = 0.1 * radius

        #If radUnit in meters:
        if radUnit == 'm':
            convertedRadius = radius

        return convertedRadius

    #Finds the Area
    def AreaFinder(self,radius):
        self.radius = radius

        #Does the Calculation
        area = math.pi * radius * radius
        return area

    #Finds a list of the air Pressure at certain points
    def PressureList(self, maxPressure, minPressure, iterPressure):
        self.maxPressure = maxPressure
        self.minPressure = minPressure
        self.iterPressure = iterPressure

        #Makes the list of air Pressure
        pressureList = []
        tempPressure = minPressure
        ifZero = 0

        if minPressure == 0:
            ifZero += 1
        while len(pressureList) < ((maxPressure / iterPressure) + ifZero):
            if len(pressureList) == 0:
                pressureList.append(minPressure)
            else:
                if tempPressure > maxPressure:
                    pressureList.append(maxPressure)
                else:
                    pressureList.append(tempPressure)
            tempPressure += iterPressure

        return pressureList
                

    def __init__ (self):

        #Radius of Tubing in any unit
        radius = 5

        #The Unit used for the radius of the tubing (metric: mm, cm, dm, or m)
        radUnit = 'cm'

        #Density of Fluid kg/m^3
        #Air in this experiment 
        self.fluidDensity = 1.2041

        #Minimum input air pressure in MPa
        minPressure = 0.0

        #Maximum input air pressure in MPa
        maxPressure = 0.100

        #Iteration of air pressure in MPa
        iterPressure = 0.01



        #Calls Unit Converter
        convertedUnit = self.UnitConverter(radius, radUnit)

        #Calls AreaFinder
        area = self.AreaFinder(convertedUnit)
        self.area = area

        #Calls PressureList
        pressureList = self.PressureList(maxPressure,minPressure,iterPressure)
        self.pressureList = pressureList


