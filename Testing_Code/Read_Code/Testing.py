import math
import numpy as np
import nidaqmx as ni

from Configuration import Configuration
from Setup import Setup
from Calculation import Calculation

#Tests the device in the system
class Testing:
    def __init__(self, setup, config):
        self.setup = setup
        self.config = config
        eqAI0 = setup.sensorAI0
        eqAI1 = setup.sensorAI1
        eqAI2 = setup.sensorAI2
        eqAI3 = setup.sensorAI3

        airflowIn = []
        airflowOut = []

        pressureIn = []
        pressureOut = []

        #Collects Pressure In and Pressure Out
        for pressure in config.pressureList:
            print("\n Press enter when the pressure is at " + str(pressure) + "MPa")
            check = input()

            for i in range(20):
                #AI0 and AI1 find pressureIn
                with ni.Task() as task0:
                    task0.ai_channels.add_ai_voltage_chan("Dev1/ai0")
                    v0 = float(task0.read())
                    p0 = abs(eqAI0[0]*v0+ eqAI0[1])
                    airflowIn.append(Calculation(p0,config.fluidDensity,config.area).airFlow)
                    pressureIn.append(p0)
                with ni.Task() as task1:
                    task1.ai_channels.add_ai_voltage_chan("Dev1/ai1")
                    v1 = float(task1.read())
                    p1 = abs(eqAI1[0]*v1 + eqAI1[1])
                    airflowIn.append(Calculation(p1,config.fluidDensity,config.area).airFlow)
                    pressureIn.append(p1)

                #AI2 and AI3 find pressureOut
                with ni.Task() as task2:
                    task2.ai_channels.add_ai_voltage_chan("Dev1/ai2")
                    v2 = float(task2.read())
                    p2 = abs(eqAI2[0]*v2 + eqAI2[1])
                    airflowOut.append(Calculation(p2,config.fluidDensity,config.area).airFlow)
                    pressureOut.append(p2)
                with ni.Task() as task3:
                    task2.ai_channels.add_ai_voltage_chan("Dev1/ai3")
                    v3 = float(task3.read())
                    p3 = abs(eqAI3[0]*v3+  eqAI3[1])
                    airflowOut.append(Calculation(p3,config.fluidDensity,config.area).airFlow)
                    pressureOut.append(p3)

        self.pressureIn = pressureIn
        self.pressureOut = pressureOut
        self.airflowIn = airflowIn
        self.airflowOut = airflowOut
        print("\nTESTING COMPLETE")
       



