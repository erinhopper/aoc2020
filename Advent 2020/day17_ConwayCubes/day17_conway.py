import sys
import copy
import timeit

startt = timeit.default_timer()

infilename = "conway.txt"

infile = open(infilename,'r')

dimension = []

while True:
	line = infile.readline()
	if not line:
		break
	dimension.append(list(line[:-1]))

ons = {}
maxx = 0
minx = 0
maxy = 0
miny = 0
maxz = 0
minz = 0
maxw = 0
minw = 0

#print dimension
for i in range(len(dimension)):
	if i > maxx:
		maxx = i
	if i< minx:
		minx = i
	for k in range(len(dimension[i])):
		if k > maxy:
			maxy = k
		if k< miny:
			miny = k
		if dimension[i][k] == '#':
			ons[(i,k,0,0)] = True

xoffset = 1
yoffset = 1
zoffset = 1

#each of these offsets is what you can add to the indecies of each to 

#RULES:
#-if cube is active + exactly 2 or 3 neighbors are active:
#--stays active, else inactive
#-if cube is inactive and exactly 3 neighbors are active:
#--becomes active, else inactive

#dim one is 
def replaceextrema(x,y,z,w):
	global maxx,minx,maxy,miny,maxz,minz,maxw,minw
	#print 'replacing'
	if x<minx:
		minx = x
	if x>maxx:
		maxx = x
	if y<miny:
		miny = y
	if y>maxy:
		maxy = y
	if z<minz:
		minz = z
	if z>maxz:
		maxz = z
	if w<minw:
		minw = w
	if w>maxw:
		maxw = w


def countneighbors(x1,y1,z1,w1,old=False,printing=False):
	count = 0
	for x in range(-1,2):
		for y in range(-1,2):
			for z in range(-1,2):
				for w in range(-1,2):
					if not (x == 0 and y==0 and z==0 and w == 0):
						try:						
							#print "trying,", [x+x1,y+y1,z+z1]
							if old == False:
								d = ons[(x+x1,y+y1,z+z1,w+w1)]
							else:
								d = lastons[(x+x1,y+y1,z+z1,w+w1)]
							if d == True:
								count +=1
								if printing == True:
									print x+x1,y+y1,z+z1,w+w1
							#break
						except KeyError:
							pass
	return count
#print ons		
#print countneighbors(0,0,0)
#print countneighbors(2,1,0)

orig = ons.copy()

for imnotgonnawastei in range(0,6):
	#NEW ROUND
	#every round lets just add a row in each dimension
	#who  cares anymore.
	
	lastons = copy.deepcopy(ons)
	
	#check all the ones that are on
	for cube in ons.keys():
		c = countneighbors(cube[0],cube[1],cube[2],cube[3],old=True)
		if c != 2 and c != 3:
			#turn it off
			ons.pop(cube)
	xr = range(minx-1,maxx+2)
	yr = range(miny-1,maxy+2)
	zr = range(minz-1,maxz+2)
	wr = range(minw-1,maxw+2)
	#and all the ones that are off. god i hate it here
	#print xr,yr,zr
	for x in xr:
		for y in yr:
			for z in zr:
				for w in wr:
					#if (x,y,z)==(2,2,1):
						#print 'THERE'
					try:
						d = lastons[(x,y,z,w)]
						#break
					except KeyError:
						#if (x,y,z)==(2,2,1):
							#print "THERE EXCEPT"
							
						c = countneighbors(x,y,z,w,old=True)
						if c == 3:
							#turn it on
							ons[(x,y,z,w)] = True
							replaceextrema(x,y,z,w)
	#and now we're done. thank fucking god

#print orig
print len(ons)
#print ons

stop = timeit.default_timer()

print 'total time: ', stop-startt
	
	


