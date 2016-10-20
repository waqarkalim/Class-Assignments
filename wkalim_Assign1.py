"""
This is program computes the rental costs for a car rental company.

The program starts here.



The first step is the intialisation stage, where different variables are assigned different values.
"""
"""
'customerName' is the variable that stores the name of the customer
'customerAge' is the variable that stores the age of the customer
'customerCode' is the variable that stores the Classification Code of the customer

"""
customerName = input("Enter your name: ").title()
customerAge = int(input("Enter your age: "))
customerCode = input("Enter either 'B', 'D', or 'W' as classification codes: ").upper()

# The if-condition below performs error handling on the variable 'customerCode' and verify whether a valid code was entered or not
if customerCode != "B" and customerCode != "D" and customerCode != "W":
    print("An error has occurred. User has inputted [{}] which is an invalid code.".format(customerCode))
    print("Customer name: " + customerName)
    print("Customer age: " + str(customerAge))
    quit()

"""
'numOfDaysCarRented' stores the value for the number of days the vehicle was rented in the rental period
'startingOdometer' stores the value for the odometer reading at the start of the rental period
'endingOdometer' stores the value for the odometer reading at the end of the rental period
"""
numOfDaysCarRented = int(input("Enter number of days the vehicle was rented: "))
startingOdometer = int(input("Enter the vehicle's odometer reading at the start of the rental period: "))
endingOdometer = int(input("Enter the vehicle's odometer reading at the end of the rental period: "))

"""
'numOfWeeksCarRented' stores the value for the number of weeks the customers rented the car for
'distanceTravelled' shows the number of kilometers driven by the customer during the rental period
'avgKmDrivenPerDay' stores the value for the average kilometers driven per day
'avgKmDrivenPerWeek' stores the value for the average kilometers driven per week
"""
numOfWeeksCarRented = (numOfDaysCarRented // 7) + 1
distanceTravelled = endingOdometer - startingOdometer
avgKmDrivenPerDay = distanceTravelled / numOfDaysCarRented
avgKmDrivenPerWeek = distanceTravelled / numOfWeeksCarRented

"""
'baseCharge' stores the initial value for the base charge which gradually changes as the program progresses
'kmDrivenCharge' stores the initial value for the fees that is charged for each kilometer travelled
'youngDriverCharges' stores the value for the fees the customer is charged if he/she is younger than 25 years
'
"""

baseCharge = 0
kmDrivenCharge = 0
youngDriverCharges = 0

"""
Below is the code that checks which Classification code is entered, 'B', 'D', or 'W', and executes the proper calculations depending on the conditions met
"""
if customerCode == "B":
    baseCharge = 20 * numOfDaysCarRented
    kmDrivenCharge = 0.30 * distanceTravelled

elif customerCode == "D":
    baseCharge = 50 * numOfDaysCarRented
    if avgKmDrivenPerDay <= 100:
        kmDrivenCharge = 0
    else:
        kmDrivenCharge = (distanceTravelled - 100) * 0.3

elif customerCode == "W":
    baseCharge = 200 * numOfWeeksCarRented
    if avgKmDrivenPerWeek <= 1000:
        kmDrivenCharge = 0
    elif 1000 < avgKmDrivenPerWeek <= 2000:
        kmDrivenCharge = 50 * numOfWeeksCarRented
    else:
        kmDrivenCharge = (100 * numOfWeeksCarRented) + (0.30 * (avgKmDrivenPerWeek - 2000) * numOfWeeksCarRented)

"""
'youngDriverCharges' stores the value for charges for being an inexperienced driver, drivers under the age of 25.
"""
if customerAge < 25:
    youngDriverCharges = 10 * numOfDaysCarRented

totalCharge = baseCharge + kmDrivenCharge + youngDriverCharges

"""
The code displays all the different inputs the user entered and all the outputs that the program calculated.
"""
print("\n"+"#"*75+"\n")

print("%-20s %54s" % ("Customer name: ", customerName))
print("%-20s %54s" % ("Customer's age: ", customerAge))
print("%-20s %42s" % ("Customer's classification code: ", customerCode))

print("\n"+"*"*75+"\n")

print("%-20s %39s" % ("Number of days the car was rented: ", numOfDaysCarRented))
print("%-20s %47s" % ("Starting odometer reading: ", startingOdometer))
print("%-20s %49s" % ("Ending odometer reading: ", endingOdometer))
print("%-20s %28s" % ("The number of kilometeres the car was driven: ", distanceTravelled))


print("\n"+"*"*75+"\n")

print("%-20s %54.2f" % ("Base Charge: ", "$" + str(baseCharge)))
print("%-20s %49.2f" % ("Kilometer Driven Charge: ", "$" + str(kmDrivenCharge)))
print("%-20s %45.2f" % ("Surcharge for young drivers: ", "$" + str(youngDriverCharges)))
print("%-20s %54.2f" % ("Total bill: ", "$" + str(totalCharge)))
