with open('input/13.txt') as f:
    lines = f.readlines()

def parse_packet(packet):
	# print(packet)
	temp = []
	i = 0
	while i < len(packet):
		# print(packet[i], i)
		if packet[i] == ']':
			i += 1
			return temp, i
		elif packet[i] == '[':
			pack, inc = parse_packet(packet[i+1:])
			# print('return', pack, inc)
			temp.append(pack)
			i += inc+1
		elif packet[i] != ',':
			# print(packet[i:])
			# print(packet.find(',', i), packet.find(']', i))
			if packet.find(',', i) < packet.find(']', i) and packet.find(',', i) != -1:
				temp.append(int(packet[i:packet.find(',', i)]))
			else:
				temp.append(int(packet[i:packet.find(']', i)]))
			i += 1
		else:
			i += 1
		# print(temp)
	# return temp, i

def compare(a, b):
	int_type = type(0)
	if type(a) == type(b) and type(a) == int_type:
		if a < b:
			return True
		else:
			return False

	elif type(a) == type(b):
		for i in range(len(a)):e
		return compare(a[0], b[0])


packets = []
a = None
b = None
packet1 = True

for line in lines:
	if line != "\n":
		line = line[1:-1]
		# print(line)
		if packet1:
			a = parse_packet(line)
			packet1 = False
		else:
			b = parse_packet(line)
			packet1 = True

	else:
		packets.append((a[0], b[0]))
		# print(packets)

for i in packets:
	print(i)

def part1(lines):
	total = 0

	for i in range(len(packets)):
		a = packets[i][0]
		b = packets[i][1]

		if compare(a, b):
			total += i


	print('Part 1:', total)


def part2(lines):

	print('Part 2:', ans)

#part1(lines)
#part2(lines)
