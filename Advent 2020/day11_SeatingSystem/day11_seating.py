import sys

infilename = "seating.txt"

infile = open(infilename,'r')

seating = []

while True:
	line = infile.readline()
	if not line:
		break
	seating.append(line[:-1])
	
#RULES:
#-if all seats around are empty, the seat will become full
#-if 4+ seats around are full, the seat will become empty

height = len(seating)#HEIGHT GOES WITH ROW #
width = len(seating[0])#WIDTH GOES WITH COLUMN #

def countadj(row,col,tocount):
	count = 0
	for j in range(-1,2):
		for k in range(-1,2):
			#if it's not off the edge or the same square 
				if (row + j) < height and (row + j) >= 0 and (col + k) < width and (col + k) >= 0:
					if not (k==0 and j==0):
						if tocount[row+j][col+k] == "#":
							count += 1
	return count

def countsee(row,col,tocount):
	count = 0
	for j in range(-1,2):
		for k in range(-1,2):
			#if it's not the same square
			if not (k==0 and j==0):
				away = 1
				while True:
					#if it's not off the edge
					if (row + away*j) < height and (row + away*j) >= 0 and (col + away*k) < width and (col + away*k) >= 0:
						if tocount[row+away*j][col+away*k] == "#": #if they see a person
							count += 1
							break
						elif tocount[row+away*j][col+away*k] == "L": #if they see a chair
							break
					else: #you've hit the edge
						break
					away += 1
	return count

def fixstr(string,ind,character):
	l = list(string)
	l[ind] = character
	return "".join(l)

def printseating(seats):
	print ""
	for i in seats:
		print i
	print ""

iters = 0

while True:
	iters += 1
	last = seating[:]
	#printseating(last)
	for r in range(height):
		for c in range(width):
			if last[r][c] != '.':
				people = countsee(r,c,last)
				if last[r][c] == "#" and people >= 5:
					seating[r] = fixstr(seating[r],c,'L')
				elif last[r][c] == "L" and people == 0:
					seating[r] = fixstr(seating[r],c,'#')
	if last == seating:
		break

total = "".join(seating)

print total.count("#")		