from QueueADT import *
from random import randint

class Passenger:
    def __init__(self, pID, ArrivalTime):
        self._pID = pID
        self._arrivalTime = ArrivalTime


    def getPID(self):
        return self._pID

    # Return Arrival Time
    def timeArrived(self):
        return self._arrivalTime


class TicketAgent:
    def __init__(self, aID):
        self._aID = aID
        self._passenger = None
        self._stopTime = -1

    def getAID(self):
        return self._aID

    # Determine if Agent is Free
    def isFree(self):
        return self._passenger is None

    def isFinished(self, CurrentTime):
        return self._passenger is not None and CurrentTime == self._stopTime

    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger


class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # parameters supplied by the user











