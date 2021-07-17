import sys
import copy

infilename = "operation.txt"

infile = open(infilename,'r')

lines = []

while True:
	line = infile.readline()
	if not line:
		break
	lines.append(line[:-1].replace(" ",""))

#rint lines

def sum(l):
	total = 0
	for i in l:
		total += i
	return total
	
	
def solveequation1(eq):
	#jflkajdljkakldkf
	#print eq
	on = 0
	current = 0
	op = True #True to add, False to multiply
	while on < len(eq):
		if eq[on] == '(':
			currentind = on+1
			openpcount = 1
			closepcount = 0
			while openpcount != closepcount:
				if eq[currentind] == '(':
					openpcount += 1
				elif eq[currentind] == ')':
					closepcount += 1
				currentind += 1
			num = solveequation1(eq[on+1:currentind-1])
					
			if op == True:
				current += num
			else:	
				current *= num
				
			on = currentind-1	
			#deal with recursion here:
			#find the end parentheses and recurse
			#also increment current and on by the right amount
		elif eq[on] == '+':
			op = True
		elif eq[on] == '*':
			op = False
		else:#is a number
			num = int(eq[on])
			if op == True:
				current += num
			else:	
				current *= num
		on += 1
	return current
	
def solveequation2(eq):
	#jflkajdljkakldkf
	#print eq

	op = True #True to add, False to multiply
	#print eq
	while '(' in eq:
		#find the first paren
		open = eq.index('(')
		#find matching outer paren

		close = open+1
		openpcount = 1
		closepcount = 0
		while openpcount != closepcount:
			if eq[close] == '(':
				openpcount += 1
			elif eq[close] == ')':
				closepcount += 1
			close += 1
			
		#solve recursively
		eval = solveequation2(eq[open+1:close-1])
		#replace the parens in eq with the number it evals to
		eq[open] = eval
		del eq[open+1:close]
	
	#print eq
	while '+' in eq:
		#find the first +
		plus = eq.index('+')
		#print eq,plus
		#print eq[plus-1]
		#print eq[plus+1]
		#add the two numbers around it
		sum = int(eq[plus-1])+int(eq[plus+1])
		#replace in eq
		eq[plus-1] = sum
		del eq[plus:plus+2]
		
	while '*' in eq:
		#find the first *
		times = eq.index('*')
		#multiply the two numbers around it
		product = int(eq[times-1])*int(eq[times+1])
		#replace in eq
		eq[times-1] = product
		del eq[times:times+2]
	
	return int(eq[0])
	
answers = []


for i in lines:
	answers.append(solveequation2(list(i)))
#print answers
print sum(answers)



	