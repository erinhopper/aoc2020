import timeit

startt = timeit.default_timer()

#TEST
start = [0,3,6]

#REAL
start = [18,11,9,0,5,1]

turnnum = len(start)+1

reciting = start[:]

lasts = {}
for i in range(len(start)-1):
	lasts[start[i]] = i

#print lasts

numbersaid = start[-1]

while turnnum<30000001:
	if numbersaid not in lasts:#never been said before
		lasts[numbersaid] = turnnum-2#put in yesterday's number
		numbersaid = 0#the number goes back to 0

	else:#has been said before
		#lasttime = len(reciting)-reciting[:-1][::-1].index(reciting[-1])#2 greater than real
		#FIRST, FIND THE DIFFERENCE BETWEEN THE TWO (THIS TIME'S NUMBER)
		n = turnnum-lasts[numbersaid]-2
		#THEN, PUT YESTERDAY'S NUMBER INTO LASTS
		lasts[numbersaid] = turnnum-2
		numbersaid = n

	#print turnnum, lasts[numbersaid],numbersaid

	#print turnnum,numbersaid

	turnnum += 1
	#print lasts
	
print numbersaid
#print lasts

stop = timeit.default_timer()

print 'total time: ', stop-startt