import sys

infilename = "customsforms.txt"

infile = open(infilename,'r')

total = 0
yesses = []
news = []
saved = []
firstline = True
while True:
	line = infile.readline()
	if not line:
		break
	if line == "\n":
		total += len(set(yesses))
		#print set(yesses)
		yesses = []
		firstline = True
	else:
		if firstline == True:
			yesses += list(line[:-1])
			if line[-1]!= "\n":
				yesses += [line[-1]]
			firstline = False
		else:
			news += list(line[:-1])
			if line[-1]!= "\n":
				news += [line[-1]]
			#print news, yesses
			for i in news:
				if i in yesses:
					saved.append(i)
					
			yesses = saved[:]
			saved = []
			news = []
		
	

total += len(set(yesses))
#print set(yesses)
print total