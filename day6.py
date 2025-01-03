myinput = [
"....#.....",
".........#",
"..........",
"..#.......",
".......#..",
"..........",
".#..^.....",
"........#.",
"#.........",
"......#..."
]

# for i in myinput:
# 	for j in i:
# 		print('J:',j)
# 		print(len(j))
directions = {1:'up',2:'right',3:'down',4:'left'}

def findGuard(myinput):
	guardpos = []
	boxes = []
	for y in range(0,len(myinput)):
		# print(myinput[y])
		for x in range(0,len(myinput[y])):
			# print(myinput[y][x])
			if myinput[y][x] == '^':
				guardpos = [y,x]
				guarddir = 1
			elif myinput[y][x] == '#':
				boxes.append([y,x])
	return(guardpos, boxes, guarddir)

guardpos, boxes, guarddir = findGuard(myinput)

print(guardpos)
print(guarddir)
print(directions[guarddir])

if directions[guarddir] == 'up':
	temppos = [guardpos[0]-1, guardpos[1]]
	
	while temppos not in boxes:
		templist = [i for i in myinput]
		templist[guardpos[0]].replace('^','X')
		guardpos = temppos
		templist[guardpos[0]][guardpos[1]] = '>'
		myinput = [i for i in templist]
		print(myinput)
	guarddir += 1







