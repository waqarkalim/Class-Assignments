"""
David Moriarty
CompSci 1026A
Assignment 4
"""


class Country :

    def __init__(self, name, pop, area, continent) :
        self._name = name
        self._pop = pop
        self._area = area
        self._continent = continent

    def __repr__(self) :
        return "%s in %s" % ( (self._name).title(), (self._continent).title() )

    def setPopulation(self, pop) :
        self._pop = pop

    def getName(self) :
        return self._name

    def getArea(self) :
        return self._area

    def getPopulation(self) :
        return self._population

    def getContinent(self) :
        return self._continent

    def getPopDensity(self) :
        popDensity = self._pop / self._area
        return populationDensity


class CountryCatalogue :

    # opens and reads from continent.txt to create cDictionary.
    def readContinentFile(cont_file) :
        cDictionary = {}

        cont_file = "continent.txt"
        cont_data = open(cont_file, 'r', encoding='utf-8', errors='ignore')

        readlines = cont_data.readline()
        readlines = cont_data.readlines()

        for line in readlines :
            Type = line.split(",")
            countryData = Type[0]
            continentData = Type[1]
            cDictionary[countryData] = continentData

        cont_data.close()
        return cDictionary

    # opens and reads from data.txt to create catalogue dictionary
    def readDataFile(cont_file, data_file) :
        catalogue = {}
        # catalogue has continent first, then population and then area.
        cont_file = 'continent.txt'
        data_file = 'data.txt'

        cont_data = open(cont_file, 'r', encoding='utf-8', errors='ignore')
        data = open(data_file, 'r', encoding='utf-8', errors='ignore')

        contline = cont_data.readline()
        contline= cont_data.readline()
        line = data.readline()
        line = data.readline()

        while line != "" and contline != "":
            catalogueList = []

            line = line.split("|")
            contline = contline.split(",")
            contline[1] = contline[1].rstrip("\r\n")
            line[1] = "".join(line[1].split(","))
            line[2] = "".join(line[2].split(",")).rstrip("\r\n")

            catalogueList.append(contline[1])
            catalogueList.append(line[1])
            catalogueList.append(line[2])
            catalogue[line[0]] = catalogueList

            line = data.readline()
            contline = cont_data.readline()

        cont_data.close()
        data.close()

        return catalogue

    # constructor method that initiates the catalogue and cDictionary.
    def __init__(self, catalogue, cDictionary) :
        self._catalogue =  readDataFile('data.txt')
        self._cDictionary = readContinentFile('continent.txt')

    # reads in user input continent name and prints all countries in the dictionary under that continent.
    def filterCountriesByContinent(self) :
        filterContinent = input("Enter the continent you want: ")

        for element in cDictionary :
            if filterContinent in cDictionary.get(element) :
                print(element)
            else :
                print("There are no contries from that continent.")

    # prints the whole country catalogue to the screen.
    def printCountryCatalogue(self) :
        for key, value in catalogue.items() :
            print(key, value)

    # searches for the country from user input in the catalogue.
    def findCountry(self) :
        findCountry = input("Enter the country you want to lookup: ")
        if findCountry in catalogue :
            print(catalogue[findCountry])
            print()
        else :
            print("Country not found.")
            print()

    # deletes a country from catalogue
    def deleteCountry(self) :
        deleteCountryName = input("Enter the country you want to delete: ")

        if deleteCountryName in catalogue :
            del catalogue[deleteCountryName]
            print(deleteCountryName, "was deleted.")

        else :
            print("That country wasn't found.")
            print()

    # adds a country to catalogue
    def addCountry(self, addCountry) :
        addCountryList = []
        addCountryName = input("Enter the country name: ")

        while addCountryName in catalogue :
            print("That country is already in the list.")
            addCountryName = input("Enter the country name: ")

        else :
            addContinentName = input("Enter the continent name: ")
            addPopulationValue = input("Enter the country's population: ")
            addAreaValue = input("Enter the country's area: ")
            addCountryList.append(addContinentName)
            addCountryList.append(addPopulationValue)
            addCountryList.append(addAreaValue)
            catalogue[addCountryName] = addCountryList

            print(addCountryList)
            print()
            print("Successfully added the country.")
            print(addCountryName, catalogue.get(addCountryName))

        return addCountry, addCountryName, addContinentName, addPopulationValue, addAreaValue

    # user inputs the name of a country, then user inputs  the new population value, and the dictionary is updated.
    def setPopulationOfASelectedCountry(self, newPop) :
        countryName = input("Enter the country you want to update the population for: ")

        if countryName in catalogue :
            print(catalogue[countryName])
            print()
            newPop = input("Enter the updated population: ")

            for key, value in catalogue.items() :
                if key == countryName :
                    catalogue[countryName][1] = newPop

            print("The population of" + catalogue[countryName] + "was updated successfully!")
            print(catalogue[countryName])

        else :
            print("Country not found.")

        return newPop, countryName

    # saves the countryCatalogue to an output file.
    def saveCountryCatalogue(self, outfile) :
        sortedCatalogue = sorted(catalogue.items())
        outfile = open('output.txt', 'w', encoding='utf-8', errors='ignore')
        for key, value in catalogue.items() :
            outfile.write('%s | %s\n' % (key, value))
        return outfile

    # looks for the country with the largest population.
    def findCountryWithLargestPop(self) :
        print("The country with the largest population is: ")
        largestPop = max(catalogue.items())
        print(largestPop)

    # looks for the country with the smallest area.
    def findCountryWithSmallestArea(self) : #Won't work, because you are just print the smallestArea which is still an integer, you would need to get the name of the country for it.
        print("The country with the smallest area is: ")
        smallestArea = min(catalogue.items())
        print(smallestArea)

    # looks for the most populated continent.
    def findMostPopulousContinent(self) :
        Asia = 0
        Africa = 0
        Antartica = 0
        Australia = 0
        NAmerica = 0
        SAmerica = 0
        Europe = 0

        for countryName in catalogue:
            if countryName[0] == "Asia":
                Asia += int(countryName[1])
            if countryName[0] == "Africa":
                Africa += int(countryName[1])
            if countryName[0] == "Antartica":
                Antartica += int(countryName[1])
            if countryName[0] == "Australia":
                Australia += int(countryName[1])
            if countryName[0] == "North America":
                NAmerica += int(countryName[1])
            if countryName[0] == "South America":
                SAmerica += int(countryName[1])
            if countryName[0] == "Europe":
                Europe += int(countryName[1])

        cPopDictionary = {Asia: "Asia", Africa: "Africa", Antartica: "Antartica", NAmerica: "North America", SAmerica: "South America", Europe: "Europe"}
        maxPop = max(cPopDictionary)
        print("The most populous continent is:", cPopDictionary.get(maxPop))

    # filters the countries by their population densities.
    def filterCountriesByPopDensity(self) :
        print("The countries sorted by population density: ")
