with open('input/14.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
	lines[i] = lines[i][:-1]

def getline(str):
	line = str.split(' -> ')
	lineout = set()

	prev = (int(line[0][:line[0].find(',')]), int(line[0][line[0].find(',')+1:]))
	# print(prev)
	for point in line:
		p = (int(point[:point.find(',')]), int(point[point.find(',')+1:]))
		# print(p, prev)
		if p[0] == prev[0]:
			if p[1] < prev[1]:
				for i in range(p[1], prev[1]+1):
					# print("p<prev, y", i)
					lineout.add((p[0],i))
			else:
				for i in range(prev[1], p[1]+1):
					# print("prev<p, y", i)
					lineout.add((p[0],i))
		else:
			if p[0] < prev[0]:
				for i in range(p[0], prev[0]+1):
					# print("p<prev, x", i)
					lineout.add((i,p[1]))
			else:
				for i in range(prev[0], p[0]+1):
					# print("prev<p, x", i)
					lineout.add((i,p[1]))
		prev = p
	return lineout


def buildTerrain(lines):
	terrain = set()
	linedraw = []

	for line in lines:
		linedraw = getline(line)
		for point in linedraw:
			terrain.add(point)

	return terrain

def simuate1(terrain):
	total = 0
	void = False
	moving = True
	lowest = 0
	for i in terrain:
		if i[1] > lowest:
			lowest = i[1]

	lowest += 1

	while not void:
		moving = True
		sand = [500, 0]
		total += 1
		while moving:
			if sand[1] >= lowest:
				void = True
				moving = False
			if (sand[0], sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
			elif (sand[0]-1, sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
				sand[0] = sand[0]-1
			elif (sand[0]+1, sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
				sand[0] = sand[0]+1
			else:
				moving = False
		terrain.add((sand[0], sand[1]))

	return total

def simuate2(terrain):
	total = 0
	finished = False
	moving = True
	lowest = 0
	for i in terrain:
		if i[1] > lowest:
			lowest = i[1]

	lowest += 2

	while not finished:
		moving = True
		sand = [500, 0]
		total += 1
		while moving:
			if sand[1]+1 == lowest:
				moving = False
			elif (sand[0], sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
			elif (sand[0]-1, sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
				sand[0] = sand[0]-1
			elif (sand[0]+1, sand[1]+1) not in terrain:
				sand[1] = sand[1]+1
				sand[0] = sand[0]+1
			else:
				moving = False
		if sand == [500, 0]:
			finished = True
		terrain.add((sand[0], sand[1]))

	return total


def part1(lines):
	terrain = buildTerrain(lines)
	ans = simuate1(terrain)-1

	print('Part 1:', ans)


def part2(lines):
	terrain = buildTerrain(lines)
	ans = simuate2(terrain)

	print('Part 2:', ans)

part1(lines)
part2(lines)
