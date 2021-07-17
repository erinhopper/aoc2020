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
	
	def checkRots(self):
		for i in self.rotations:
			print bin(i)
		print ""
		for i in self.brotations:
			print bin(i)
	
	def rotateEdges(self,r=0,flipped=False):
		#NOT TESTED
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

		
		

test = ["#..#.##..","#.......#","........#","#........","........#","........#","........#","#.......#",".##..##.#"]
piece = PuzzlePiece(3,test)
piece.prettyPrintTile()
piece.checkRots()
print [bin(i) for i in piece.rotateEdges(r=1,flipped=True)]

rot = piece.rotatePixels(r=1,flipped=True)
for i in rot:
	print i