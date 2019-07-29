from enum import Enum, auto

contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

regex = contents[0]
#regex = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'

class Literal(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    START = auto()
    END = auto()
    OPEN = auto()
    CLOSE = auto()
    DELIM = auto()

def parseChar(char):
    if char == 'N':
        return Literal.NORTH
    if char == 'E':
        return Literal.EAST
    if char == 'S':
        return Literal.SOUTH
    if char == 'W':
        return Literal.WEST
    if char == '^':
        return Literal.START
    if char == '$':
        return Literal.END
    if char == '(':
        return Literal.OPEN
    if char == ')':
        return Literal.CLOSE
    if char == '|':
        return Literal.DELIM

class Node():
    def __init__(self, direction):
        self.direction = direction
        self.children = []

cardinal = [Literal.NORTH, Literal.EAST, Literal.SOUTH, Literal.WEST]

depth = 0
branchParents = []
branchEnds = []

def parseString(parentNode, string):
    global depth
    global branchParents
    global branchEnds

    currentLiteral = parseChar(string[0])

    if currentLiteral in cardinal:
        currentNode = Node(currentLiteral)

        parentNode.children.append(currentNode)

        return parseString(currentNode, string[1:])

    elif currentLiteral is Literal.OPEN:
        currentNode = Node(Literal.OPEN)
        parentNode.children.append(currentNode)
        branchParents.append(currentNode)
        branchEnds.append([])
        depth += 1
        return parseString(currentNode, string[1:])

    elif currentLiteral is Literal.DELIM:
        branchEnds[depth - 1].append(parentNode)
        return parseString(branchParents[depth - 1], string[1:])

    elif currentLiteral is Literal.CLOSE:
        currentNode = Node(Literal.CLOSE)
        parentNode.children.append(currentNode)
        for end in branchEnds[depth - 1]:
            end.children.append(currentNode)
        branchEnds.pop(depth - 1)
        branchParents.pop(depth - 1)
        depth -= 1
        return parseString(currentNode, string[1:])

    elif currentLiteral is Literal.END:
        currentNode = Node(Literal.END)
        parentNode.children.append(currentNode)
        return currentNode

head = Node(Literal.START)
tail = parseString(head, regex[1:])

rooms = {(0, 0): 0}
branches = []
branchEnds = []

def traverseGraph(currentRoom, steps, node):
    global depth
    global branchParents
    global branchEnds
    global rooms

    if node.direction is Literal.END:
        return
    if node.direction is Literal.OPEN:
        for child in node.children:
            closeNode, closeRoom = traverseGraph(currentRoom, steps, child)

        return traverseGraph(closeRoom, rooms[closeRoom], closeNode.children[0])
    if node.direction is Literal.CLOSE:
        return (node, currentRoom)

    nextRoom = currentRoom
    if node.direction is Literal.NORTH:
        nextRoom = (currentRoom[0], currentRoom[1] + 1)
        steps += 1
    elif node.direction is Literal.EAST:
        nextRoom = (currentRoom[0] + 1, currentRoom[1])
        steps += 1
    elif node.direction is Literal.WEST:
        nextRoom = (currentRoom[0] - 1, currentRoom[1])
        steps += 1
    elif node.direction is Literal.SOUTH:
        nextRoom = (currentRoom[0], currentRoom[1] - 1)
        steps += 1

    if nextRoom in rooms:
        if steps < rooms[nextRoom]:
            rooms[nextRoom] = steps
    else:
        rooms[nextRoom] = steps

    return traverseGraph(nextRoom, steps, node.children[0])

traverseGraph((0, 0), 0, head)
print(rooms)
