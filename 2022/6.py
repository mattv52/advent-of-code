with open('input/6.txt') as f:
    lines = f.readlines()

def allUnique(arr):
	if (any(arr.count(x) > 1 for x in arr)):
		return False
	else:
		return True


def part1(lines):
	line = lines[0]
	i = 0
	recent = [line[0], line[1], line[2], line[3]]

	for c in line:
		recent[i%4] = c
		i += 1

		if allUnique(recent):
			ans = str(i)
			break

	print("Part 1: ", ans)


	
def part2(lines):
	line = lines[0]
	print(line)
	recent = []
	for i in range(14):
		recent.append(line[i])
	
	i = 0
	for c in line:
		print(c, i)
		print(recent)
		recent[i%14] = c
		print(recent)
		i += 1

		if allUnique(recent):
			ans = str(i)
			break

	print("Part 2: ", ans)

part1(lines)
part2(lines)