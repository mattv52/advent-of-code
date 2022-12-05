with open('input/2.txt') as f:
    lines = f.readlines()

def calcPoints1(game):
	score = 0

	opp = game[0]
	you = game[2]
	
	if (opp == 'A' and you == 'Y') or (opp == 'B' and you == 'Z') or (opp == 'C' and you == 'X'): 
		score = 6
	elif (opp == 'A' and you == 'X') or (opp == 'B' and you == 'Y') or (opp == 'C' and you == 'Z'): 
		score = 3
	else:
		score = 0

	score+= ord(you)-87

	return score

def calcPoints2(game):

	you = game[2]
	opp = game[0]

	if (opp == 'A' and you == 'X') or (opp == 'B' and you == 'Z') or (opp == 'C' and you == 'Y'): 
		score = 3
	elif (opp == 'A' and you == 'Z') or (opp == 'B' and you == 'Y') or (opp == 'C' and you == 'X'): 
		score = 2
	else:
		score = 1

	if you == 'Z': 
		score += 6
	elif you == 'Y': 
		score += 3

	return score

def part1(lines):
	total = 0

	for game in lines:
		total += calcPoints1(game)

	print("Part 1: ", total)

def part2(lines):
	total = 0

	for game in lines:
		total += calcPoints2(game)

	print("Part 2: ", total)

part1(lines)
part2(lines)