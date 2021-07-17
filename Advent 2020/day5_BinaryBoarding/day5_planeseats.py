import sys

infilename = "planeseats.txt"

infile = open(infilename,'r')

#greatest = 0
ids = []
while True:
	line = infile.readline()
	if not line:
		break
		
	row = 0
	column = 0
	
	place = 6
	for i in list(line[:7]):
		if i == 'B':
			row += 1<<place
		place -= 1
		
	place = 2
	for i in list(line[7:10]):
		if i == 'R':
			column += 1<<place
		place -= 1
	
	seatid = row*8 + column
	ids.append(seatid)
	#if seatid>greatest:
	#	greatest = seatid
	
possibilities = []
for i in range(1024):
	if i not in ids:
		possibilities.append(i)
#print greatest
print possibilities