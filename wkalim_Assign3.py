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


def coordinateValues(line):
	line = line.split(" ", 2)
	line.pop()
	Xcoordinate = float(line[0][1:-1])
	Ycoordinate = float(line[1][:-1])
	return Xcoordinate, Ycoordinate

def locationTracker(Xcoordinate, Ycoordinate):
	EasternCount = 0
	CentralCount = 0
	MountainCount = 0
	PacificCount = 0
	location = ""
	if p2[0] < Xcoordinate < p1[0] and p4[0] < Xcoordinate < p3[0]:
		if p4[1] < Ycoordinate < p2[1] and p3[1] < Ycoordinate < p1[1]:
			EasternCount += 1
			location = "Eastern"
		elif p6[1] < Ycoordinate < p4[1] and p5[1] < Ycoordinate < p3[1]:
			CentralCount += 1
			location = "Central"
		elif p8[1] < Ycoordinate < p6[1] and p7[1] < Ycoordinate < p5[1]:
			MountainCount += 1
			location = "Mountain"
		elif p10[1] < Ycoordinate < p8[1] and p9[1] < Ycoordinate < p7[1]:
			PacificCount += 1
			location = "Pacific"
	else:
		return("Location not in range")
	return location

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

def wordMatch(keywordLIST, lineTWEETList):
	happinessSCORE = 0
	NumberOfMatches = 0
	for word in keywordLIST:
		#print(section)
		for section in lineTWEETList:
			if str(word[0]).lower() == str(section).lower():
				index = keywordLIST.index(word)
				happinessSCORE = happinessSCORE + int(keywordLIST[index][1])
				print("YES MATCH")
				NumberOfMatches = NumberOfMatches + 1
				break
	if NumberOfMatches != 0:
		happinessSCORE = happinessSCORE/NumberOfMatches
	return happinessSCORE

text_file = "tweets.txt"
keyword_file = "keywords.txt" # Change this afterwards
# keyword_file = input("Enter name of keyword file: ")

infileTEXT = open(text_file, "r", encoding='utf-8', errors='ignore')
infileKEYWORD = open(keyword_file, "r", encoding='utf-8', errors='ignore')

lineKEYWORD = infileKEYWORD.readline()
lineTWEET = infileTEXT.readline()

count = 0 # not important

keywordLIST = KeywordOrganize(lineKEYWORD)

EasternScore = 0
CentralScore = 0
MountainScore = 0
PacificScore = 0

while lineTWEET != "":
	
	lineTWEET = infileTEXT.readline()
	lineTWEET.strip("\n ,.")
	lineTWEETList = lineTWEET.split(" ")
	
	Xcoordinate, Ycoordinate = coordinateValues(lineTWEET)
	
	location = locationTracker(Xcoordinate, Ycoordinate)

	score = wordMatch(keywordLIST, lineTWEETList)

	EasternScore, CentralScore, MountainScore, PacificScore = regionScore(location, score, EasternScore, CentralScore, MountainScore, PacificScore)

	print(lineTWEET)
	print(location)

			
	count = count + 1 # not important

	lineTWEET = infileTEXT.readline()
	
	print("The score of the %s tweet is %s." %(count, score)) # not important
	print("___________________________________________")


print("Eastern Score: %s \nCentral Score: %s \nMountain Score: %s \nPacific Score: %s \n" % (EasternScore, CentralScore, MountainScore, PacificScore))
print(keywordLIST)
print("The number of lines are", count)
infileTEXT.close()
infileKEYWORD.close()
