with open('input/15.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
	if lines[i][-1] == '\n':
		lines[i] = lines[i][:-1]

def part1(lines):
	checked = set()

	for line in lines:
		x = int(line[line.find("x=")+2:line.find(",")])
		y = int(line[line.find("y=")+2:line.find(":")])
		sensor = (x, y)

		x = int(line[line.find("x=", 40)+2:line.find(",", 40)])
		y = int(line[line.find("y=", 40)+2:])
		beacon = (x, y)
		print(beacon)

		radius = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])

		for i in range(1, radius+1):
			for j in range(1, i+1):
				temp = (sensor[0]-j, sensor[1]-(i-j))
				# if temp[0] ==

	ans = len(checked)

	print('Part 1:', ans)


def part2(lines):

	ans = ''
	print('Part 2:', ans)

part1(lines)
#part2(lines)
