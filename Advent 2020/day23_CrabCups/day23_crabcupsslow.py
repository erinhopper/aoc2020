import timeit

startt = timeit.default_timer()

#test
cups = [3,8,9,1,2,5,4,6,7]
numturns = 100

cups = cups+range(10,1000001)
numturns = 10000000

#real
lcups = 9
lcups = 1000000
#print cups

#cups = [2,4,7,8,1,9,3,5,6]
numturns=100

def move(order,currentind):
	#print "cups:",order

	#first, pick up the three cups clockwise (to the right)
	#print currentind
	current = order[currentind]
	first = order[((currentind+1)%lcups)]
	second = order[((currentind+2)%lcups)]
	third = order[((currentind+3)%lcups)]
	
	order.remove(first)
	order.remove(second)
	order.remove(third)
	
	#print "pick up:",first,second,third
	#second, select a destination cup
	destination = (current-2)%lcups+1
	while destination == first or destination == second or destination == third:
		destination = (destination-2)%lcups+1

	#print "destination:",destination
	#third, put your selected cups back down
	#to the right of the selected cup

	ind = order.index(destination)
	order[ind+1:ind+1] = [first,second,third]
	#and return the current order
	return order,current

currentind = 0
for i in range(numturns):
	#print ""
	#print "move",i+1
	cups,c = move(cups,currentind)
	currentind = (cups.index(c)+1)%lcups

	
#print cups

stop = timeit.default_timer()

print 'total time: ', stop-startt