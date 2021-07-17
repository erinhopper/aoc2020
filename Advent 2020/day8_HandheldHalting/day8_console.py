import sys

infilename = "console.txt"

infile = open(infilename,'r')

commands = []
while True:
	line = infile.readline()
	if not line:
		break
	
	if line[0] == 'a':
		com = 0
	elif line[0] == 'n':
		com = 1
	elif line[0] == 'j':
		com = 2
	else:
		print "broken"
		
	num = int(line[4:])
	
	commands.append((com,num))

def loopcheck(commands, lookingforloop=True, ret=False):	
	done = []
	on = 0
	acc = 0
	l = len(commands)
	while True:
		if on in done:
			if lookingforloop == True:
				print "Found loop: "+ str(acc)
			if ret == True:
				return done
			break
		if on == l:
			print "Finished without finding loop, ACC = " + str(acc)
			break
		current = commands[on]
		done.append(on)
		if current[0] == 0:#acc
			on += 1
			acc += current[1]
		elif current[0] == 1:#nop
			on += 1
		elif current[0] == 2:
			on += current[1]
			
d = loopcheck(commands,ret=True)
	
for i in d:
	if commands[i][0] != 0:
		#change line i and run the loop checker
		commands2 = commands[:]
		n = commands[i][1]
		if commands[i][0] == 2:
			commands2[i] = (1,n)
		else:
			commands2[i] = (2,n)
		loopcheck(commands2,lookingforloop=False)