from collections import deque

with open('input/5.txt') as f:
    lines1 = deque(f.readlines())

with open('input/5.txt') as f:
    lines2 = deque(f.readlines())


# move 3 from 8 to 2
def part1(lines):

	crates = []
	for i in range(9):
		crates.append(deque())

	line = lines.popleft()
	while line != "\n":
		if line[1] != ' ':
			crates[0].appendleft(line[1])
		if line[5] != ' ':
			crates[1].appendleft(line[5])
		if line[9] != ' ':
			crates[2].appendleft(line[9])
		if line[13] != ' ':
			crates[3].appendleft(line[13])
		if line[17] != ' ':
			crates[4].appendleft(line[17])
		if line[21] != ' ':
			crates[5].appendleft(line[21])
		if line[25] != ' ':
			crates[6].appendleft(line[25])
		if line[29] != ' ':
			crates[7].appendleft(line[29])
		if line[33] != ' ':
			crates[8].appendleft(line[33])

		line = lines.popleft()

	for crate in crates:
		crate.popleft()

	for line in lines:
		amount = int(line[5:line.find(' ', 5)])
		a = int(line[line.find(' ', 10)+1])-1
		b = int(line[line.find(' ', 15)+1])-1

		for i in range(amount):
			crates[b].append(crates[a].pop())

	ans = ''
	for crate in crates:
		ans += (crate.pop())
	print("Part 1: ", ans)


	
def part2(lines):
	crates = []
	for i in range(9):
		crates.append(deque())

	line = lines.popleft()
	while line != "\n":
		if line[1] != ' ':
			crates[0].appendleft(line[1])
		if line[5] != ' ':
			crates[1].appendleft(line[5])
		if line[9] != ' ':
			crates[2].appendleft(line[9])
		if line[13] != ' ':
			crates[3].appendleft(line[13])
		if line[17] != ' ':
			crates[4].appendleft(line[17])
		if line[21] != ' ':
			crates[5].appendleft(line[21])
		if line[25] != ' ':
			crates[6].appendleft(line[25])
		if line[29] != ' ':
			crates[7].appendleft(line[29])
		if line[33] != ' ':
			crates[8].appendleft(line[33])

		line = lines.popleft()

	for crate in crates:
		crate.popleft()

	for line in lines:
		amount = int(line[5:line.find(' ', 5)])
		a = int(line[line.find(' ', 10)+1])-1
		b = int(line[line.find(' ', 15)+1])-1

		temp = deque()
		for i in range(amount):
			temp.append(crates[a].pop())

		for i in range(amount):
			crates[b].append(temp.pop())
		

	ans = ''
	for crate in crates:
		ans += (crate.pop())
	print("Part 2: ", ans)

part1(lines1)
part2(lines2)