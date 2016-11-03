text_file = "tweets.txt"
keyword_file = "keywords.txt" # Change this afterwards
# keyword_file = input("Enter name of keyword file: ")
keywordLIST = []

infileTEXT = open(text_file, "r", encoding='utf-8', errors='ignore')
infileKEYWORD = open(keyword_file, "r", encoding='utf-8', errors='ignore')

lineKEYWORD = infileKEYWORD.readline()
lineTWEET = infileTEXT.readline()

count = 0

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

while lineTWEET != "":
	happinessSCORE = 0
	lineTWEET = infileTEXT.readline()
	lineTWEET.strip("\n ,.")
	lineTWEETList = lineTWEET.split(" ")
	print(lineTWEET)
	#print(str(keywordLIST[count][0]) + " " + str(keywordLIST[count][1]))
	for i in range(len(lineTWEET)-6):
		for x in range(len(keywordLIST)):
			if str(lineTWEET[i+6]) == str(keywordLIST[x][0]):
				happinessSCORE = happinessSCORE + int(keywordLIST[x][1])
	count = count + 1
	print("The score of the %s tweet is %s." %(count, happinessSCORE))


print(keywordLIST)

infileTEXT.close()
infileKEYWORD.close()
