from QueueADT import *
from random import randint

class Passenger:
    def __init__(self, pID, ArrivalTime):
        self._pID = pID
        self._arrivalTime = ArrivalTime

    def getPID(self):
        return self._pID

    # Return Arrival Time
    def getTimeArrived(self):
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

    def isFinished(self, currentTime):
        return self._passenger is not None and currentTime == self._stopTime

    def startService(self, passenger, stopTime):
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        finished_passenger = self._passenger
        self._passenger = None
        return finished_passenger


class TicketCounterSimulation:
    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        # parameters supplied by the user
        self._arriveprob = 1.0 / betweenTime # The probability of a passenger coming
        self._serviceTime = serviceTime # Processing time for one passenger
        self._numMinutes = numMinutes # Time for simulation to run
        self.served = 0 # How many passengers are served during 'numMinutes'

        # Simulation components
        self._passengersQueue = CircularQueue()
        self._Agents = [None] * numAgents
        for i in range(numAgents):
            self._Agents[i] = TicketAgent(i+1) # i+1 = Agent ID

        # Computed during the simulation
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        for currentTime in range(self._numMinutes + 1):
            self._handleArrival(currentTime)
            self._handleBeginService(currentTime)
            self._handleEndService(currentTime)
        self.printResult()

    def printResult(self):
        numServed = self._numPassengers - len(self._passengersQueue)
        avgWaitTime = float(self._totalWaitTime) / numServed
        print("\nNumber of passengers served = {}".format(numServed))
        print("Number of passengers remaining in line = {}".format(len(self._passengersQueue)))
        print("The average wait time was {:.2f} minutes.".format(avgWaitTime))

    def _handleArrival(self, currentTime):
        prob = randint(0.0, 1.0)
        if 0.0 <= prob <= self._arriveprob:
            passenger = Passenger(self._numPassengers + 1, currentTime) # ID, ArrivalTime
            self._passengersQueue.enqueue(passenger)
            self._numPassengers += 1
            print("Time {} : Passenger {} arrived".format(currentTime, passenger.getPID()))


    def _handleBeginService(self, currentTime):
        i = 0
        while i < len(self._Agents):
            # self._Agents[i] = TicketAgent instance
            if self._Agents[i].isFree() and not self._passengersQueue.isEmpty() and currentTime != self._numMinutes:
                passenger = self._passengersQueue.dequeue() # Passenger instance
                self.served += 1
                stopTime = currentTime + self._serviceTime
                self._Agents[i].startService(passenger, stopTime)
                self._totalWaitTime += (currentTime - passenger.getTimeArrived())
                print("Time {}: Agent {} started serving passenger {}".format(currentTime, self._Agents[i].getAID(), passenger.getPID() ))
            i+=1

    def _handleEndService(self, currentTime):
        i = 0
        while i < len(self._Agents):
            if self._Agents[i].isFinished(currentTime):
                passenger = self._Agents[i].stopService() # Return all processed passengers
                print("Time {}: Agent {} stopped serving passenger {}".format(currentTime, self._Agents[i].getAID(), passenger.getPID() ))
            i+=1


