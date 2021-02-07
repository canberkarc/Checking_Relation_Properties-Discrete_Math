def main_func(input_filename, output_filename):
	file = open(input_filename, "r")
	lines = file.readlines() # Read all lines from file

	# Detect how many lines are there in file
	count = 0
	for line in lines: 
		count += 1
	file.close()


	file = open(input_filename, "r")
	line = file.readline()
	
	# Loop to read contents from file
	# Number of relations to relationNum
	# Sets to sett
	# Relations to relations
	# relasetNum is a counter for sets
	count2 = 1 
	relaSetNum = 1
	relationNum = 0
	sett = []
	relations = []
	while (count2 != count):

		count2 += 1
		# Check if a valid input is read, otherwise print error message and exit
		if((line != "\n") and (line != "") and line[0].isnumeric() ):
			relationNum = int(line) # Read number of relations in relationNum
		elif(line == ""):
			break
		else: # If something entered that not expected, print Error!.
			print("Error, something entered that not expected!\n")
			

		# Read line, parse it and put its contents(just required ones) into list sett 
		line = file.readline()
		l = line.strip(",")
		for i in range(0,len(l),2):
			sett.append(l[i])
		sett.append("-") # This is for seperating sets

		# Length of list sett
		lenSett = len(sett)

		# Read relations into list relations
		for i in range(0,relationNum):
			line = file.readline()
			l = line.strip(",")
			relations.append((l[0],l[2]))
			count2 += 1 # Increment count2 for loop
		relaSetNum += 1 # Increment number of sets
		relations.append("-") # This is for seperating relations
		line = file.readline()
	file.close()

	out_file = open("output.txt","w") # Open output.txt in write mode

	ii = 0
	jj = 0
	sets = []
	relationss = []
	for i in range(1,relaSetNum):	 
		while (sett[ii] != "-"): # Get sets respectively from list sett to list sets, list sets will be empty after each iteration
			sets.append(sett[ii])
			ii += 1

		while (relations[jj] != "-"): # Get relations respectively from list relations to list relationss, list relations will be empty after each iteration
			relationss.append(relations[jj])
			jj += 1

		# Write to file
		out_file.write("n\n")
		for kx in relationss: # Write relations
			ss = "(" + str(kx[0]) + "," + str(kx[1]) + ")"
			out_file.write(ss)
		out_file.write("\n")

		if(checkError(sets,relationss) == True): # Check for error
			checkReflexivity(out_file, sets,relationss) #Reflexivity function
			checkSymmetric(out_file,relationss) #Symmetric function
			checkAntisymmetric(out_file,relationss) #Antisymmetric function
			checkTransitive(out_file,relationss) #Transitive function
		else:
			# If there is any error then print error for this input and go to next input
			out_file.write('Error! Unmatch between sets and their relations')
			break

		# Reset sets list for next sets
		if(ii != (lenSett - 1)): 
			ii += 1
			sets = [] # Reset sets list for next set
		
		# Reset relationss list for next relations	
		jj += 1
		relationss = [] # Reset relationss list for next relations
	out_file.close()

# Check if there is any unmatch between sets and their relations
def checkError(sets,relationss):
	ind1 = 0
	ind2 = 0
	chVal = True

	# Check if there is any other element from set in relations
	for ind1 in range(len(relationss)): # Loop of length relations
		for ind2 in range(0,2): # To reach elements of relations
			count = 0
			for k in sets: # Loop through set elements
				if(relationss[ind1][ind2] != k): # If elements of relation are different from all elements in set
					count += 1					 # count will be equal to length of sets and function will return False
			if(count == len(sets)):				 # otherwise will return True
				chVal = False
	return chVal			

def checkReflexivity(fp,sets,relationss):
	# In first loop, I take one element of set, let's call it as x. 
	# Then I search for (x,x) in relations, if there is then make checkVal "True" else it'll remain as False
	for k in sets:
		checkVal = False
		for i in relationss:
			if((i[0] == i[1]) and (i[0] == k) and (i[1] == k)):
				checkVal = True
	#If checkVal is False then print sentence and exit
		if(checkVal == False):
			fp.write("Reflexive: No because ({},{}) is not found.\n".format(k,k))
			return checkVal
	#If all relations are checked and all reflexive relations are present then print sentence and exit.
	fp.write("Reflexive: Yes, all elements are present.\n")
	return checkVal

def checkSymmetric(fp,relationss):
	#If vice versa of (x,y) in relations does not exist then there is no symmetry
	for (x, y) in relationss:
		if (y, x) not in relationss:
			fp.write("Symmetric: No, ({}, {}) is not found whereas ({}, {}) is found.\n".format(y,x,x,y))
			return False
	#If all relations are checked and there is nothing breaks symmetry
	fp.write("Symmetric: Yes, symmetrics of each pair are found.\n")
	return True

def checkAntisymmetric(fp,relationss):
	truee = [] # List to store elements that are printed if check is yes
	check = False # Antisymmetry check condition
	
	# With nested loop in relations, I compare if there is any antisymmetry or not and ignore same x and y(for example (a,a))
	for (x,y) in relationss:
		for (a,b) in relationss:
			if ((x != y) and (x == b) and (y == a)): # If there is an example that breakes antisymmetry
				fp.write("Antisymmetric: No, ({}, {}) is found whereas ({}, {}) is found.\n".format(y,x,x,y))
				check = False
				return False
			if((x != y) and ((x != b) or (y != a))):
				truee.extend([y,x,x,y])
				check = True
		
	if(check == True): #If all relations checked and there is antisymmetry
		fp.write("Antisymmetric: Yes, ({}, {}) is not found whereas ({}, {}) is found.\n".format(truee[0],truee[1],truee[2],truee[3]))
	else: # If all relations are reflexive
		fp.write("Antisymmetric: Yes, all relations consist of reflexive relations\n")	
		
def checkTransitive(fp,relationss): 
	truee = []
	count = 0
	
	# Check if all relations are reflexive, if count is equal to length of relations then all relations are reflexive.
	for i in relationss:
		if(i[0] == i[1]):
			count += 1

	if(count == len(relationss)):
		fp.write("Transitive: Yes, all relations are reflexive and there is no other relation.\n")
	else:
		# If not, with nested loop, check if there is any transitive relation without checking relations that have same elements
		# for example (a,a). If there is no transitive relation then print message and exit.
		for (a,b) in relationss:
			for (c,d) in relationss:
				if ((b == c) and (a != b) and ((a,d) in relationss)):
					truee.extend([a,d,a,b,c,d]) # Put values to print in sentence if there is transitivity
				elif((b == c) and (a != b) and ((a,d) not in relationss)):
					fp.write("Transitive: No, ({}, {}) is not found whereas ({}, {}) and ({}, {}) are found.\n".format(a,d,a,b,c,d))
					return False
		# If all relations are checked and there is transitivity, print message
		fp.write("Transitive: Yes, ({}, {}) is found whereas ({}, {}) and ({}, {}) are found.\n".format(truee[0],truee[1],truee[2],truee[3],truee[4],truee[5]))

if __name__ == '__main__':
	main_func("input.txt","output.txt")