import sys

infilename = "expensereport.txt"

infile = open(infilename,'r')

nums = []

while True:
	line = infile.readline()
	if not line:
		break
	nums.append(int(line[:len(line)-1]))
	
infile.close()

l = len(nums)
for i in range(l):
	for k in range(l):
		for j in range(l):
			if nums[i]+nums[k]+nums[j]==2020:
				print nums[i],nums[k],nums[j],nums[k]*nums[i]*nums[j]