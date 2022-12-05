with open('input/4.txt') as f:
    lines = f.readlines()


def part1(lines):
	total = 0;

	for line in lines:

		a = line[:line.find(',')]
		b = line[line.find(',')+1:]

		min1 = int(a[:a.find('-')])
		max1 = int(a[a.find('-')+1:])
		min2 = int(b[:b.find('-')])
		max2 = int(b[b.find('-')+1:])

		if (min1 == min2):
			total += 1
		elif(min1 < min2):
			if max1 >= max2:
				total += 1
		elif(min1 > min2):
			if max1 <= max2:
				total += 1
	print("Part 1: ", total)
	
def part2(lines):
	total = 0;

	for line in lines:

		a = line[:line.find(',')]
		b = line[line.find(',')+1:]

		min1 = int(a[:a.find('-')])
		max1 = int(a[a.find('-')+1:])
		min2 = int(b[:b.find('-')])
		max2 = int(b[b.find('-')+1:])

		if not(max1<min2 or max2<min1):
			total += 1
	
	print("Part 2: ", total)

part1(lines)
part2(lines)