import sys
import math

infilename = "tickets.txt"

infile = open(infilename,'r')

dirs = []

on = 0
allrules = []
tickets = []
chunkedrules = []
while True:
	line = infile.readline()
	if not line:
		break
	if line == "\n":
		on += 1
	elif line[0] == 'y' or line[0] == 'n':
		pass #boring, all words only
	elif on == 0:
		split = line.index("or ")
		l = len(line[:split])

		first = int(line[line.index(":")+1:line.index("-")])
		second = int(line[line.index("-")+1:line.index("or ")])

		third = int(line[split+3:line[split:].index("-")+l])
		fourth = int(line[line[split:].index("-")+l+1:])
		
		#chunks them together by field
		chunkedrules.append(((first, second),(third, fourth)))
		
		allrules.append((first, second))
		allrules.append((third, fourth))
	else: #taking in a ticket
		t = line.split(',')
		tick = [int(i) for i in t]
		#print tick
		tickets.append(tick) 
		
allowed = set()
for i in allrules:
	allowed.update(set(range(i[0],i[1]+1)))

errorrate = 0
bad = []

for i in range(0,len(tickets)):
	for k in tickets[i]:
		if k not in allowed:
			errorrate += k
			bad.append(i)
			#print k

for i in bad[::-1]:#loop through bad backwards
	tickets.pop(i)

#now all the bads should be gone
#lets check:
bads = 0
for i in range(0,len(tickets)):
	for k in tickets[i]:
		if k not in allowed:
			bads += 1
			#print k
if bads != 0:
	print 'SOMETHING BAD HAPPENED'
	exit(0)

#now, we wanna kinda fix some variables:
#1. redo the tickets so they're arranged by category, not ticket
ticketcats = []
for i in range(len(tickets[0])):
	ticketcats.append([k[i] for k in tickets])
	
#2. now redo the ranges so it's a list of sets?
#uhhhhh
rulessep = []
for i in chunkedrules:
	start = set(range(i[0][0],i[0][1]+1))
	start.update(range(i[1][0],i[1][1]+1))
	rulessep.append(start)
#print rulessep

#3. init-ing some more important variables
numcats = len(ticketcats)
possibilities = []
for i in range(numcats):
	possibilities.append(range(numcats))

certanities = [-1]*numcats

#first try: process of elimination(compare)
for cat in range(numcats):
	for rule in range(numcats):
		for bo in ticketcats[cat]:
			if bo not in rulessep[rule]:
				possibilities[cat].remove(rule)

#print possibilities

#second: comb through iteratively
#take out anything that's certain
while True:
	#print possibilities
	donesomething = False
	for i in range(numcats):
		if len(possibilities[i])==1:
			donesomething = True
			#add to certainties,
			used = possibilities[i][0]
			certanities[i] = used
			#then iteratively take it out of possibilities
			for k in range(numcats):
				if used in possibilities[k]:
					possibilities[k].remove(used)

	if donesomething == False:
		break
		
print possibilities
print certanities
#now we know what everything is so...

topsix = []
for i in range(numcats):
	if certanities[i] < 6:
		topsix.append(i)
		
print topsix

ans = 1
for i in topsix:
	ans *= tickets[0][i]
	
print ans

