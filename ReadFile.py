class FileReader():
	def ReadFile(filename):
		try:
			infile = open(filename, "r")
			nextLine = infile.readline()
		except IOError:
			print("File " + filename + " cannot be read.")
		except exception:
			print("File " + filename + " not found.") 

	def readline():
		current = nextLine
		try:
			nextLine = infile.readline()
		except IOError:
			print("File cannot be read.")

		return current

	def EOF():
		if current == None:
			return current == None

	def close():
		try:
			inflie.close()
		except IOError:
			print("Problem closing file")

