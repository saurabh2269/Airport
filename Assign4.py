from Flight import *
from Airport import *
class Assign4:

    allAirports = {}
    allFlights = {}

    def loadData(airportFile, flightFile):
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
                    print(flightObj)
                    Assign4.allFlights.setdefault(formated_line[1], []).append(flightObj)
                except (TypeError) as e:
                    print(e)
        print(Assign4.allFlights)

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
        result = []
        for flights in Assign4.allFlights.values():
            for flight in flights:
                if flight._origin.country == country or flight._destination.country == country:
                    result.append(flight)
        return result

    def findReturnFlight(firstFlight):
        pass

    