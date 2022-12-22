from math import gcd

with open('input/11.txt') as f:
    lines = f.readlines()
lines.append("\n")

def lcm(a,b):
   return (a * b) // gcd(a, b)

class Monkey:
	def __init__(self, items, opperation, test, true, false):
		self.items = items
		self.opperation = opperation
		self.test_value = test
		self.true = true
		self.false = false

	def test(self):
		if self.items[0]%self.test_value == 0:
			return self.true
		else:
			return self.false

	def opperate(self):
		if self.opperation[0] == '*':
			for i in range(len(self.items)):
				self.items[i] *= int(self.opperation[2:])
				self.items[i] //= 3

		if self.opperation[0] == '+':
			for i in range(len(self.items)):
				self.items[i] += int(self.opperation[2:])
				self.items[i] //= 3

		if self.opperation[0] == '^':
			for i in range(len(self.items)):
				self.items[i] = self.items[i]**2
				self.items[i] //= 3

	def opperate2(self):
		if self.opperation[0] == '*':
			for i in range(len(self.items)):
				self.items[i] *= int(self.opperation[2:])
				self.items[i] //= 3

		if self.opperation[0] == '+':
			for i in range(len(self.items)):
				self.items[i] += int(self.opperation[2:])

		if self.opperation[0] == '^':
			for i in range(len(self.items)):
				self.items[i] = self.items[i]**2



monkeys = []
monkey = False
items = []
opperation = ""
test = -1
true = -1
false = -1

for line in lines:
	# print(line)
	if line != "\n":
		# print(line[8])
		if line[8] == ':': #Init new monkey
			monkey = True

		if monkey:
			# print(line[8])
			if line[8] == 'n': # starting items
				x = line[18:-1]
				temp = x.split(", ")
				for i in temp:
					items.append(int(i))
			
			elif line[8] == 'i': # operation
				x = line[23:-1]
				if x[-3:] == "old":
					opperation = "^ 2"
				else:
					opperation = x

			elif line[8] == 'd': # test
				test = int(line[21:-1])

			elif line[8] == 'r': # true
				true = int(line[29:-1])

			elif line[8] == 'a': # false
				false = int(line[30:-1])

	else:
		monkeys.append(Monkey(items, opperation, test, true, false))
		monkey = False
		items = []
		opperation = ""
		test = -1
		true = -1
		false = -1		

# for i in monkeys:
# 	print(i.items)
# 	print(i.opperation)
# 	print(i.test)
# 	print(i.true)
# 	print(i.false)



def part1(lines):
	rounds = 20

	inspections = []
	for i in range(len(monkeys)):
		inspections.append(0)

	for i in range(rounds):
		for j in range(len(monkeys)):
			monkeys[j].opperate()
			while monkeys[j].items:
				inspections[j] += 1
				monkeys[monkeys[j].test()].items.append(monkeys[j].items[0])
				del monkeys[j].items[0]

	biggest = [0,0]
	for i in inspections:
		if i > biggest[0]:
			biggest[0] = i
			if biggest[0] > biggest[1]:
				temp = biggest[0]
				biggest[0] = biggest[1]
				biggest[1] = temp

	# print(biggest)

	print('Part 1:', biggest[0]*biggest[1])


def part2(lines):
	rounds = 10000

	inspections = []
	for i in range(len(monkeys)):
		inspections.append(0)

	for i in range(rounds):
		print (i)
		for j in range(len(monkeys)):
			monkeys[j].opperate2()
			while monkeys[j].items:
				inspections[j] += 1
				monkeys[monkeys[j].test()].items.append(monkeys[j].items[0])
				del monkeys[j].items[0]

	biggest = [0,0]
	for i in inspections:
		if i > biggest[0]:
			biggest[0] = i
			if biggest[0] > biggest[1]:
				temp = biggest[0]
				biggest[0] = biggest[1]
				biggest[1] = temp

	# print(biggest)

	print('Part 2:', biggest[0]*biggest[1])

part1(lines)
part2(lines)