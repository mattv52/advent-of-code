with open('input/1.txt') as f:
    lines = f.readlines()

lines[-1]+="\n"
# print(str(int(lines[-1])))
# print(lines)
largest = [0,0,0]
runningtot = 0

for cal in lines:
	if cal == '\n':
		if runningtot > largest[0]:
			largest[0] = runningtot
			largest.sort()
		runningtot = 0
	else:
		runningtot += int(cal)

print(largest)
print(largest[0]+largest[1]+largest[2])