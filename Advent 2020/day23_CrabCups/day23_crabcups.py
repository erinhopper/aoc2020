
import sys
import timeit

startt = timeit.default_timer()

#test
cups = [3,8,9,1,2,5,4,6,7]
#real
cups = [2,4,7,8,1,9,3,5,6]
cups = cups+range(10,1000001)
numturns = 10000000

lcups = 9
lcups = 1000000
#print cups




def move(order,current):
	#fix this whole fucking thing
	#print "cups:",makepretty(order)

	#first, pick up the three cups clockwise (to the right)
	#BY CHANGING THE POINTER of CURRENT TO SKIP THEM
	#AND STORING THE CUP VALUES IN VARIABLES
	
	
	first = order[current]
	second = order[first]
	third = order[second]
	
	order[current] = order[third]
	
	#print "pick up:",first,second,third
	
	
	#second, select a destination cup
	#AHHHHHHHH
	destination = (current-2)%lcups+1
	while destination == first or destination == second or destination == third:
		destination = (destination-2)%lcups+1

	#print "destination:",destination
	
	#third, put your selected cups back down
	#to the right of the selected cup
	#by switching two pointers

	todaleft = destination
	todaright = order[destination]
	
	order[todaleft] = first
	order[third] = todaright
	
	#and return the current order
	return order,order[current]

def makepretty(pointers):
	#print pointers
	current = [0]*(len(pointers)-1)
	current[0] = pointers[1]
	for i in range(0,len(current)-1):
		current[i+1]=pointers[current[i]]
	return current
		
	
def makepointers(pretty):
	current = [0]*(len(pretty)+1)
	for i in range(len(pretty)-1):
		current[pretty[i]] = pretty[i+1]
	current[pretty[-1]] = pretty[0]
	return current
	 
#AHHHHH
#lets make this into a method with pointers!
#i wanna die
current = cups[0]
cups = makepointers(cups)


for i in range(numturns):
	#print ""
	#print "move",i+1
	cups, current = move(cups,current)
	
print makepretty(cups)

f = cups[1]
s = cups[f]
print f,s,f*s

stop = timeit.default_timer()

print 'total time: ', stop-startt