/**
 * This class represents basic country information.
 * @Umair Qureshi CS1027 
 * ID:250812923
 */
public class Country {
	/**
	 * the name of the Country and Continent 
	 */
	private String Continent,Country_Name;
	/**
	 * the area of the country
	 */
	private double Country_Area;
	/**
	 * the population of the country
	 */
	private Integer Country_Population;
	
	/**
	 * Constructor
	 * @param Country_Name set to String value
	 * @param Country_Area set to Double value
	 * @param Country_Population set to Integer value
	 */
	public Country(String Country_Name, Integer Country_Population, double Country_Area, String continent) {
	    Continent = continent;
		this.setCountry_Name(Country_Name);
	    this.setCountry_Area(Country_Area);
	    this.setCountry_Population(Country_Population);
	
	}
	/**
	 * gets the Country_Name
	 * @param Country_Name
	 */
	public String getCountry_Name() {
		return Country_Name;
	}
	/**
	 * sets the Country_Name to itself
	 * @param Country_Name
	 */
	public void setCountry_Name(String country_Name) {
		Country_Name = country_Name;
	}
	/**
	 * gets the Country_Area 
	 * @param Country_Area
	 */
	public double getCountry_Area() {
		return Country_Area;
	}
	/**
	 * sets the Country_Area to itself
	 * @param Country_Area
	 */
	public void setCountry_Area(double country_Area) {
		Country_Area = country_Area;
	}
	/**
	 * gets the Country_Population 
	 * @param Country_Population
	 */
	public Integer getCountry_Population() {
		return Country_Population;
	}
	/**
	 * sets the Country_Population to itself
	 * @param Country_Population
	 */
	public void setCountry_Population(Integer country_Population) {
		Country_Population = country_Population;
	}
	/**
	 * gets the Continent
	 * @param Continent
	 */
	public String getContinent() {
		return Continent;
	}
	/**
	 * sets the Continent to itself
	 * @param Continent
	 */
	public void setContinent(String continent) {
		Continent = continent;
	}
	/**
	 * getpopdensity() method: gets the Population Density by calculating it out 
	 */
	public Double getPopDensity(){
		Double PopDensity = this.getCountry_Population()/this.getCountry_Area();
		return PopDensity;
	}
	/**
	 * writeToFile Method: writes to a file using the ThingToWriteFile object write
	 */
	public void writeToFile(ThingToWriteFile write){
		write.writeLine(Country_Name + "," + Continent + "," + Country_Population + "," + getPopDensity());
	}
	/**
	 * printCountryDetails() method: prints the country details in appropriate format 
	 * @param Country_Area
	 */
	public void printCountryDetails(){
		System.out.println("\n" + Country_Name + " is located in " + Continent + " has a population of " + Country_Population +
				" an area of " + Country_Area + " and has a population density of " + getPopDensity());
	}
	/**
	 * toString Method: Returns the Part Information as a String
	 */
	public String toString(){
		String CountryInfo = this.Country_Name + " in " + this.Continent;
		return CountryInfo;
	}
}
