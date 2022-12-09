from math import sqrt
with open('input/9.txt') as f:
    lines = f.readlines()


# -1 = dont move else
#  				701
#  				6 2
#  				543
def moveTail(head, tail):
	distx = (head[0]-tail[0])
	disty = (head[1]-tail[1])
	dist = sqrt(distx**2 + disty**2)

	if dist == 0 or dist == 1 or dist == sqrt(2):
		return -1

	if (distx > 1 and disty > 0) or (distx > 0 and disty > 1):
		return 1
	if (distx > 1 and disty < 0) or (distx > 0 and disty < -1):
		return 3
	if (distx < -1 and disty < 0) or (distx < 0 and disty < -1):
		return 5
	if (distx < -1 and disty > 0) or (distx < 0 and disty > 1):
		return 7
	
	if disty > 1:
		return 0
	if distx > 1:
		return 2
	if disty < -1:
		return 4
	if distx < -1:
		return 6		

def move(x, direction):
	if direction == -1:
		return x
	if direction == 0:
		temp = list(x)
		temp[1]+=1
		return tuple(temp)
	if direction == 1:
		temp = list(x)
		temp[0]+=1
		temp[1]+=1
		return tuple(temp)
	if direction == 2:
		temp = list(x)
		temp[0]+=1
		return tuple(temp)
	if direction == 3:
		temp = list(x)
		temp[0]+=1
		temp[1]-=1
		return tuple(temp)
	if direction == 4:
		temp = list(x)
		temp[1]-=1
		return tuple(temp)
	if direction == 5:
		temp = list(x)
		temp[0]-=1
		temp[1]-=1
		return tuple(temp)
	if direction == 6:
		temp = list(x)
		temp[0]-=1
		return tuple(temp)
	if direction == 7:
		temp = list(x)
		temp[1]+=1
		temp[0]-=1
		return tuple(temp)

def part1(lines):
	start = (0, 0)
	visited = set(())
	visited.add(start)
	head = start
	tail = start

	for line in lines:
		direction = line[0]
		moves = int(line[2:])

		if direction == 'U':
			for i in range(moves):
				head = move(head, 0)
				tailMove = moveTail(head, tail)
				if tailMove != -1:
					tail = move(tail, tailMove)
					visited.add(tail)
		if direction == 'D':
			for i in range(moves):
				head = move(head, 4)
				tailMove = moveTail(head, tail)
				if tailMove != -1:
					tail = move(tail, tailMove)
					visited.add(tail)
		if direction == 'L':
			for i in range(moves):
				head = move(head, 6)
				tailMove = moveTail(head, tail)
				if tailMove != -1:
					tail = move(tail, tailMove)
					visited.add(tail)
		if direction == 'R':
			for i in range(moves):
				head = move(head, 2)
				tailMove = moveTail(head, tail)
				if tailMove != -1:
					tail = move(tail, tailMove)
					visited.add(tail)

	print('Part 1:', len(visited))


def part2(lines):
	start = (0, 0)
	visited = set(())
	visited.add(start)
	rope = []
	ropeLength = 10
	for i in range(ropeLength):
		rope.append(start)

	for line in lines:
		direction = line[0]
		moves = int(line[2:])

		if direction == 'U':
			for i in range(moves):
				rope[0] = move(rope[0], 0)
				for i in range(1, ropeLength):
					tailMove = moveTail(rope[i-1], rope[i])
					if tailMove != -1:
						rope[i] = move(rope[i], tailMove)
						visited.add(rope[-1])
		if direction == 'D':
			for i in range(moves):
				rope[0] = move(rope[0], 4)
				for i in range(1, ropeLength):
					tailMove = moveTail(rope[i-1], rope[i])
					if tailMove != -1:
						rope[i] = move(rope[i], tailMove)
						visited.add(rope[-1])
		if direction == 'L':
			for i in range(moves):
				rope[0] = move(rope[0], 6)
				for i in range(1, ropeLength):
					tailMove = moveTail(rope[i-1], rope[i])
					if tailMove != -1:
						rope[i] = move(rope[i], tailMove)
						visited.add(rope[-1])
		if direction == 'R':
			for i in range(moves):
				rope[0] = move(rope[0], 2)
				for i in range(1, ropeLength):
					tailMove = moveTail(rope[i-1], rope[i])
					if tailMove != -1:
						rope[i] = move(rope[i], tailMove)
						visited.add(rope[-1])
		# print(visited)
	print('Part 2:', len(visited))

part1(lines)
part2(lines)