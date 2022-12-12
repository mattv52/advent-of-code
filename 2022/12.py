from collections import deque

with open('input/12.txt') as f:
    inputlines = f.readlines()

class Hill:
	def __init__(self, pos, size):
		self.pos = pos
		self.size = size
		


start = (-1, -1)
startlist = []
end = (-1, -1)

lines = []
for x in range(len(inputlines)):
	temp = []
	for y in range(len(inputlines[x])):
		hill = ord(inputlines[x][y])-97
		if hill != -87:
			if hill == -14:
				start = (x, y)
				startlist.append((x, y))
				temp.append(0)
			elif hill == 0:
				startlist.append((x, y))
				temp.append(0)
			elif hill == -28:
				end = (x, y)
				temp.append(25)
			else:
				temp.append(hill)

			# temp.append((int(tree)))
	lines.append(temp)

graph = {}
for x in range(len(lines)):
	for y in range(len(lines[x])):
		temp = []
		this = lines[x][y]
		if x-1 >= 0:
			if this-lines[x-1][y] >= -1:
				temp.append((x-1, y))
		if x+1 < len(lines):
			if this-lines[x+1][y] >= -1:
				temp.append((x+1, y))
		if y-1 >= 0:
			if this-lines[x][y-1] >= -1:
				temp.append((x, y-1))
		if y+1 < len(lines[x]):
			if this-lines[x][y+1] >= -1:
				temp.append((x, y+1))
		graph[(x, y)] = temp

def get_shortest_path(graph, start, end):
	dist = {start: [start]}
	q = deque()
	q.append(start)
	while len(q):
		at = q.popleft()
		for next in graph[at]:
			if next not in dist:
				dist[next] = [dist[at], next]
				q.append(next)
	
	temp = dist.get(end)
	x = 1
	if temp != None:
		while len(temp[0]) > 1:
			temp = temp[0]
			x += 1
		return x
	else:
		return -1


def part1(graph):
	dist = {start: [start]}
	q = deque()
	q.append(start)
	while len(q):
		at = q.popleft()
		for next in graph[at]:
			if next not in dist:
				dist[next] = [dist[at], next]
				q.append(next)
	
	temp = dist.get(end)
	x = 1
	while len(temp[0]) > 1:
		temp = temp[0]
		x += 1

	ans = x
	print('Part 1:', ans)


def part2(graph):
	shortest = 9999999
	for pos in startlist:
		x = get_shortest_path(graph, pos, end)
		if x != -1:
			if x < shortest:
				shortest = x


	print('Part 2:', shortest)

part1(graph)
part2(graph)
