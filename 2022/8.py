with open('input/8.txt') as f:
    lines = f.readlines()
	
class Tree:
	def __init__(self, tree):
		self.tree = tree
		self.checked = False

	def __str__(self):
		return f"[{self.tree}, {self.checked}]"


newLine = []
for line in lines:
	temp = []
	for tree in line:
		if tree != '\n':
			temp.append(Tree(int(tree)))
	newLine.append(temp)

def part1(lines):
	left=0
	right=0
	up=0
	down=0

	for line in lines:
		left_tree=-1
		right_tree=-1
		for i in range(len(line)):
			if line[i].tree >left_tree:
				left_tree = line[i].tree
				if not line[i].checked:
					left += 1
					line[i].checked = True

			if line[len(line)-i-1].tree > right_tree:
				right_tree = line[len(line)-i-1].tree
				if not line[len(line)-i-1].checked:
					line[len(line)-i-1].checked = True
					right += 1

	for i in range(len(lines[0])):
		up_tree=-1
		down_tree=-1
		for j in range(len(lines)):
			if lines[j][i].tree >up_tree:
				up_tree = lines[j][i].tree
				if not lines[j][i].checked:
					up += 1
					lines[j][i].checked = True

			temp = lines[len(lines[0])-j-1][i]
			if temp.tree > down_tree:
				down_tree = temp.tree
				if not temp.checked:
					down += 1
					temp.checked = True


	# for x in newLine:
	# 	for y in x:
	# 		print(y, end="")
	# 	print('')

	ans = left + right + up + down
	print("Part 1: ", ans)


def part2(lines):
	
	ans = 0

	for i in range(len(lines)):
		for j in range(len(lines[i])):
			scores = [0, 0, 0, 0] #NESW
			tree = lines[i][j].tree

			for n in range(i-1, -1, -1):
				scores[0] += 1
				if lines[n][j].tree >= tree:
					break

			for e in range(j+1, len(lines[i])):
				scores[1] += 1
				if lines[i][e].tree >= tree:
					break
			
			for s in range(i+1, len(lines[i])):
				scores[2] += 1
				if lines[s][j].tree >= tree:
					break
			
			for w in range(j-1, -1, -1):
				scores[3] += 1
				if lines[i][w].tree >= tree:
					break

			tot = scores[0]*scores[1]*scores[2]*scores[3]
			if tot > ans:
				ans = tot

	print("Part 2: ", ans)

part1(newLine)
part2(newLine)