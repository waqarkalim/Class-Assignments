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
        catalogue = dict()
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

            #catalogue.append(country)
            catalogue[country.getName()] = [int(country.getPopulation()), float(country.getArea()), country.getContinent()]
            cDictionary[country.getName()] = country.getContinent()

            cline = cFile.readline()
            dline = dFile.readline()
        print(catalogue)
        cFile.close()
        dFile.close()

    def addCountry(self):
        #FOUND = False
        name = input("Enter country to add: ").title()
        # for country in catalogue:
        #     if name == country.getName():
        #         FOUND = True
        # if FOUND == True:
        #     print("Country cannot be added. Already in catalogue")
        if name in catalogue:
            print("Country cannot be added. Already in catalogue.")
            addCountry()
        else:
            population = int(input("Enter population: "))
            area = float(input("Enter area: "))
            continent = input("Enter continent: ")

            country = Country(name, population, area, continent)
            #catalogue.append(country)
            catalogue[name] = [population, area, continent]
            cDictionary[name] = continent
            print(name + " was added to catalogue.")
            print("*"*20)

    def deleteCountry(self):

        name = input("Enter country to be deleted: ").title()
        if name in catalogue:
            del catalogue[name]
            print(name + " was deleted from catalogue")
            print("*"*20)
        # for country in catalogue:
        #     if name.title()  == country.getName():
        #         catalogue.remove(country)
        #         print(name + " was deleted from catalogue.")

    def findCountry(self):
        name = input("Enter country to be searched for: ").title()
        while name not in catalogue:
            print(name + " not found in catalogue.")
            name = input("Enter country to be searched for: ").title()

        print(name + ":",catalogue.get(name))
        print("*"*20)
        # FOUND = False
        # name = input("Enter country to be searched for: ")
        # for country in catalogue:
        #     if name.title() == country.getName():
        #         FOUND = True
        #         print(name, catalogue.get(name))
        # if FOUND == False:
        #     print(name + " not found.")

    def filterCountriesByContinent(self):
        continent = input("Enter continent: ")
        for name in cDictionary:
            if continent.title() == cDictionary.get(name):
                print(name)

    def printCountryCatalogue(self):
        print(catalogue)
        print("*"*20)

    def setPopulationOfASelectedCountry(self):
        name = input("Enter name of the country whose population is to be changed: ").title()
        if name in catalogue:
            newPop = input("Enter new population for " + name + ": ")
            self._population = newPop
        else:
            print("Country not in catalogue.")
            print("*"*20)
        # FOUND = False
        # name = input("Enter country name: ")
        # for country in catalogue:
        #     if name.title() == country.getName():
        #         FOUND = True
        #         newPop  = input("Enter new population for", name + ": ")
        #         country.setPopulation(newPop)
        #         print("The new population density is", country.getPopDensity())
        # if FOUND == False:
        #     print("Country not in catalogue.")

    def findCountryWithLargestPop(self):
        maxPop = 0

        for country in catalogue:
            if catalogue.get(country)[0] > maxPop:
                maxPop = catalogue.get(country)[0]

        for country in catalogue:
            if maxPop == catalogue.get(country)[0]:
                print(country + " has the largest population of " + str(maxPop))
                print("*"*20)

    def findCountryWithSmallestArea(self):

        for country in catalogue:
            if country == list(catalogue.keys())[0]:
                minArea = catalogue.get(country)[1]
            if catalogue.get(country)[1] < minArea:
                minArea= catalogue.get(country)[1]

        for country in catalogue:
            if minArea == catalogue.get(country)[1]:
                print(country + " has the smallest area of " + str(minArea))
                print("*"*20)

    def filterCountriesByPopDensity(self):
        min = int(input("Enter lower bound of range: "))
        max = int(input("Enter upper bound of range: "))

        for country in catalogue:
            if min < catalogue.get(country)[0] < max:
                print(country)

    def findMostPopulousContinent(self):
        Asia = 0
        Europe = 0
        Australia = 0
        North_America = 0
        South_America = 0
        Antartica = 0
        Africa = 0

        for country in catalogue:
            if catalogue.get(country)[2] == "Asia":
                Asia += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "Europe":
                Europe += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "Australia":
                Australia += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "North America":
                North_America += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "South America":
                South_America += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "Antartica":
                Antartica += int(catalogue.get(country)[0])
            elif catalogue.get(country)[2] == "Africa":
                Africa += int(catalogue.get(country)[0])

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
            file.write(country + "|" + str(catalogue.get(country)[2]) + "|" + str(catalogue.get(country)[0]) + "|" + str(int(catalogue.get(country)[0])/int(catalogue.get(country)[1]))+"\n")
        file.close()
        print("All the output were successfully added to " + str(filename) + ".")
