from Airport import *

class Flight:
    def __init__(self, flightNo, origin, destination):
        if(not (isinstance(origin, Airport) and isinstance(destination, Airport))):
            raise TypeError("The origin and destination must be Airport objects")
        
        self._flightNo = flightNo
        self._origin = origin
        self._destination = destination



    def __repr__(self):
        zone = "domestic" if self.isDomesticFlight() else "international"
        return "Flight: " + self._flightNo + " from " + self._origin.city + " to " + self._destination.city + " { " + zone + " }"



    def __eq__(self, other):
        if(not isinstance(other, Flight)):
            return False

        if(other._origin == self._origin and other._destination == self._destination):
            return True

        return False



    def getFlightNumber(self):
        return self._flightNo



    def getOrigin(self):
        return self._origin



    def getDestination(self):
        return self._destination


    def isDomesticFlight(self):
        return self._origin.country == self._destination.country
    

    def setOrigin(self, origin):
        self._origin = origin



    def setDestination(self, destination):
        self._destination = destination
