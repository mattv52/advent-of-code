with open('input/10.txt') as f:
    lines = f.readlines()

def check_cycle(cycle):
	if cycle%40 == 20 and cycle < 230:
		return 1
	else:
		return 0

def incCursor(cursor):
	cursor[1] += 1
	if cursor[1] == 40:
		cursor[0] += 1
		cursor[1] = 0

	return cursor

def part1(lines):
	x = 1
	cycle = 1
	signal = 0

	for instr in lines:
		if instr[0] == 'n':
			cycle += 1
			signal += x*cycle*check_cycle(cycle)
		elif instr[0] == 'a':
			cycle += 1
			signal += x*cycle*check_cycle(cycle)
			cycle += 1
			x += int(instr[5:])
			signal += x*cycle*check_cycle(cycle)
		# print("x:", x, "cycle:", cycle, "signal", signal)

	print('Part 1:', signal)


def part2(lines):
	x = 1
	cursor = [0, 0]


	screen = [[],[],[],[],[],[]]

	for instr in lines:
		if instr[0] == 'n':
			if abs(x-cursor[1]) == 1 or abs(x-cursor[1]) == 0:
				screen[cursor[0]].append('#')
			else:
				screen[cursor[0]].append('.')
			cursor = incCursor(cursor)

		elif instr[0] == 'a':
			if abs(x-cursor[1]) == 1 or abs(x-cursor[1]) == 0:
				screen[cursor[0]].append('#')
			else:
				screen[cursor[0]].append('.')
			cursor = incCursor(cursor)

			if abs(x-cursor[1]) == 1 or abs(x-cursor[1]) == 0:
				screen[cursor[0]].append('#')
			else:
				screen[cursor[0]].append('.')
			x += int(instr[5:])
			cursor = incCursor(cursor)

		# print("x:", x, "cursor", cursor)
	
	print('Part 2: VV')
	for i in screen:
		for j in i:
			print(j, end="")
		print("")

part1(lines)
part2(lines)
