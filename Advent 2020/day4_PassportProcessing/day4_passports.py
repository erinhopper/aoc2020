import sys

infilename = "passports.txt"

infile = open(infilename,'r')

def isNumeric(s):
	for i in list(s):
		if i in '0123456789':
			return True
	return False

valids = 0
total = 1
byr=iyr=eyr=hgt=hcl=ecl=pid=False


while True:
	
	line = infile.readline()
	if not line:
		break
	if line == "\n":
		if ((byr and iyr) and (eyr and hgt)) and ((hcl and ecl) and pid):
			valids += 1
		total += 1
		byr=iyr=eyr=hgt=hcl=ecl=pid=False
	else:
		l = line[:-1].split(" ")
		for i in l:
			field = i[:3]
			data = i[4:]
			if field == "byr":
				if isNumeric(data) and int(data) > 1919 and int(data)<2003:
					byr = True

			elif field == "iyr":
				if isNumeric(data) and int(data) > 2009 and int(data)<2021:
					iyr = True
			elif field == "eyr":
				if isNumeric(data) and int(data) >=2020 and int(data)<=2030:
					eyr = True
			elif field == "hgt":
				if data[-2:]=="cm":	
					if isNumeric(data[:-2]) and int(data[:-2]) >=150 and int(data[1:-2]) <= 193:
						hgt = True
				elif data[-2:]=="in":
					if isNumeric(data[:-2]) and int(data[:-2]) >=59 and int(data[1:-2]) <= 76:
						hgt = True
			elif field == "hcl":
				if len(data) == 7 and data[0] == '#':
					count = 0
					for k in data[1:]:
						if k in list("abcdef0123456789"):
							count += 1
					if count == 6:		
						hcl = True
			elif field == "ecl":
				if data in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
					ecl = True
			elif field == "pid":
				if len(data)== 9 and isNumeric(data):
					pid = True
			

if ((byr and iyr) and (eyr and hgt)) and ((hcl and ecl) and pid):
	valids += 1


#print total
print valids
#print total-valids