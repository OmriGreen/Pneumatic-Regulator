import nidaqmx as ni
    
import numpy as np

from Configuration import Configuration

#Sets up the sensors used and finds the relationship with the pressure detected vs the voltage output.
class Setup:
    def __init__(self, config):
        self.config = config
        pressureArray = []
        voltageList0 = []
        voltageList1 = []
        voltageList2 = []
        voltageList3 = []


    
 

        #Finds the Voltage for each pressure output by each sensor
        #The + 5 is to make sure all of the data in the voltage lists are positive
        for pressure in config.pressureList:
            print("Press enter when the pressure is at " + str(pressure) + " MPa")
            check = input()
            for x in range(20):
                pressureArray.append(pressure)
                with ni.Task() as task0:
                    task0.ai_channels.add_ai_voltage_chan("Dev1/ai0")
                    voltageList0.append(task0.read())
                with ni.Task() as task1:
                    task1.ai_channels.add_ai_voltage_chan("Dev1/ai1")
                    voltageList1.append(task1.read())
                with ni.Task() as task2:
                    task2.ai_channels.add_ai_voltage_chan("Dev1/ai2")
                    voltageList2.append(task2.read())
                with ni.Task() as task3:
                    task3.ai_channels.add_ai_voltage_chan("Dev1/ai3")
                    voltageList3.append(task3.read())

        #Finds and records the relationship between voltage and pressure for each sensor to the 3rd power 
        #There is a max and min pressure for the sensors

        x = np.array(pressureArray)
        y0 = np.array(voltageList0)
        y1 = np.array(voltageList1)
        y2 = np.array(voltageList2)
        y3 = np.array(voltageList3)

        
        a,b = np.polyfit(y0,x, 1)
        self.sensorAI0 = [a,b]

        a,b = np.polyfit(y1,x, 1)
        self.sensorAI1 = [a,b]

        a,b = np.polyfit(y2,x,  1)
        self.sensorAI2 = [a,b]

        a,b = np.polyfit(y3,x, 1)
        self.sensorAI3 = [a,b]

        print("Set up Complete")
