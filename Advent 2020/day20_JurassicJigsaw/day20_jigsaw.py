import sys
import copy
import math

infilename = "jigsaw.txt"

class PuzzlePiece(object):

	@staticmethod
	def makeBin(listofbits):
		total = 0
		for i in range(len(listofbits)):
			bit = listofbits[::-1][i]
			total = total | (bit<<i)
			#print i, bit, bin(total)
		return total
	
	def __init__(self, i, p):
		self.status = None
		self.index = i
		self.pairs = {}
		
		self.pixels = []
		for i in p:
			self.pixels.append([])
			for k in i:
				if k == "#":
					self.pixels[-1].append(1)
				else:
					self.pixels[-1].append(0)
		
		self.top = self.pixels[0]
		self.right = [i[-1] for i in self.pixels]
		self.bottom = (self.pixels[-1])
		self.left = [i[0] for i in self.pixels]

		self.rotations = [PuzzlePiece.makeBin(self.top),PuzzlePiece.makeBin(self.right),PuzzlePiece.makeBin(self.bottom[::-1]),PuzzlePiece.makeBin(self.left[::-1])]
		self.brotations = [PuzzlePiece.makeBin(self.top[::-1]),PuzzlePiece.makeBin(self.left),PuzzlePiece.makeBin(self.bottom),PuzzlePiece.makeBin(self.right[::-1])]
		#print self.rotations+self.brotations
	
	def getIndex(self):
		return self.index
	
	def getPixels(self):
		return self.pixels
	
	def prettyPrintTile(self):
		print "Tile",self.index
		for i in self.pixels:
			print i
	
	def getPossibles(self):
		return self.rotations + self.brotations
	
	def setStatus(self,stat):
		self.status = stat
	
	def getPairs(self):
		return self.pairs
	
	def setPair(self,otherPiece, sideNum):
		self.pairs[sideNum]=otherPiece
	
	def checkRots(self):
		for i in self.rotations:
			print bin(i)
		print ""
		for i in self.brotations:
			print bin(i)
	
	def rotateEdges(self,r=0,flipped=False):
		if flipped==False:
			base = self.rotations
		else:
			base = self.brotations
		first = base[r]
		second = base[(1+r)%4]
		third = base[(2+r)%4]
		fourth = base[(3+r)%4]
		return [first,second,third,fourth]
		
	def rotatePixels(self,r=0,flipped=False):
		new = []
		if flipped==True:
			for i in self.pixels:
				new.append(i[::-1])
		else:
			for i in self.pixels:
				new.append(i[:])
		if r == 3:
			r = 1 
		elif r == 1:
			r = 3
			
		original = new
		for i in range(r):
			rotated = [list(i) for i in zip(*original[::-1])]
			original = rotated
			
		return original
		
	@staticmethod
	def rotate2D(array, r=0,flipped=False):
		new = []
		if flipped==True:
			for i in array:
				new.append(i[::-1])
		else:
			for i in array:
				new.append(i[:])
		if r == 3:
			r = 1 
		elif r == 1:
			r = 3
			
		original = new
		for i in range(r):
			rotated = [list(i) for i in zip(*original[::-1])]
			original = rotated
			
		return original

def flipBits(num,length=10):
	newnum = 0
	for i in range(0,length):
		if num&1==True:
			newnum += 1
		num = num >> 1
		newnum = newnum << 1
	newnum = newnum>>1
	return newnum

infile = open(infilename,'r')

puzzlepieces = []
pixels = []
numofpieces = 1

line = infile.readline()
indnum = int(line[5:9])


while True:
	line = infile.readline()
	if not line:
		break
	if line == '\n':
		puzzlepieces.append(PuzzlePiece(indnum,pixels))
		numofpieces += 1
		line = infile.readline()
		indnum = int(line[5:9])
		pixels = []
		#print indnum
	else:
		pixels.append(line[:-1])

puzzlepieces.append(PuzzlePiece(indnum,pixels))
	
def printpieces(puzzlepieces):
	print ""
	for i in puzzlepieces:
		i.prettyPrintTile()
		print ""


#printpieces(puzzlepieces)

#print numofpieces

#print puzzlepieces

possibles = []
for i in puzzlepieces:
	possibles.append(i.getPossibles())
	
#find pairs
#we're quadruple counting here
pairs = []

pairsper = [0]*numofpieces

pairseach = []
for i in range(numofpieces):
	pairseach.append([])

