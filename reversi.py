inp = """f4
f5
g6
END"""

xAxis = list(map(chr, range(97, 105)))
yAxis = range(1, 9)

whiteSpots = ["d4", "e5"]
blackSpots = ["d5", "e4"]

def getLeft(pos):
	letter, number = list(pos)
	letIdx = xAxis.index(letter)
	if letIdx > 1:
		return xAxis[letIdx - 1] + number

def getRight(pos):
	letter, number = list(pos)
	letIdx = xAxis.index(letter)
	if letIdx < len(xAxis) - 1:
		return xAxis[letIdx + 1] + number

def getUp(pos):
	letter, number = list(pos)
	if int(number) > 1:
		return letter + str(int(number) - 1)

def getDown(pos):
	letter, number = list(pos)
	if int(number) < 8:
		return letter + str(int(number) + 1)

def handleMove(newPos, isWhite):
	sameArr = whiteSpots if isWhite else blackSpots
	oppositeArr = blackSpots if isWhite else whiteSpots
	sameArr.append(newPos)

	# right
	right = getRight(newPos)
	if right in oppositeArr and getRight(right) in sameArr:
		oppositeArr.remove(right)
		sameArr.append(right)

	# left
	left = getLeft(newPos)
	if left in oppositeArr and getLeft(left) in sameArr:
		oppositeArr.remove(left)
		sameArr.append(left)

	# up
	up = getUp(newPos)
	if up in oppositeArr and getUp(up) in sameArr:
		oppositeArr.remove(up)
		sameArr.append(up)

	# down
	down = getDown(newPos)
	if down in oppositeArr and getDown(down) in sameArr:
		oppositeArr.remove(down)
		sameArr.append(down)

	# up-right
	ur = getUp(right)
	if ur in oppositeArr and getUp(getRight(ur)) in sameArr:
		oppositeArr.remove(ur)
		sameArr.remove(ur)

	# up-left
	ul = getUp(left)
	if ul in oppositeArr and getUp(getLeft(ul)) in sameArr:
		oppositeArr.remove(ul)
		sameArr.append(ul)

	# down-right
	dr = getDown(right)
	if dr in oppositeArr and getDown(getRight(dr)) in sameArr:
		oppositeArr.remove(dr)
		sameArr.append(dr)

	# down-left
	dl = getDown(left)
	if dl in oppositeArr and getDown(getLeft(dl)) in sameArr:
		oppositeArr.remove(dl)
		sameArr.append(dl)
	


def drawBoard():
	board = ""
	for y in yAxis:
		for x in xAxis:
			coord = x + str(y)
			if coord in whiteSpots:
				board += "W"
			elif coord in blackSpots:
				board += "B"
			else:
				board += "."
		board += "\n"
	return board

isWhite = True
for move in inp.split("\n")[:-1]:
	handleMove(move, isWhite)
	isWhite = not isWhite

print drawBoard()
