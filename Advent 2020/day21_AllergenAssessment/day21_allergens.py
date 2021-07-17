import sys
import copy


infilename = "allergens.txt"


infile = open(infilename,'r')


foods = []
while True:
	line = infile.readline()
	if not line:
		break
	foods.append([])
	#first, take out the ingredients
	splitter = line.index('(')
	foods[-1].append(line[:splitter-1].split(" "))
	#now, the allergens
	foods[-1].append(line[splitter+10:-2].split(", "))

def recursivelength(l):
	#finds the total number of elements in a array, no matter how many dimensions
	total = 0
	for i in l:
		if type(i)==str:
			total += 1
		else:
			try:
				a = len(i)
				total += recursivelength(i)
			except TypeError:
				total += 1
	return total

#make it easier to handle by assigning every food a number value
dictoffoods = {}
currentnum = 0
for i in range(len(foods)):
	for k in range(len(foods[i][0])):
		if foods[i][0][k] not in dictoffoods.keys():
			dictoffoods[foods[i][0][k]] = currentnum
			foods[i][0][k] = currentnum
			currentnum += 1
		else:
			foods[i][0][k] = dictoffoods[foods[i][0][k]]
			
#print foods

			
allallergens = []

for i in foods:
	allallergens = allallergens + i[1]

allallergens = list(set(allallergens))

numofallergens = len(allallergens)

coulds = {}
for i in allallergens:
	#check if it's in more than one food
	foodsin = []
	for k in range(len(foods)):
		if i in foods[k][1]:
			foodsin.append(k)
	#print foodsin
	if len(foodsin)>1:
		#print "in",i
		couldbe = set(foods[foodsin[0]][0])
		for k in foodsin[1:]:
			#print k
			#print couldbe, set(foods[k][0])
			couldbe = couldbe.intersection(set(foods[k][0]))
			#print couldbe
	else:
		couldbe = set(foods[foodsin[0]][0])

	#if len(couldbe) == 1:
		#print i, "must be", list(couldbe)[0]
		
	coulds[i] = list(couldbe)
	#print i,foodsin
	
totalingredients = [i[0] for i in foods]

totalingredients = []
for i in foods:
	totalingredients += i[0]

totalallergens = []
for i in coulds.values():
	totalallergens += i

#print coulds
print totalingredients
totalallergens = list(set(totalallergens))
print "t",totalallergens
#print recursivelength(totalingredients)
#print recursivelength(totalallergens)
#print recursivelength(totalingredients) - recursivelength(totalallergens)

impossibles = totalingredients
for eachpos in totalallergens:
	while eachpos in impossibles:
		impossibles.remove(eachpos)
		
#print impossibles
print len(impossibles)

print len(totalallergens),len(allallergens)

foodsbackward = {v: k for k, v in dictoffoods.iteritems()}
#print foodsbackward
print ""

print coulds	

print sorted(coulds.keys())

#sore by hand and get:
done = [30,61,19,47,76,53,23,97]

names = [foodsbackward[i] for i in done]

print ",".join(names)