for i in range(len(possibles)):
	for k in range(i):
		first = possibles[i]
		second = possibles[k]
		same = 0
		for one in first:
			if one in second:
				pairs.append([i,k,one])
				same += 1
				pairsper[i]+=1
				pairsper[k]+=1
				pairseach[i].append((k,one))
				pairseach[k].append((i,one))
				puzzlepieces[i].setPair(puzzlepieces[k],one)
				puzzlepieces[k].setPair(puzzlepieces[i],one)
		#print same
			
cornernums = []
corners = []
edges = []
middles = []
for i in range(numofpieces):
	if pairsper[i]==8:
		middles.append(puzzlepieces[i])
		#MIDDLE
		puzzlepieces[i].setStatus("Middle")
	elif pairsper[i] == 6:
		edges.append(puzzlepieces[i])
		puzzlepieces[i].setStatus("Edge")
		#EDGE
	elif pairsper[i] == 4:
		puzzlepieces[i].setStatus("Edge")
		corners.append(puzzlepieces[i])
		cornernums.append(puzzlepieces[i].getIndex())
		#CORNER
	else:
		print "fuck"
		
#print cornernums
#total = 1
#for i in cornernums:
#	total *= i
#print total

#print pairs
#print pairseach
#print ""
#now we actually have to put it together
sidelength = int(math.sqrt(numofpieces))
puzzle = []
for i in range(sidelength):
	puzzle.append([0]*sidelength)
	
#FIRST CORNER
#lets figure out which two edges are connected to other things
first = corners[0]
firstrotations = first.rotations
firstconnects = first.getPairs()
#print firstrotations, firstconnects
firstedgesused = firstconnects.keys()

#print firstedgesused
connectsup = []
for i in firstrotations:
	if i in firstedgesused:
		connectsup.append(i)

#print connectsup
#and now lets figure out which orientation lets then 
for i in range(4):
	if set(first.rotateEdges(r=i)[1:3]) == set(connectsup):
		#print i
		puzzle[0][0] = (first,i,False)
		#print first.rotatePixels(r=i)
		break

#BEAUTIFUL
#print puzzle

for i in range(1,sidelength):
	last = puzzle[0][i-1]
	#print last
	right = (last[0].rotateEdges(r=last[1],flipped=last[2]))[1]
	lastpairs = last[0].getPairs()
	
	#print right, lastpairs
	
	newpiece = lastpairs[right]
	left = flipBits(right)
	#possibleorientations = []
	newpairs = newpiece.getPairs()
	#print left, newpairs
	for k in range(4):
		if newpiece.rotateEdges(r=k)[3] == left:
			#possibleorientations.append([k,True])
			if newpiece.rotateEdges(r=k)[2] in newpairs:
				puzzle[0][i] = (newpiece,k,False)
				break
		if newpiece.rotateEdges(r=k,flipped = True)[3] == left:
			#possibleorientations.append([k,False])
			if newpiece.rotateEdges(r=k,flipped = True)[2] in newpairs:
				puzzle[0][i] = (newpiece,k,True)
				break

#for i in puzzle[0]:
#	print i[0].getIndex()

#YEAHHHHHH WE GOT DA FIRST ROW

#now for the first column (VERY similar:)
for i in range(1,sidelength):
	last = puzzle[i-1][0]
	#print last
	bottom = (last[0].rotateEdges(r=last[1],flipped=last[2]))[2]
	lastpairs = last[0].getPairs()
	
	#print bottom, lastpairs
	
	newpiece = lastpairs[bottom]
	top = flipBits(bottom)
	#possibleorientations = []
	newpairs = newpiece.getPairs()
	#print top, newpairs
	for k in range(4):
		if newpiece.rotateEdges(r=k)[0] == top:
			#possibleorientations.append([k,True])
			if newpiece.rotateEdges(r=k)[1] in newpairs:
				#checking that the right is open
				puzzle[i][0] = (newpiece,k,False)
				break
		if newpiece.rotateEdges(r=k,flipped = True)[0] == top:
			#possibleorientations.append([k,False])
			if newpiece.rotateEdges(r=k,flipped = True)[1] in newpairs:
				#checking that the right is open
				puzzle[i][0] = (newpiece,k,True)
				break

#YEAH DAT FIRST COLUMN

