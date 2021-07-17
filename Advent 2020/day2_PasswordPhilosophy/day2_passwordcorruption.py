import sys

def isvalid(n1,n2,ch,password):
	#print n1,n2,ch,password
	#print password[n1-1],password[n2-1]
	if (password[n1-1]==ch) is not (password[n2-1]==ch):#exactly one must be true
		return True
	return False

infilename = "passworddata.txt"

infile = open(infilename,'r')

valid = 0

while True:
	line = infile.readline()
	if not line:
		break
	num1 = int(line[:line.index('-')])
	num2 = int(line[line.index('-')+1:line.index(' ')])
	char = line[line.index(' ')+1:line.index(':')]
	pas = line[line.index(':')+2:-1]
	if isvalid(num1,num2,char,pas) == True:
		valid += 1
	
	
infile.close()

print valid