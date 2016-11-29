from ReadFile import FileReader

class CountryCatalogue():
	DEFAULT_SIZE = 5
	NOT_FOUND = -1

	catalogue = []

	numOfCountries = 0

	continents = set()

	cdict = dict()

	countryReader = FileReader()
	continentReader = FileReader()

	def __init__(countryFile, continentFile):
		catalogue = Country(DEFAULT_SIZE)
		numOfCountries = 0

		countryReader = FileReader(countryFile)
		continentReader = FileReader(continentFile)

		continentReader.readline()
		while not continentReader.EOF():
			line = continentReader.readline()
			info = line.split(",")
			country = info[0]
			continent = info[1]
			continents.add(continent)
			cdict[country] = continent

		continentReader.close()

		countryReader.readline()
		while not countryReader.EOF():
			line = countryReader.readline()
			CountryInfo = line.split(",")
			Country_Name = CountryInfo[0]
			Country_Population = int(CountryInfo[1])
			Country_Area = float(CountryInfo[2])
			country = cdict.get(Country_Name)

			Country_Info = Country(Country_Name, Country_Population, Country_Area, continent)
			addCatalogue(CountryInfo)

		countryReader.close()

	def addCatalogue(country):
		if len(catalogue) == numOfCountries:
			expandCapacity()

		catalogue[numOfCountries] = country
		numOfCountries += 1

	def expandCapacity():
		largerCatalogue = Country[len(catalogue)*2]
		for i in range(0, len(catalogue)):
			largerCatalogue[i] = catalogue[i]

		catalogue = largerCatalogue

	def addCountry(country):
		continents.add(country.getContinent())
		cdict.add(country.getCountry_Name(), country.getContinent())
		addCatalogue(country)

	def getCountry(index):
		if (index < numOfCountries) and (index != NOT_FOUND):
			return catalogue[index]

		return None

	def printCountryCatalogue():
		print("\n Country Catalogue: ")
		for i in range(0, numOfCountries):
			print("\n" + str(catalogue[i]))

	