#and everything else:
for i in range(1,sidelength):
	for j in range(1,sidelength):
		#print i,j
		#finding puzzle[i][j]
		above = puzzle[i-1][j]
		abovebottom = (above[0].rotateEdges(r=above[1],flipped=above[2]))[2]
		abovepairs = above[0].getPairs()
		
		totheleft = puzzle[i][j-1]
		ttleftright = (totheleft[0].rotateEdges(r=totheleft[1],flipped=totheleft[2]))[1]
		leftpairs = totheleft[0].getPairs()
		
		newpiece = leftpairs[ttleftright]
		if newpiece.getIndex() != abovepairs[abovebottom].getIndex():
			print "broken"
			break
		
		top = flipBits(abovebottom)
		left = flipBits(ttleftright)
		
		#ok now orientation
		for k in range(4):
			if newpiece.rotateEdges(r=k)[0] == top:
				#possibleorientations.append([k,True])
				if newpiece.rotateEdges(r=k)[3] == left:
					#checking that the left is good
					puzzle[i][j] = (newpiece,k,False)
					break
			if newpiece.rotateEdges(r=k,flipped = True)[0] == top:
				#possibleorientations.append([k,False])
				if newpiece.rotateEdges(r=k,flipped = True)[3] == left:
					#checking that the right is open
					puzzle[i][j] = (newpiece,k,True)
					break

#for i in puzzle:
#	for j in i:
#		print j[0].getIndex()

def printfull(pixelpuzzle,sidel):
	for i in pixelpuzzle:
		print ""
		#print i
		for j in range(10):
			print i[0][j],i[1][j],i[2][j]#,i[3][j],i[4][j],i[5][j],i[6][j],i[7][j],i[8][j],i[9][j],i[10][j],i[11][j]


pixelpuzzle = []
for i in puzzle:
	pixelpuzzle.append([])
	for k in i:
		pixelpuzzle[-1].append(k[0].rotatePixels(r=k[1],flipped=k[2]))

#printfull(pixelpuzzle,sidelength)

#ok! time to pare off the unimportant parts
#everything not in the top row needs the top pared off
for i in range(0,sidelength):
	for j in range(0,sidelength):
		#skip the top row
		(pixelpuzzle[i][j]).pop(0)

#everything not in the bottom row needs the bottom pared off
for i in range(0,sidelength):
	for j in range(0,sidelength):
		#skip the bottom row
		(pixelpuzzle[i][j]).pop(-1)
#everything not in the left row needs the left pared off
for i in range(0,sidelength):
	for j in range(0,sidelength):
		#skip the left column
		for k in range(0,len(pixelpuzzle[i][j])):
			(pixelpuzzle[i][j][k]).pop(0)
#everything not in the right row needs the right pared off
for i in range(0,sidelength):
	for j in range(0,sidelength):
		#skip the left column
		for k in range(0,len(pixelpuzzle[i][j])):
			(pixelpuzzle[i][j][k]).pop(-1)

#now lets uh. make everything into strings ig?
for a in range(len(pixelpuzzle)):# a tile row
	for b in range(len(pixelpuzzle[a])): #a tile
		for c in range(len(pixelpuzzle[a][b])): #a pixel row
			for d in range(len(pixelpuzzle[a][b][c])):# a pixel
				pixelpuzzle[a][b][c][d] = str(pixelpuzzle[a][b][c][d])
				
#and attempt to concatenate it into a real thing
image = [[]]#for the first row
for i in range(sidelength*9):
	image.append([])
image.append([])#for the last row
	
for i in range(sidelength):
	image[0].append("".join(pixelpuzzle[0][i][0]))
	pixelpuzzle[0][i].pop(0)
#print image[0]

for a in range(len(pixelpuzzle)):# a tile row
	for b in range(len(pixelpuzzle[a])): #a tile
		for c in range(len(pixelpuzzle[a][b])): #a pixel row
			image[a*9+1+c].append("".join(pixelpuzzle[a][b][c]))

while [] in image:
	image.remove([])
	
#print image

for i in range(len(image)):
	image[i] = "".join(image[i])
	
for i in image:
	print i
#print 'height:',len(image)
#print 'width:',len(image[1])

#wonderful!

def isASeaMonster(startrow,startcol,im):
	vectors = [(1,0),(2,1),(2,4),(1,5),(1,6),(2,7),(2,10),(1,11),(1,12),(2,13),(2,16),(1,17),(1,18),(1,19),(0,18)]
	for i in vectors:
		if im[startrow+i[0]][startcol+i[1]]!='1':
			return False
	#hey it's a monster!!!
	#time to replace all the 
	return True

lineimage = "".join(image)
roughwater = lineimage.count('1')

print roughwater

for i in range(4):
	print ''
	print "trying i =",i
	
	cimage = PuzzlePiece.rotate2D(image,r=i,flipped=True)
	
	for row in range(0,len(cimage)-2):
		for col in range(0,len(cimage[1])-19):
			if isASeaMonster(row,col,cimage):
				roughwater -= 15
				print 'got one!'
				print row,col

print roughwater