"""
Created by Waqaar Bin Kalim
CS 1026A

This program analyzes a file containing twitter information like the tweet, the time the tweet was posted, and the location from where the tweet was posted in the form of longitude and latitude coordinates.
On top of that, it also searches if there are any keywords (which are given in keywords.txt) in the tweets, and if there are, then a "happiness score" is calculated which relies on the "sentiment values" which are also provided in "keywords.txt"
Apart from that, the program also searches for the region the tweet was posted from and ultimately calculates the "happiness score" for the all the regions.
"""
# importing the drawSimpleHistogram function from happy_histogram.py to draw a graph of the "happiness score" that we will caluclate later in the program
from happy_histogram import drawSimpleHistogram

# different coordinates are initialized, and these coordinates will be used to determine in which region a tweet originated from
p1 = (49.189787, -67.444574) 
p2 = (24.660845, -67.444574) 
p3 = (49.189787, -87.518395) 
p4 = (24.660845, -87.518395) 
p5 = (49.189787, -101.998892) 
p6 = (24.660845, -101.998892) 
p7 = (49.189787, -115.236428) 
p8 = (24.660845, -115.236428) 
p9 = (49.189787, -125.242264)
p10 = (24.660845, -125.242264)


# the coordinateValues() function takes in one parameter, the coordniates that are in the lines that are being read, and just outputs the values as an float
def coordinateValues(line):
	line = line.split(" ", 2)
	line.pop()
	Xcoordinate = float(line[0][1:-1])
	Ycoordinate = float(line[1][:-1])
	return Xcoordinate, Ycoordinate

# the locationTracker() function takes in two parameters, the X-coordinate and the Y-coordinate of the tweet, and tries to determines the actual region the tweet originated from by narrowing down the X and Y coordinates in the pre-initialized coordinates that we have
def locationTracker(Xcoordinate, Ycoordinate):

	location = ""
	if p2[0] < Xcoordinate < p1[0] and p4[0] < Xcoordinate < p3[0]:
		if p4[1] < Ycoordinate < p2[1] and p3[1] < Ycoordinate < p1[1]:
			location = "Eastern"
		elif p6[1] < Ycoordinate < p4[1] and p5[1] < Ycoordinate < p3[1]:
			location = "Central"
		elif p8[1] < Ycoordinate < p6[1] and p7[1] < Ycoordinate < p5[1]:
			location = "Mountain"
		elif p10[1] < Ycoordinate < p8[1] and p9[1] < Ycoordinate < p7[1]:
			location = "Pacific"
	else:
		return("Location not in range")
	return location


# the regionCounter() function takes in 7 parameters, and outputs the number of tweets that originated from each region, and also how many did not belong to any region
def regionCounter(location, MATCH, EasternCount, CentralCount, MountainCount, PacificCount, OutOfRange):
	
	if MATCH:
		if location == "Eastern":
			EasternCount += 1
		elif location == "Central":
			CentralCount += 1
		elif location == "Mountain":
			MountainCount += 1
		elif location == "Pacific":
			PacificCount += 1
		else:
			OutOfRange += 1

	return EasternCount, CentralCount, MountainCount, PacificCount, OutOfRange

# the regionScore() function takes 6 parameters, and outputs by total sum of the sentiments values for each region
def regionScore(location, happinessSCORE, EasternScore, CentralScore, MountainScore, PacificScore):
	
	if location == "Eastern":
		EasternScore += happinessSCORE
	elif location == "Central":
		CentralScore += happinessSCORE
	elif location == "Mountain":
		MountainScore += happinessSCORE
	elif location == "Pacific":
		PacificScore += happinessSCORE

	return EasternScore, CentralScore, MountainScore, PacificScore

# the finalRegionScore() takes in 8 parameters, and it outputs the final happiness score for each region, by dividing the sum that we got by calling the regionScore() function, by the number of tweet that originataed in each region.
def finalRegionScore(EasternScore, EasternCount, CentralScore, CentralCount, MountainScore, MountainCount, PacificScore, PacificCount):

	EasternScore = EasternScore/EasternCount
	CentralScore = CentralScore/CentralCount
	MountainScore = MountainScore/MountainCount
	PacificScore = PacificScore/PacificCount

	return EasternScore, CentralScore, MountainScore, PacificScore

