import sys
import copy

import timeit

startt = timeit.default_timer()

infilename = "tiling.txt"


infile = open(infilename,'r')

#first, read in the data and separate out each direction correctly

directions = []

while True:
	line = infile.readline()
	if not line:
		break
	pointer = 0
	directions.append([])
	while pointer<len(line[:-1]):
		if line[pointer]=='s' or line[pointer]=='n':
			#next two
			directions[-1].append(line[pointer:pointer+2])
			pointer += 2
		else:
			#next one
			directions[-1].append(line[pointer])
			pointer += 1
		
#print directions
#print len(directions)
	
#each hexagon can be stored as three numbers:
#the distance from the origin in each of three directions:
#northeast, southeast, and east

blacktiles = []

#second, for each hex: 
#loop through the data, add and store three sep variables for each direction
for d in directions:
	e=0
	n=0
	for current in d:
		if current == "ne":
			n += 1
			e+=1
		elif current == "sw":
			n-= 1
			e -= 1
		elif current == "e":
			e += 2
		elif current == 'w':
			e -= 2
		elif current == 'se':
			n -= 1
			e += 1
		elif current == 'nw':
			n += 1
			e -= 1

		
		#third, have a list of all the current black ones. 
		#if it's in the list, take it out. else, put it in.
	if (e,n) in blacktiles:
		blacktiles.remove((e,n))
	else:
		blacktiles.append((e,n))
		
		
#print blacktiles
print len(blacktiles)

#DO NOT CHANGE ABOVE
#now for ~conway!!~

maxe = 0
mine = 0
maxn = 0
minn = 0

#set original extrema
for i in blacktiles:
	print i
	if i[0]>maxe:
		maxe = i[0]
		print "maxe = ",i[0]
		
	if i[0]<mine:	
		mine = i[0]
		print "mine = ",i[0]

	if i[1]>maxn:
		maxn = i[1]
		print "maxn = ",i[1]

	if i[1]<minn:
		minn = i[1]
		print "minn = ",i[1]


print ""
print maxe,mine,maxn,minn
print ""

def getneighbors(orig,blacks):
	count = 0
	e = orig[0]
	n = orig[1]
	#ne
	if (e+1,n+1) in blacks:
		count += 1
	#e
	if (e+2,n) in blacks:
		count += 1
	#se
	if (e+1,n-1) in blacks:
		count += 1
	#sw
	if (e-1,n-1) in blacks:
		count += 1
	#w
	if (e-2,n) in blacks:
		count += 1
	#nw
	if (e-1,n+1) in blacks:
		count += 1
	
	return count
	
def isvalid(tile):
	#checks if it's a valid tilenum
	#(basically same parity)
	if tile[0]%2==tile[1]%2:
		return True
	return False
	
#print isvalid((-3,1))
#print isvalid((0,1))

def replaceextrema(e,n):
	global maxe,mine,maxn,minn
	#print 'replacing'
	if e<mine:
		mine = e
	if e>maxe:
		maxe = e
	if n<minn:
		minn = n
	if n>maxn:
		maxn = n

#'it's all conway's game of life'
#'always has been'

#RULES:
#-if tile is black and it has 0 or >2 black tiles touching it:
#--turn white
#-if tile is white and has two black tiles touching it:
#--turn black

#print blacktiles


for imnotgonnawastei in range(1,101):
	#NEW ROUND
	#who  cares anymore.
	
	lastblacks = copy.deepcopy(blacktiles)
	#check all the ones that are black
	for btile in lastblacks:
		c = getneighbors(btile,lastblacks)
		if c == 0 or c > 2:
			#turn it to white
			blacktiles.remove(btile)
			
	er = range(mine-1,maxe+2)
	nr = range(minn-1,maxn+2)
	
	
	
	#and all the ones that are white
	#print mine,maxe,minn,maxn
	for e in er:
		for n in nr:
			if isvalid((e,n)):
				if (e,n) not in lastblacks:	#if it's white		
					c = getneighbors((e,n),lastblacks)
					if c == 2:
						#turn it on
						blacktiles.append((e,n))
						replaceextrema(e,n)
			else:
				#print (e,n)
				pass
	#and now we're done. thank fucking god
	
	print ""
	print 'round',imnotgonnawastei,'tiles',len(blacktiles)
	
stop = timeit.default_timer()

print 'total time: ', stop-startt
