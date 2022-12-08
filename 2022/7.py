from anytree import Node, RenderTree

with open('input/7.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
	lines[i] = lines[i][:-1]

def generateTree(lines):

	del lines[0]
	root = Node("/", dir=True)
	current = root

	for line in lines:
		if line == "$ cd /":
			current = root
		elif line == "$ cd ..":	
			current = current.parent
		elif line[2:4] == "cd":	
			for child in current.children:
				if child.name == line[5:]:
					current = child
					break
		elif line == "$ ls":	
			pass
		elif line[:3] == "dir":
			Node(line[4:], dir=True, parent=current)
		else:
			sep = line.find(' ')
			Node(line[sep+1:], dir=False, size=int(line[:sep]), parent=current)

	# print(RenderTree(root))
	return root

def calcSize(root):
	total = 0
	for child in root.children:
		if child.dir == False:
			total += child.size
		else:
			total += calcSize(child)
	root.size = total
	return total

def findSize(root):
	total = 0

	for child in root.children:
		if child.dir == True:
			total += findSize(child)

	if root.size <= 100000:
		total += root.size
	return total

def closestDir(root, size):
	for child in root.children:
		if child.dir == True:
			closestDir(child, size)

	if root.size >= size:
		print(root.size)
	# return total


def part1(lines):
	root = generateTree(lines)
	calcSize(root)
	ans = findSize(root)

	print("Part 1: ", ans)


	
def part2(lines):
	root = generateTree(lines)
	root_size = calcSize(root)
	empty = 70000000-root_size
	need = 30000000-empty

	
	print("Part 2: (smallest)")
	closestDir(root, need)

part1(lines)
part2(lines)