# the KeywordOrganize() function takes in 1 parameter, each line of the file "keywords.txt", and tries to store each keyword and its sentiment value inside a list.
def KeywordOrganize(lineKEYWORD):
	keywordLIST = []
	while lineKEYWORD != "":
		lineWORD_list = []
		lineKEYWORDlist = list(lineKEYWORD.rstrip())
		comma_pos = lineKEYWORDlist.index(",")
		keyword = "".join(lineKEYWORDlist[:comma_pos])
		score = "".join(lineKEYWORDlist[comma_pos+1:])
		lineWORD_list.append(keyword)
		lineWORD_list.append(int(score))
		keywordLIST.append(lineWORD_list)
		lineKEYWORD = infileKEYWORD.readline()
	return keywordLIST

# the wordMatch() function takes in 2 parameters, and processes whether there are any same words between the words in the "keywords.txt" file and tweets that are in the "tweet.txt" file and also calcualates the happiness Score, and returns the happiness Score and whether a match was found.
def wordMatch(keywordLIST, lineTWEETList):
	global MATCH
	happinessSCORE = 0
	NumberOfMatches = 0
	for word in keywordLIST:
		#print(section)
		for section in lineTWEETList:
			if str(word[0]).lower() == str(section).lower():
				index = keywordLIST.index(word)
				happinessSCORE = happinessSCORE + int(keywordLIST[index][1])
				MATCH = True
				NumberOfMatches = NumberOfMatches + 1

	if NumberOfMatches != 0:
		happinessSCORE = happinessSCORE/NumberOfMatches

	return happinessSCORE, MATCH

text_file = "tweets.txt"
keyword_file = input("Enter the name of the keyword file:- ") # "keywords.txt"

infileTEXT = open(text_file, "r", encoding='utf-8', errors='ignore')
infileKEYWORD = open(keyword_file, "r", encoding='utf-8', errors='ignore')

lineKEYWORD = infileKEYWORD.readline()
lineTWEET = infileTEXT.readline()

keywordLIST = KeywordOrganize(lineKEYWORD)

EasternScore = 0
CentralScore = 0
MountainScore = 0
PacificScore = 0

EasternCount = 0
CentralCount = 0
MountainCount = 0
PacificCount = 0

OutOfRange = 0

while lineTWEET != "":
	MATCH = False
	
	lineTWEET.strip("\n ,.!?")
	lineTWEETList = lineTWEET.split(" ")
	
	Xcoordinate, Ycoordinate = coordinateValues(lineTWEET)
	
	location = locationTracker(Xcoordinate, Ycoordinate)

	score, MATCH = wordMatch(keywordLIST, lineTWEETList)

	EasternCount, CentralCount, MountainCount, PacificCount, OutOfRange = regionCounter(location, MATCH, EasternCount, CentralCount, MountainCount, PacificCount, OutOfRange)
	EasternScore, CentralScore, MountainScore, PacificScore = regionScore(location, score, EasternScore, CentralScore, MountainScore, PacificScore)


	lineTWEET = infileTEXT.readline()
	


print("Eastern Count: %s \nCentral Count: %s \nMountain Count: %s \nPacific Count: %s \n" % (EasternCount, CentralCount, MountainCount, PacificCount))

EasternScore, CentralScore, MountainScore, PacificScore = finalRegionScore(EasternScore, EasternCount, CentralScore, CentralCount, MountainScore, MountainCount, PacificScore, PacificCount)

print("Eastern Final Score: %s \nCentral Final Score: %s \nMountain Final Score: %s \nPacific Final Score: %s \n" % (EasternScore, CentralScore, MountainScore, PacificScore))

drawSimpleHistogram(EasternScore, CentralScore, MountainScore, PacificScore)



infileTEXT.close()
infileKEYWORD.close()
