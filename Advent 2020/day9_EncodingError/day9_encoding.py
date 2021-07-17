import sys

infilename = "encoding.txt"

infile = open(infilename,'r')

numbers = []

while True:
	line = infile.readline()
	if not line:
		break
	numbers.append(int(line))

preamsize = 25

for ind in range(preamsize, len(numbers)): #ind will be each num we check
	preamble = numbers[ind-preamsize:ind]
	good = False
	for k in range(0,preamsize):
		for h in range(k+1,preamsize):
			if preamble[k] + preamble[h] == numbers[ind]:
				good = True
	if good == False:
		answer = numbers[ind]
		numbers = numbers[:ind]
		print "ANSWER:", answer
		break

#need n>1 contiguous numbers that sum to answer (542529149)

#pick loop through every set of two numbers to be bounds of range

def extremasum(l):
	max = l[0]
	min = l[0]
	for i in l:
		if i>max:
			max = i
		if i<min:
			min = i
	return max+min

for k in range(0,len(numbers)):
	for h in range(k+1,len(numbers)):
		if sum(numbers[k:h+1]) == answer:
			contset = numbers[k:h+1]
			print "ANSWER:",extremasum(contset)
