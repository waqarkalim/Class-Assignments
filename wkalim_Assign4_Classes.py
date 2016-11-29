"""
Created by Waqaar Bin Kalim
COMPSCI 1028A
Assignment4
"""

class Country():

	def __init__(self, name, pop, area, continent):
		
		self.name = name
		self.pop = int(pop)
		self.area = float(area)
		self.continent = continent

	def getName(self):
		return self.name

	def getPopulation(self):
		return self.population

	def getArea(self):
		return self.area

	def getContinent(self):
		return self.continent

	def getPopDensity(self):
		popDensity = self.pop/self.area
		return popDensity

	def setPopulation(self, pop):
		self.pop = 0

	def __repr__(self):
		return "%s in %s" %((self.name).title(), (self.continent).title())

class CountryCatalogue():

	def readContinentFile(file):
		cDictionary = {}
		infile = open(file, "r")
		
		line = infile.readline()
		line = infile.readline()
		
		while line != "":
			line.split(":").strip("\n")
			cDictionary[line[0]] = line[1]
		infile.close()

		return cDictionary

	def readDataFile(file):
		catalogue = {}
		infile = opne(file, "r")

		line = infile.readline()
		line = infile.readline()

		while line != "":
			line.split("|").strip("\n")
			catalogue[line[0]] = line[1]
			catalogue[line[0]] = line[2]
		infile.close()

		return catalogue

	def __init__(self, catalogue, cDictionary):

		self.catalogue = readDataFile("data.txt")
		self.cDictionary = readContinentFile("continent.txt")
		





