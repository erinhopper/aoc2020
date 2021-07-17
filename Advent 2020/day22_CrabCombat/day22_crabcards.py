import sys
import timeit

startt = timeit.default_timer()

infilename = "crabcards.txt"


infile = open(infilename,'r')
line = infile.readline()


foods = []
player = 1
p1 = []
p2 = []
while True:
	line = infile.readline()
	if not line:
		break
	if line == "\n":
		player += 1
		line = infile.readline()
	elif player == 1:
		p1.append(int(line))
	elif player == 2:
		p2.append(int(line))


#print p1, p2

cardsper = len(p2)

def game(p1,p2,gamenum,retcards=False):
	rn = 1 
	gn = 2
	seenbefore = []
	while True:
		#start of a round!
		#print "game",gamenum,"round", rn
		#print "player 1's deck", p1
		#print "player 2's deck", p2
		
		#infinite loop checker
		roundsummary = (tuple(p1),tuple(p2))
		if roundsummary in seenbefore:
			#print "LOOP CHECK: this round has happened before!"
			#print "player 1 wins by default."
			if retcards==True:
				return p1
			else:
				return "p1"
		seenbefore.append(roundsummary)
		
		p1card = p1.pop(0)
		p2card = p2.pop(0)
		
		#print "player 1 plays", p1card
		#print "player 2 plays", p2card
		

		#if both players have at least as many cards as their value
		if len(p1)>=p1card and len(p2)>= p2card:
			#play a subgame
			winner = game(p1[:p1card],p2[:p2card],gn)
			#print "back to game",gamenum
			if winner == "p1":
				p1.append(p1card)
				p1.append(p2card)
				#print "player 1 wins!"
			else:
				p2.append(p2card)
				p2.append(p1card)
				#print "player 2 wins!"
		#else:
		else:
			if p1card>p2card:
				p1.append(p1card)
				p1.append(p2card)
				#print "player 1 wins!"
			else:
				p2.append(p2card)
				p2.append(p1card)
				#print "player 2 wins!"
			
		#print ""
		
		if len(p1)==0: 
			if retcards==False:
				return "p2"
			else:
				return p2
		if len(p2)==0: 
			if retcards==False:
				return "p1"
			else:
				return p1
		rn += 1




def knapsack(l):
	counter = 1
	score = 0
	for i in l[::-1]:
		score+=i*counter
		counter += 1
	return score
	
winlist = game(p1,p2,1,retcards=True)
print "winning hand:", winlist
print "score = ", knapsack(winlist)

stop = timeit.default_timer()

t = stop-startt
print 'total time: ', t

if t>15:
	print "too slow!!"
if