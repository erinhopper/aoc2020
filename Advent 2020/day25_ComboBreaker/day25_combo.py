import sys
import copy

import timeit

startt = timeit.default_timer()

#test case
cardpublickey = 5764801
doorpublickey = 17807724

#real case
cardpublickey = 10212254
doorpublickey = 12577395

def transform(loopsize,subjectnum=7):
	value = 1
	for i in range(loopsize):
		value = (value*subjectnum)%20201227
		#hehe sunday
	return value

#print transform(8,subjectnum=transform(11))
#for testcases, the door loopsize is 8 and the card loopsize is 11


value = 1
lsize = 1

while True:
	value = (value*7)%20201227
	if value==cardpublickey:
		cardloopsize = lsize
		print "card loopsize:",cardloopsize
		break
	lsize += 1

value = 1
lsize = 1

while True:
	value = (value*7)%20201227
	if value==doorpublickey:
		doorloopsize = lsize
		print "door loopsize:",doorloopsize
		break
	lsize += 1

print "encryption key:",transform(doorloopsize,subjectnum=transform(cardloopsize))

	
stop = timeit.default_timer()

print 'total time: ', stop-startt

#and we're done.
#thanks for everything i learned, all of december,
#the feeling when i got each new star.
#thanks for linked lists and regex and conway's game of life.
#thanks for 50 stars.
#thank you, advent of code