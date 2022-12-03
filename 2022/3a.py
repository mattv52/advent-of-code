with open('input/3.txt') as f:
    lines = f.readlines()

def sort(string):

	temp = []
	for i in range(len(string)):
		temp.append(string[i])

	temp.sort()

	return ''.join(temp)

def compStr(s1, s2):

	i=0
	j=0
	while i != len(s1) or j != len(s2):
		if compChar(s1[i], s2[j]) == 2:
			return s1[i]
		elif compChar(s1[i], s2[j]) == 1:
			i += 1
		elif compChar(s1[i], s2[j]) == 0:
			j += 1

# 0 is c1 larger, 1 is c2 larger, 2 is match
def compChar(c1, c2):
	if ord(c1) == ord(c2):
		return 2
	elif ord(c1) < ord(c2):
		return 1
	elif ord(c1) > ord(c2):
		return 0
	return -1

def calcPriority(c):
	if ord(c) > 95: #lower
		return ord(c)-96
	else: #upper
		return ord(c)-38

packs = [[],[]]

for line in lines:
	size = len(line)//2
	packs[0].append(line[:size])
	packs[1].append(line[size:-1])

total = 0

for i in range(len(packs[0])):
	packs[0][i] = sort(packs[0][i])
	packs[1][i] = sort(packs[1][i])

	total += calcPriority(compStr(packs[0][i], packs[1][i]))
	# print(total)

print(total)