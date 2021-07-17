import sys
import copy

infilename = "messagestest2.txt"
infilename = "messages.txt"


infile = open(infilename,'r')

rules = {}
messages = []
on = 0
while True:
	line = infile.readline()
	if not line:
		break
	if line == '\n':
		on += 1
	elif on == 0:
		splitter = line.index(":")
		rulenum = int(line[:splitter])
		rule = line[splitter+2:-1]
		rules[rulenum]=rule
	else:#on == 1
		messages.append(line[:-1])

#first letss uhhhhh parse the rules?
#god i hate it here.
#all i do is s u f f e r
#anyway

for current in rules.keys():
	r = rules[current]
	if '"' in r:#single character
		rules[current] = (0,r.replace('"',''))
	elif '|' in r:#ors!!
		splitter = r.index("|")
		#print r[:splitter].split(" ")
		first = [int(k) for k in r[:splitter-1].split(" ")]
		second = [int(k) for k in r[splitter+2:].split(" ")]
		rules[current] = (1,(first,second))
	else:#it's a pointer or an and (which is like the same thing)
		nums = [int(k) for k in r.split(" ")]
		rules[current] = (2,nums)

#FOR PART TWO ONLY
rules[8] = (1,([42],[42,8]))
rules[11] = (1,([42,31],[42,11,31]))

def andrule(data,string,extr=True):
	left = string
	for i in data: #each rulenumber
		if left == True:
			return False
			#ran out of space before finishing rules!!
		
		left = works(i,left,extra=True)
		if left == False:
			return False
	#if we're still alive
	if left == True:
		#we finished the string! beautiful
		return True
	elif extr == True:
		#we have extra but it's allowed and wanted
		return left
	else:
		return False
		#we have extra but it's illegal
	

def works(rulenum, string, extra = True):
	r = rules[rulenum]
	type = r[0]
	data = r[1]
	
	if rulenum == 8: #SPECIAL CASE
		saved = []
		ch = True
		left = string
		while True:
			ch = works(42,left,extra=True)
			if ch==False:
				break
			if ch == True:
				saved.append([])
				break
			left = ch
			saved.append(left)
			
		if len(saved) == 0:
			return False #we never got one
		else:
			return saved#oh no.
		
	elif rulenum == 11:#SPECIAL CASE
		saved = [string]
		ch = True
		ch1 = False
		ch2 = False
		left = string
		brokeon = 1
		while True:
			ch1 = works(42,left,extra=True)
			if ch1 == False or ch1 == True:
				brokeon = 1
				break
			#now ch1 must be the string of what's left
			ch2 = works(31,ch1,extra=True)
			if ch2 == False:
				brokeon = 2
				break
			if ch2 == True:
				brokeon = 2
				saved.append([])
				break
			#now ch2 must be the string of what's left
			left = ch2
			saved.append(left)
		
		#now we have to check everything in left
		if len(saved) == 0:
			return False #we never got one
		#if brokeon == 1:#
		#	return False
		if ch2 == False:
			return False
		else:
			return saved#oh no.
				
	if type == 0: # single character
		if string[0] == data:
			if len(string)== 1:
				return True
			elif extra == True:
				return string[1:]
			else:
				return False #extra is illegal :(
		else:
			return False
	
	elif type == 1:#or
		
		first = andrule(data[0],string,extr=extra)
		if first == True:
			return True
		elif first != False and extra == True:
			#first had leftovers
			return first
		second = andrule(data[1],string,extr=extra)
		if second == True:
			#at least one worked with no extra
			return True
		elif second != False and extra == True:
			#first had leftovers
			return second
		else:
		#either both returned false or it had extra when it wasn't supposed to
			return False
	else:#and
		return andrule(data, string, extr=extra)

#toprint = [8,42,11,31]
#for i in toprint:
#	print i,rules[i]
#print rules
#print messages
sum11 = 0
sum8 = 0
for i in messages:
	listof8s = works(8,i,extra=True)
	#print listof8s
	if listof8s != False:
		sum8 += 1
		for k in listof8s:
			if k != []:
				if works(11,k,extra=False)!=False:
					#print "WORKS"
					sum11 += 1
					print k
					print i
					print ''
					break

print sum8,sum11
