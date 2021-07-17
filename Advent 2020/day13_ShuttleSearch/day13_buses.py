import sys
import math

infilename = "buses.txt"

infile = open(infilename,'r')

dirs = []


line = infile.readline()
time = int(line)
line = infile.readline()

def greatest(l):
	sofar = l[0]
	for i in l:
		if sofar<i:
			sofar = i
	return sofar
	
def sum(l):
	total = 0
	for i in l:
		total += i
	return total
	
def product(l):
	total = 1
	for i in l:
		total *= i
	return total
	
def check(nums, ans):
	for i in nums:
		if (ans)%i[0] != i[1]:
			return False
	return True
		
buses = line.split(",")

nums = []

aftertime = 0
for i in buses:
	try:
		a = int(i)
		nums.append([int(a),aftertime%int(a)])
	except ValueError:
		pass
	aftertime += 1

print nums

max = 983
maxoffset = 17

#minute = max-maxoffset
#
#while True:
#	didit = True
#	for i in nums:
#		if (minute+i[1])%i[0] != 0:
#			didit = False#one didn't work :(
#			break
#	if didit == True:
#		print minute
#		break
#	#print minute
#	minute += max
	
chunks = []
zeroes = [i[0] for i in nums]
ones = [i[1] for i in nums]
prodzers = product(zeroes)

for i in nums:
	canceling = prodzers/i[0]
	#canceling makes it invisible to everything else
	#now we need to make canceling % i[0] = i[1]
	orig = canceling
	inc = 2
	#print canceling%i[0]
	#print canceling, i[0], prodzers
	while canceling%i[0] != i[1]:
		if canceling%i[0] == 1:
			canceling *= i[1]
		else:
			canceling = orig*inc
		inc += 1
		if inc>i[0]:
			print "failed"
			exit(0)
	#print "out of cancel",i
	#JUST A CHECK:
	#canceling should be i[1] mod i[0] and 0 mod everything else
	if canceling % i[0] != i[1]:
		print "BAD"
		break
	for k in zeroes:
		if canceling % k != 0:
			if k != i[0]:
				print "BAD2"
				break
	#ok we're good
	chunks.append(canceling)

#print chunks
s = sum(chunks)
print check(nums, s)
plusminus = product(zeroes)

while s > plusminus:
	s -= plusminus

print plusminus-s
