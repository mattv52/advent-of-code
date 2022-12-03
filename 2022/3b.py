with open('input/3.txt') as f:
    lines = f.readlines()

print(lines)

def sort(string):

	temp = []
	for i in range(len(string)):
		temp.append(string[i])

	temp.sort()

	return ''.join(temp)

def compStr(s1, s2, s3):

	i=0
	j=0
	k=0
	while i != len(s1) or j != len(s2) or k != len(s3):
		print(s1[i], s2[j], s3[k])
		if lowChar(s1[i], s2[j], s3[k]) == -1:
			return s1[i]
		elif lowChar(s1[i], s2[j], s3[k]) == 0:
			i += 1
		elif lowChar(s1[i], s2[j], s3[k]) == 1:
			j += 1
		elif lowChar(s1[i], s2[j], s3[k]) == 2:
			k += 1

def lowChar(c1, c2, c3):
	i = ord(c1)
	j = ord(c2)
	k = ord(c3)

	if i == j and j == k:
		return -1
	elif i <= j and i <= k:
		return 0
	elif j <= i and j <= k:
		return 1
	elif k <= j and k <= i:
		return 2

def calcPriority(c):
	if ord(c) > 95: #lower
		return ord(c)-96
	else: #upper
		return ord(c)-38

# for line in lines:
# 	size = len(line)//2
# 	packs[0].append(line[:size])
# 	packs[1].append(line[size:-1])

total = 0

for i in range(0, len(lines), 3):
	lines[i] = sort(lines[i][:-1])
	lines[i+1] = sort(lines[i+1][:-1])
	lines[i+2] = sort(lines[i+2][:-1])

	total += calcPriority(compStr(lines[i], lines[i+1], lines[i+2]))
	# print(total)

print(total)