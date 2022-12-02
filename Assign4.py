from Flight import *
from Airport import *
class Assign4:

    allAirports = {}
    allFlights = {}

    def loadData(airportFile, flightFile):
        try:
            with open(airportFile, "r") as filestream:
                for line in filestream:
                    formated_line = line.replace('\t', '').replace(' ','').strip('\n').strip('\t').split(",")
                    airportObj = Airport(formated_line[0], formated_line[2], formated_line[1])
                    Assign4.allAirports[formated_line[0]] = airportObj

            with open(flightFile, "r") as filestream:
                for line in filestream:
                    formated_line = line.replace('\t', '').replace(' ','').strip('\n').strip('\t').split(",")
                    try:
                        flightObj = Flight(formated_line[0], Assign4.allAirports.get(formated_line[1]), Assign4.allAirports.get(formated_line[2]))
                        Assign4.allFlights.setdefault(formated_line[1], []).append(flightObj)
                    except (TypeError) as e:
                        print(e)
            return True
        except:
            return False



    def getAirportByCode(code):
        return Assign4.allAirports[code] if code in Assign4.allAirports else -1



    def findAllCityFlights(city):
        result = []
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if flight._origin.city == city or flight._destination.city == city:
                    result.append(flight)
        return result




    def findAllCountryFlights(country):
        result = []
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if flight._origin.country == country or flight._destination.country == country:
                    result.append(flight)
        return result




    def findFlightBetween(origAirport, destAirport):
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if(flight._origin.city == origAirport.city and flight._destination.city == destAirport.city):
                    return " Direct Flight: " + flight._origin.code + " to " + flight._destination.code

        singleHopRoute = set()
        originMap = {}
        destinationMap = {}
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if(origAirport.city == flight._origin.city):
                    originMap[flight._destination.code] = flight
                elif(destAirport.city == flight._destination.city):
                    destinationMap[flight._origin.code] = flight
        for port in originMap.keys():
            if (len(originMap)!=0 and len(destinationMap)!=0 and originMap.get(port, None) != None and destinationMap.get(port, None) !=None):
                singleHopRoute.add(port)

        if len(singleHopRoute) != 0:
            return singleHopRoute
        else:
            return -1



    def findReturnFlight(firstFlight):
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if(flight._origin.city == firstFlight._destination.city and flight._destination.city == firstFlight._origin.city):
                    return flight
        return -1

    