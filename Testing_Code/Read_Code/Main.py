from Configuration import Configuration
from Graphing import Graphing
from Setup import Setup
from Testing import Testing

#Main class, press Run to Run the program
class Main:
    def __init__(self):
        config = Configuration()
        setup = Setup(config)
        testing = Testing(setup, config)
        Graphing(testing.pressureIn, testing.pressureOut, testing.airflowIn, testing.airflowOut)

Main()
