import sys

infilename = "tobogganslope.txt"

infile = open(infilename,'r')

slope = []
while True:
	line = infile.readline()
	if not line:
		break
	slope.append([])
	for i in list(line[:-1]):
		if i == '.':
			slope[-1].append(False)
		elif i == "#":
			slope[-1].append(True)

l = len(slope[0])

def trees(right, down):
	treeshit = 0
	ind = 0
	
	for i in range(0,len(slope),down):
		if slope[i][ind%l] == True:
			treeshit += 1
		ind += right
	
	return treeshit

fir = trees(1,1)
se = trees(3,1)
th = trees(5,1)
fo = trees(7,1)
fit = trees(1,2)

print fir,se,th,fo,fit

print fir*se*th*fo*fit