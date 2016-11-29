import java.util.*;

public class CountryCatalogue {
	/**
	 * the default size as to how many countries in catalogue
	 */
	private final int DEFAULT_SIZE = 5;
	/**
	 * the index at which the Country is not found
	 */
	private final int NOT_FOUND = -1;
	
	/**
	 * initializing an array to hold the countries
	 */
	private Country [] catalogue;
	/**
	 * the current number of countries
	 */
	private Integer numOfCountries;
	/**
	 * a set of continents
	 */
	public Set<String> continents;
	/**
	 * declaring a map for dictionary
	 */
	public Map<String, String> cdict;
	
	private ThingToReadFile countryReader;
	private ThingToReadFile continentReader;
	
	/**
	 * Constructor 
	 * @param filename: setting the entire text file as string 
	 */
	public CountryCatalogue(String countryFile, String continentFile){
		/***
		 * Initiating instance variables
		 */
		catalogue = new Country[DEFAULT_SIZE];
		numOfCountries = 0;
	
		countryReader = new ThingToReadFile(countryFile);
		continentReader = new ThingToReadFile(continentFile);

		continents = new HashSet<String>();
		cdict = new HashMap<String, String>();

		/**
		 * Splits and stores the file into its appropriate variables
		 * gets rid of header 
		 * reads the continent file
		 */
        continentReader.readLine();
        while(!continentReader.endOfFile()){
            String line = continentReader.readLine();
            String[] info = line.split(",");
            String country = info[0];
            String continent = info[1];
            continents.add(continent);
            cdict.put(country, continent);
        }
        continentReader.close();

		//Read country file
		//Gets rid of header
		countryReader.readLine();
        while(!countryReader.endOfFile()){
            String line = countryReader.readLine();
            String[] CountryInfo = line.split(",");
            String Country_Name = CountryInfo[0];
            Integer Country_Population = Integer.parseInt(CountryInfo[1]);
            double Country_Area = Double.parseDouble(CountryInfo[2]);
            String continent = cdict.get(Country_Name);

            Country Country_Info = new Country(Country_Name, Country_Population, Country_Area, continent);
            addCatalogue(Country_Info);
        }
        countryReader.close();
	}
	/**
	 * addCatalogue method: that add countries to the new array
	 * @param country: object to compare all the countries
	 */
	private void addCatalogue(Country country){
		if (catalogue.length == numOfCountries){
            expandCapacity();
		}

        catalogue[numOfCountries] = country;
        numOfCountries++;
	}
	/**
	 * expandCapacity method: that add countries to the new array
	 */
	private void expandCapacity(){
		Country[] largerCatalogue = new Country[catalogue.length*2];
		for (int i = 0; i < catalogue.length; i++){
			largerCatalogue[i] = catalogue[i];
		}
        catalogue = largerCatalogue;
	}

	/**
	 * addCountry method: that add countries and updates the set and cdict
	 * @param country: object to compare all the countries
	 */
	public void addCountry(Country country){
		continents.add(country.getContinent());
        cdict.put(country.getCountry_Name(), country.getContinent());
		addCatalogue(country);
	}
	/**
	 * gets the Country
	 * @param index
	 */
	public Country getCountry(int index){
        if(index < numOfCountries && index != NOT_FOUND){
            return catalogue[index];
        }

		return null;
	}
	/**
	 * printCountryCatalogue() method: prints the country details in appropriate format 
	 */
	public void printCountryCatalogue(){
        System.out.println("\n Country Catalogue: ");
        for(int i = 0; i < numOfCountries; i++){
            System.out.println("\n" + catalogue[i].toString());
        }
	}
	/**
	 * filterCountriesByContinent() method: filters the countries by continent
	 * @param Continent
	 */
	public void filterCountriesByContinent(String continent){
        System.out.println("\nCountries in " + continent + ": ");
        for(int i = 0; i < numOfCountries; i++){
            if(catalogue[i].getContinent().equals(continent)){
                System.out.println(catalogue[i].getCountry_Name());
            }
        }
	}
	/**
	 * searchCatalogue() method: searches through catalogue array for specified country
	 * @param Continent
	 */
	public int searchCatalogue(String country){
		for(int i = 0; i < numOfCountries; i++){
            if(catalogue[i].getCountry_Name().equals(country)){
				return i;
			}
		}

        System.out.println("\nTarget country not in catalogue.");
        return NOT_FOUND;
	}
	/**
	 * removeCountry() method: filters the countries by continent
	 * @param Country
	 */
	public void removeCountry(String country){
		int index = searchCatalogue(country);
		if(index != NOT_FOUND){
			System.out.println("\nCountry \"" + country + "\" removed successfully.");
			catalogue[index] = catalogue[numOfCountries];
			catalogue[numOfCountries] = null;
            numOfCountries--;
		}else{
			System.out.println("\nCannot find country");
		}
	}

    public void setPopulationOfACountry(String country, int newpop){
        int index = searchCatalogue(country);
        if(index != NOT_FOUND){
            System.out.println("\nChanging population of " + country + " to " + newpop);
            catalogue[index].setCountry_Population(newpop);
        }else{
            System.out.println("\nCould not change " + country + " population.");
        }
    }

    public void saveCountryCatalogue(String file){
        ThingToWriteFile writeFile = new ThingToWriteFile(file);
        for(int i = 0; i < numOfCountries; i++){
            catalogue[i].writeToFile(writeFile);
        }
    }

    public int findCountryWithLargestPop(){
        int largestPopIndex = 0;

        for(int i = 0; i < numOfCountries; i++){
            if(catalogue[i].getCountry_Population() > catalogue[largestPopIndex].getCountry_Population()){
                largestPopIndex = i;
            }
        }

        return largestPopIndex;
    }

    public int findCountryWithSmallestArea(){
        int smallestAreaIndex = 0;

        for(int i = 0; i < numOfCountries; i++){
            if(catalogue[i].getCountry_Area() < catalogue[smallestAreaIndex].getCountry_Area()){
                smallestAreaIndex = i;
            }
        }

        return smallestAreaIndex;
    }

    public void printCountriesFilterDensity(int low, int high){
        System.out.println("\nCountries with a population density between " + low + " and " + high + ": ");

        for(int i = 0; i < numOfCountries; i++){
            double density = catalogue[i].getPopDensity();
            if(density >= low && density <= high){
                System.out.println("\n\t" + catalogue[i].toString() + "\n\t has a population density of " + density + ".");
            }
        }
    }

    public void findMostPopulousContinent(){
        // Init map
        Map<String, Integer> conts = new HashMap<>();
        for(String c : continents){
            conts.put(c, 0);
        }

        // Add up all continent populations
        for(int i = 0; i < numOfCountries; i++){
            String continent = catalogue[i].getContinent();
            int oldPop = conts.get(continent);
            int tempPop = catalogue[i].getCountry_Population();
            conts.replace(continent, oldPop + tempPop);
        }

        // Find max population
        int max = 0;
        for(int p : conts.values()){
            if(p > max){
                max = p;
            }
        }

        // Find the continent name that has max population
        String maxName = "";
        for(String c : conts.keySet()){
            if(conts.get(c) == max){
                maxName = c;
            }
        }

        System.out.println("\nContinent with the largest population: " + maxName + ", with " + max);
    }

}
