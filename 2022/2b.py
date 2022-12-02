with open('input/2.txt') as f:
    lines = f.readlines()

def calcPoints(game):

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

total = 0;

for game in lines:
	total += calcPoints(game)

print(total)