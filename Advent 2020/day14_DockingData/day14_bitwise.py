import sys
import math

infilename = "bitwise.txt"

infile = open(infilename,'r')

def sum(l):
	total = 0
	for i in l:
		total += i
	return total

def bitmask(masksep, number):
	masked = (number & masksep[0]) | masksep[1]
	return masked
	
def makemasks1(mask):
	current = 0
	zeroes = 0
	ones = 0
	for i in mask[::-1]:
		if i == 'X':#1 for zeroes, 0 for ones
			zeroes = zeroes | (1<<current) 
		elif i == '1':#1 for both
			zeroes = zeroes | (1<<current) 
			ones = ones | (1<<current)
		current += 1
	return [zeroes,ones]

def makemasks2(mask):
	current = 0
	new = 0
	xs = []
	for i in mask[::-1]:
		if i == '1':#1 for both
			new = new | (1<<current)
		elif i == 'X':
			xs.append(current)
		current += 1
	
	return [new,xs]
	#returns: the mask with all the x's are 0s (for or-ing)
	#and a list of where are the x's are

def getmems(masksep, number):
	#first: apply the basic part of the mask (all the floating bits are the same)
	perfect = number | masksep[0]
	#second: deal with the float bits
	x_s = masksep[1]
	numfloats = len(x_s)
	each = []
	for pattern in range(1<<numfloats):
		#for each pattern
		on = perfect
		for bit in range(numfloats): #for each index
			value = ((1<<bit) & pattern)>>bit#get whether its a 1 or 0
			babymask = 1 << x_s[bit] #put it in the right place
			#and insert it into on
			#print 'val =', value, 'babymask = ', babymask
			if value == 1:
				on = on | babymask
			else: #value = 0
				origvalue = (on & babymask)>> x_s[bit]
				#print origvalue
				if origvalue == 1:
					on -= babymask
		#print bin(on)		
		each.append(on)
	return each


t = makemasks2('00X1001X')
print bin(t[0]), t[1]
s = getmems(t, 42)
print s
for i in s:
	print bin(i)

#t = makemasks1('XX0XX11X')
#print bin(t[0]), bin(t[1])
#print bin(bitmask(t,107))


mem = {}


while True:
	line = infile.readline()
	if not line:
		break
	if line[1] == "a": #mask
		mask = line[6:-1]
		#masksep = makemasks1(mask)
		masksep = makemasks2(mask)
		#print bin(masksep[0]), bin(masksep[1])

		#do something here to set it up:
		#make two numbers to act as bitmasks: 
		#one that has ones in all the right places and zeroes elsewhere (to and)
		#and one that has zeroes in all the right places and ones elsewhere (to and)
	elif line[1] == 'e': #mem
		ind = int(line[line.index('[')+1:line.index(']')])
		value = int(line[line.index('=')+1:])
		
		all = getmems(masksep, ind)
		
		for i in all:
			mem[i] = value
		#mem[ind] = bitmask(masksep, value)
		
	else:
		break

print mem
print sum(mem.values())
	