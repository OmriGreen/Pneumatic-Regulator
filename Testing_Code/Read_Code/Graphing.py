import math
import numpy as np
import matplotlib.pyplot as plt

from Configuration import Configuration
from Setup import Setup
from Testing import Testing

#Makes graphs utilizing the information from the Testing
class Graphing:
    def __init__(self, pressureIN, pressureOUT, airflowIN, airflowOUT):
        self.pressureIN = pressureIN
        self.pressureOUT = pressureOUT
        self.airflowIN = airflowIN
        self.airflowOUT = airflowOUT

        graphList = [[pressureIN,pressureOUT, 'PvP'],[pressureIN,airflowOUT,'PvA'],[airflowIN,pressureOUT,'AvP'],[airflowIN,airflowOUT,'AvA']]
        #Makes the Graphs

        for graph in graphList:
            plt.plot(graph[0],graph[1], 'o', label='datapoints')

            x = np.array(graph[0])
            y = np.array(graph[1])
            a,b,c,d = np.polyfit(x,y,3)
            plt.plot(x, a*x*x*x + b*x*x + c*x + d, label='line of best fit')
            plt.plot([],[],label = 'f(x) = ' + str(a) + 'x^3 ' + '+ ' +  str(b) + 'x^2 ' + '+ ' + str(c) + 'x ' + str(d))
            plt.legend()
            if graph[2] == ('PvP'):
                plt.ylabel('Pressure Out (MPa)')
                plt.xlabel('Pressure In (MPa)')
                plt.title('Pressure In vs Pressure Out')
                print("SAVE MANUALLY")
                plt.show()
                plt.clf()
            if graph[2] == ('AvA'):
                plt.ylabel('Airflow Out (m/s)')
                plt.xlabel('Airflow In (m/s)')
                plt.title("Airflow In vs Airflow Out")
                print("SAVE MANUALLY")
                plt.show()
                plt.clf()
            if graph[2] == ('PvA'):
                plt.xlabel('Pressure In (MPa)')
                plt.ylabel('Airflow Out (m/s)')
                plt.title('Pressure In vs Airflow Out')
                print("SAVE MANUALLY")
                plt.show()
                plt.clf()
            if graph[2] == ('AvP'):
                plt.xlabel('Airflow In (m/s)')
                plt.ylabel('Presure Out (MPa)')
                plt.title('Airflow In vs Pressure Out')
                print("SAVE MANUALLY")
                plt.show()
                plt.clf()
