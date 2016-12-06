"""
Created by: Waqar Bin Kalim
CompSci 1026
Assignment 4
"""

class Country:
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent

    def __repr__(self):
        output = str(self._name) + " in " + str(self._continent)
        return output

    def setPopulation(self, pop):
        self._population = pop

    def getName(self):
        return self._name

    def getArea(self):
        return self._area

    def getPopulation(self):
        return self._population

    def getContinent(self):
        return self._continent

    def getPopDensity(self):
        return self._population/self._area

class CountryCatalogue:

    def __init__(self, filename):
        global catalogue
        global cDictionary
        catalogue = list()
        cDictionary = dict()

        continentFile = "continent.txt"
        self._dFile = filename

        cFile = open(continentFile, "r")
        dFile = open(self._dFile, "r")

        cline = cFile.readline()
        cline = cFile.readline()

        dline = dFile.readline()
        dline = dFile.readline()

        while (cline != "") and (dline != ""):
            cline = cline.split(",")
            dline = dline.split("|")

            ccName = cline[0]
            dcName = dline[0]

            population = "".join(dline[1].split(","))
            area = "".join(dline[2].split(",")).rstrip("\r\n")
            continent = cline[1].rstrip("\r\n")

            country = Country(ccName, population, area, continent)

            catalogue.append(country)
            #catalogue[country.getName()] = [int(country.getPopulation()), float(country.getArea()), country.getContinent()]
            cDictionary[country.getName()] = country.getContinent()

            cline = cFile.readline()
            dline = dFile.readline()
        print(catalogue)
        cFile.close()
        dFile.close()

    def addCountry(self):
        FOUND = False
        name = input("Enter country to add: ")
        for country in catalogue:
            if name == country.getName():
                FOUND = True
        if FOUND == True:
            print("Country cannot be added. Already in catalogue")

        else:
            population = int(input("Enter population: "))
            area = float(input("Enter area: "))
            continent = input("Enter continent: ")

            country = Country(name, population, area, continent)
            catalogue.append(country)
            print(name + " was successfully added to catalogue")
            print("*"*30)
        # if name in catalogue:
        #     print("Country cannot be added. Already in catalogue.")
        #     addCountry()
        # else:
        #     population = int(input("Enter population: "))
        #     area = float(input("Enter area: "))
        #     continent = input("Enter continent: ")

        #     country = Country(name, population, area, continent)
        #     #catalogue.append(country)
        #     catalogue[name] = [population, area, continent]
        #     cDictionary[name] = continent
        #     print(name + " was added to catalogue.")
        #     print("*"*20)

    def deleteCountry(self):
        name = input("Enter country to delete: ")
        FOUND = False
        for country in catalogue:
            if name  == country.getName():
                FOUND = True
                catalogue.remove(country)
                print(name + " was deleted from catalogue.")
        if FOUND == False:
            print(name + " was not in catalogue.")

    def findCountry(self):
        #name = input("Enter country to be searched for: ").title()
        # while name not in catalogue:
        #     print(name + " not found in catalogue.")
        #     name = input("Enter country to be searched for: ").title()

        # print(name + ":",catalogue.get(name))
        # print("*"*20)
        FOUND = False
        name = input("Enter country to be searched for: ")
        for country in catalogue:
            if name == country.getName():
                FOUND = True
                print(country.getName() + ": " + country.getPopulation() + ", " + country.getArea() + ", " + country.getContinent())
        if FOUND == False:
            print(name + " not found.")

    def filterCountriesByContinent(self):
        continent = input("Enter continent: ")
        for name in cDictionary:
            if continent.lower() == cDictionary.get(name).lower():
                print(name)

    def printCountryCatalogue(self):
        for country in catalogue:
            print(country)
        print("*"*30)

    def setPopulationOfASelectedCountry(self):
        #name = input("Enter name of the country whose population is to be changed: ").title()
        # if name in catalogue:
        #     newPop = input("Enter new population for " + name + ": ")
        #     self._population = newPop
        # else:
        #     print("Country not in catalogue.")
        #     print("*"*20)
        FOUND = False
        name = input("Enter name of the country whose population is to be changed: ")
        for country in catalogue:
            if name.title() == country.getName():
                FOUND = True
                newPop  = int(input("Enter new population for " + name + ": "))
                country.setPopulation(newPop)
                print("The new population density is", country.getPopDensity())
        if FOUND == False:
            print("Country not in catalogue.")

    def findCountryWithLargestPop(self):
        maxPop = 0

        for country in catalogue:
            if int(country.getPopulation()) > int(maxPop):
                maxPop = country.getPopulation()

        for country in catalogue:
            if maxPop == country.getPopulation():
                print(country.getName() + " has the largest population of " + str(maxPop))
                print("*"*30)

    def findCountryWithSmallestArea(self):

        for country in catalogue:
            if country.getName() == list(catalogue)[0].getName():
                minArea = float(country.getArea())
            if float(country.getArea()) < minArea:
                minArea = float(country.getArea())

        for country in catalogue:
            if minArea == country.getArea():
                print(country.getName() + " has the smallest area of " + str(minArea))
                print("*"*30)

    def filterCountriesByPopDensity(self):
        min = int(input("Enter lower bound of range: "))
        max = int(input("Enter upper bound of range: "))
        print("The countries which fall into the population range of %s and %s are: " % (str(min), str(max)))
        for country in catalogue:
            if int(min) < int(country.getPopulation()) < int(max):
                print(country.getName())

    def findMostPopulousContinent(self):
        Asia = 0
        Europe = 0
        Australia = 0
        North_America = 0
        South_America = 0
        Antartica = 0
        Africa = 0

        for country in catalogue:
            if country.getContinent() == "Asia":
                Asia += int(country.getPopulation())
            elif country.getContinent() == "Europe":
                Europe += int(country.getPopulation())
            elif country.getContinent() == "Australia":
                Australia += int(country.getPopulation())
            elif country.getContinent() == "North America":
                North_America += int(country.getPopulation())
            elif country.getContinent() == "South America":
                South_America += int(country.getPopulation())
            elif country.getContinent() == "Antartica":
                Antartica += int(country.getPopulation())
            elif country.getContinent() == "Africa":
                Africa += int(country.getPopulation())

        maxPop = max(Asia, Europe, Australia, North_America, South_America, Antartica, Africa)
        cPopDictionary = {Asia : "Asia", Europe : "Europe", Australia : "Australia", North_America : "North America", South_America : "South America", Antartica : "Antartica", Africa : "Africa"}
        for pop in cPopDictionary:
            if pop == maxPop:
                continent = cPopDictionary.get(pop)

        print("The most populous continent is", continent)
        print("*"*20)

    def saveCountryCatalogue(self, filename):
        file = open(filename, "w")
        for country in catalogue:
            file.write(country.getName() + "|" + str(country.getContinent()) + "|" + str(country.getPopulation()) + "|" + str(int(country.getPopulation()/int(country.getArea()))+"\n"))
        file.close()
        print("All the output were successfully added to " + str(filename) + ".")
