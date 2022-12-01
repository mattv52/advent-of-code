with open('input/1.txt') as f:
    lines = f.readlines()

lines[-1]+="\n"
# print(str(int(lines[-1])))
# print(lines)
largest = 0
runningtot = 0

for cal in lines:
	if cal == '\n':
		largest = runningtot if (runningtot > largest) else largest
		runningtot = 0
	else:
		runningtot += int(cal)

print(largest)