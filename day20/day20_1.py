<<<<<<< HEAD
from enum import Enum, auto

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

regex = contents[0]
#regex = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
#regex = '^N(E|S|)(W|N|)E$'

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

    while True:
        currentLiteral = parseChar(string[0])

        if currentLiteral in cardinal:
            currentNode = Node(currentLiteral)

            parentNode.children.append(currentNode)

            parentNode, string = currentNode, string[1:]

        elif currentLiteral is Literal.OPEN:
            currentNode = Node(Literal.OPEN)
            parentNode.children.append(currentNode)
            branchParents.append(currentNode)
            branchEnds.append([])
            depth += 1
            parentNode, string = currentNode, string[1:]

        elif currentLiteral is Literal.DELIM:
            branchEnds[depth - 1].append(parentNode)
            parentNode, string = branchParents[depth - 1], string[1:]

        elif currentLiteral is Literal.CLOSE:
            currentNode = Node(Literal.CLOSE)
            parentNode.children.append(currentNode)
            for end in branchEnds[depth - 1]:
                end.children.append(currentNode)
            branchEnds.pop(depth - 1)
            branchParents.pop(depth - 1)
            depth -= 1
            parentNode, string = currentNode, string[1:]

        elif currentLiteral is Literal.END:
            currentNode = Node(Literal.END)
            parentNode.children.append(currentNode)
            return currentNode

head = Node(Literal.START)
tail = parseString(head, regex[1:])

print('regex parsed')

rooms = {(0, 0): 0}

class TraversalAgent():
    def __init__(self, steps, starting_node, starting_room, manager):
        self.steps = steps 
        self.starting_node = starting_node
        self.current_node = starting_node
        self.starting_room = starting_room
        self.current_room = starting_room
        self.manager = manager

    def traverse(self):
        global rooms
        while True:
            if self.current_node.direction is Literal.END:
                return
            elif self.current_node.direction is Literal.OPEN:
                for child in self.current_node.children[1:]:
                    self.manager.agents.append(
                            TraversalAgent(
                                self.steps, child, self.current_room,
                                self.manager))
            elif self.current_node.direction in cardinal:
                direction = self.current_node.direction
                if direction is Literal.NORTH:
                    self.current_room = (self.current_room[0], self.current_room[1] + 1)
                elif direction is Literal.EAST:
                    self.current_room = (self.current_room[0] + 1, self.current_room[1])
                elif direction is Literal.SOUTH:
                    self.current_room = (self.current_room[0], self.current_room[1] - 1)
                elif direction is Literal.WEST:
                    self.current_room = (self.current_room[0] - 1, self.current_room[1])

                self.steps += 1

                if self.current_room in rooms:
                    if rooms[self.current_room] > self.steps:
                        rooms[self.current_room] = self.steps
                    else:
                        return
                else:
                    rooms[self.current_room] = self.steps
            
            self.current_node = self.current_node.children[0]

class AgentManager():
    def __init__(self):
        self.agents = []
        self.complete = []

    def traverse_agents(self):
        while len(self.agents[:]) > 0:
            agent = self.agents.pop(0)
            agent.traverse()
            self.complete.append(agent)

            print('{} agents left'.format(len(self.agents[:])))

am = AgentManager()
am.agents.append(TraversalAgent(0, head, (0, 0), am))
am.traverse_agents()

print(max(rooms.values()))

print(len([distance for distance in rooms.values() if distance >= 1000]))

