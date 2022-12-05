with open('input/1.txt') as f:
    lines = f.readlines()

lines[-1]+="\n"
# print(str(int(lines[-1])))
# print(lines)
def part1(lines):
	largest = 0
	runningtot = 0

	for cal in lines:
		if cal == '\n':
			largest = runningtot if (runningtot > largest) else largest
			runningtot = 0
		else:
			runningtot += int(cal)

	print("Part 1: ", largest)

def part2(lines):
	largest = [0,0,0]
	runningtot = 0

	for cal in lines:
		if cal == '\n':
			if runningtot > largest[0]:
				largest[0] = runningtot
				largest.sort()
			runningtot = 0
		else:
			runningtot += int(cal)

	print("Part 2: ", largest[0]+largest[1]+largest[2])

part1(lines)
part2(lines)