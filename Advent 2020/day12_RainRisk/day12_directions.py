import sys
import math

infilename = "directions.txt"

infile = open(infilename,'r')

dirs = []

while True:
	line = infile.readline()
	if not line:
		break
	dirs.append(line[:-1])
	
	
def rotate(pair,amount):
	amount = amount%360
	if amount == 0:
		return pair
	elif amount == 90:
		return [pair[1]*-1,pair[0]]
	elif amount == 180:
		return [pair[0]*-1,pair[1]*-1]
	elif amount == 270:
		return [pair[1],pair[0]*-1]

	
shipposition = [0,0]
waypointdistances = [10,1]#RELATIVE TO THE SHIP

#EAST-WEST,NORTH-SOUTH
#DOES NOT CHANGE

direction = 0

#0 - east is forward (+0, mod 4)
#90 - north is forward (+1, mod 4)
#180 - west is forward (+2, mod 4)
#270 - south is forward (+3, mod 4)

#LEFT IS POSITIVE, RIGHT IS NEGATIVE
#print dirs

for current in dirs:
	action = current[0]
	value = int(current[1:])
	#print action, value
	if action == 'R':
		waypointdistances = rotate(waypointdistances,value*-1)
		
	elif action == 'L':
		waypointdistances = rotate(waypointdistances,value)
		
	elif action == 'F':
		shipposition[0] += (waypointdistances[0] * value)
		shipposition[1] += (waypointdistances[1] * value)
	
	elif action == 'N':
		waypointdistances[1] += value
	elif action == 'S':
		waypointdistances[1] -= value
	elif action == 'E':
		waypointdistances[0] += value
	elif action == 'W':
		waypointdistances[0] -= value
		
	else:
		print "something is wrong"		
		
ew = abs(shipposition[0])
ns = abs(shipposition[1])

print ew, ns
print ew + ns