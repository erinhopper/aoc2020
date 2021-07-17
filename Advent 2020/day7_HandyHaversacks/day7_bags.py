import sys

infilename = "bags.txt"

infile = open(infilename,'r')

bags = {}

#
#CREATES A DICT WITH KEY=OUTER, VALULE = LIST OF ALL INNERS
#
while True:
	line = infile.readline()
	if not line:
		break
	if line == "\n":
		break
	color1 = line[:line.index("bags")-1]
	contains = line[line.index("contain")+8:-2]
	if "no other bags" in contains:
		bags[color1] = []
	else:
		bags[color1] = []
		data = contains.split(', ')
		for i in data:
			num = int(i[:2])
			color2 = i[2:-4]
			if num>1:
				color2 = color2[:-1]
			bags[color1].append((num,color2))

#print bags

#
#CREATES A DICT WITH KEY = INNER, VALUE = LIST OF ALL OUTERS
#
# while True:
# 	line = infile.readline()
# 	if not line:
# 		break
# 	color1 = line[:line.index("bags")-1]
# 	contains = line[line.index("contain")+8:-2]
# 	if "no other bags" in contains:
# 		pass
# 	else:
#  		data = contains.split(', ')
#  		for i in data:
#  			num = int(i[:2])
#  			color2 = i[2:-4]
#  			if num>1:
#  				color2 = color2[:-1]
# 			if color2 in bags:
# 				bags[color2].append(color1)
# 			else:
# 				bags[color2] = [color1]
				
poss = []

def get_outers(color,bags,poss):
	#print "GETTING",color
	if color not in bags:
		#print "not in?"
 		return poss
	else:
		imms = bags[color]
		count = 0
		for i in imms:
			poss.append(i)
			poss = get_outers(i,bags,poss)
		return poss
		
#poss = get_outers("shiny gold",bags,poss)
#print "ANSWER 1:", len(set(poss))

done = {}
def get_inners(color,bags):
	if color not in bags:
		return 0
	if color in done:
		return done[color]
	directly = bags[color]
	total = 0#it at least has the new bags
	for i in directly:
		#i is a tuple: (num,incolor)
		num = i[0]
		incolor = i[1]
		total += num*(get_inners(incolor,bags))
		total += num#the number of bags of incolor
		#print num, incolor
	done[color] = total
	return total

print "ANSWER 2:",get_inners("shiny gold",bags)

