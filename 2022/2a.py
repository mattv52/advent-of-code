with open('input/2.txt') as f:
    lines = f.readlines()

def calcPoints(game):
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

total = 0;

for game in lines:
	total += calcPoints(game)

print(total)