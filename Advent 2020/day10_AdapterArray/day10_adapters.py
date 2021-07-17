import sys

infilename = "adapters.txt"

infile = open(infilename,'r')

numbers = [0]

while True:
	line = infile.readline()
	if not line:
		break
	numbers.append(int(line))
	
numbers.sort()

def product(l):
	total = 1
	for i in l:
		total *= i
	return total

def is_valid(l):
	for i in range(0,len(l)-1):
		if (l[i+1]-l[i])>3:
			return False
	return True

numbers.append(numbers[-1]+3)

ones = 0
twos = 0
threes = 0 #for the end, which is always three

ps = []

for i in range(0,len(numbers)-1):
	diff = numbers[i+1]-numbers[i]
	
	if diff == 0:
		print "SAME ADAPTER??"
	elif diff == 1:
		ones += 1
	elif diff == 2:
		twos += 1
	elif diff == 3:
		threes += 1
		ps.append(i+1)
	else:
		print "DIFF WEIRD",diff

print "ANSWER ONE:",ones*threes

partitions = [numbers[0:ps[0]]]

for i in range(0,len(ps)-1):
	partitions.append(numbers[ps[i]:ps[i+1]])

partitions.append(numbers[ps[-1]:])

each = []

for current in partitions:
	#solve the case for current: figure out how many possibilities there are
	if len(current) < 3:
		possibilities = 1
	else:
		possibilities = 0
		inners = len(current)-2 #number of ones we can take out
		for i in range(2**inners):
			currenttesting = [current[0]]
			#USE BINARY COUNTING SCHEME
			#i is which ones should be 'on' (in use)
			#and off (not in use)
			for adapter in range(inners):
				if i & (1<<adapter):
					currenttesting.append(current[1+adapter])
			currenttesting.append(current[-1])
			if is_valid(currenttesting):
				possibilities += 1	
	each.append(possibilities)

#print partitions
#print each
print "ANSWER TWO:", product(each)

	