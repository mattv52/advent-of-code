with open('input/17.txt') as f:
    lines = f.readlines()
for i in range(len(lines)):
	if lines[i][-1] == '\n':
		lines[i] = lines[i][:-1]

class Rock:
	def __init__(self, shape, base):
		bot = base + 2
		if shape == "-":
			self.left = (2, bot) 
			self.right = (5, bot)
			self.rocks = [[2, bot], [3, bot], [4, bot], [5, bot]]

		if shape == "+":
			self.left = (2, bot+1) 
			self.right = (4, bot+1)
			self.rocks = [[2, bot+1], [3, bot], [3, bot+1], [3, bot+2]]

		if shape == "L":
			self.left = (2, bot)
			self.right = (4, bot)
			self.rocks = [[2, bot], [3, bot], [4, bot], [4, bot+1]]

		if shape == "|":
			self.left = (2, bot)
			self.right = (2, bot)
			self.rocks = [[2, bot], [2, bot+1], [2, bot+2], [2, bot+3]]

		if shape == "o":
			self.left = (2, bot)
			self.right = (3, bot)
			self.rocks = [[2, bot], [2, bot+1], [3, bot], [3, bot+1]]

	def moveDown(base):
		temp = self.rocks
		for i in range(len(temp)):

			if base[part[0]] ==


	def moveLeft():

	def moveRight():



def part1(lines):
	rocks = 0
	base = [0, 0, 0, 0, 0, 0, 0]

	while rocks < 2022:
		rocksShape = ['-', '+', 'L', '|', 'o']
		rock = Rock(rocksShape[rocks%5], max(base))
		rocks += 1
		falling = True
		while falling:
			char = lines[0][i%len(lines[0])]
			if char == '<':
				rock.moveLeft()

			if char == '>':
				rock.moveRight()

			moved = rock.moveDown()

			if moved == -1:
				falling = False
				updateBase(base, rock)
			i += 1

	ans = max(base)
	print('Part 1:', ans)


def part2(lines):

	ans = ''
	print('Part 2:', ans)

part1(lines)
#part2(lines)
