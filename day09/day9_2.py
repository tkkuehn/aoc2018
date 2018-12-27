#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()[0].split(' ')

    num_players = int(contents[0])
    num_marbles = (int(contents[6]) + 1) * 100

    class Node:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            if next:
                self.next = next
            else:
                self.next = self
            
            if prev:
                self.prev = prev
            else:
                self.prev = self

        def advance(self):
            return self.next

        def retreat(self):
            return self.prev

        def insert(self, value):
            self.next = Node(value, self.next, self)
            self.next.next.prev = self.next
            if self.prev.value == self.value:
                self.prev = self.next

        def remove(self):
            self.prev.next = self.next
            self.next.prev = self.prev
            return self.next

    circle = Node(0)
    scores = [0] * num_players

    player_index = 0
    current_marble = 0
    for marble in range(num_marbles):
        if marble == 0:
            pass
        elif marble % 23 == 0:
            scores[player_index] += marble
            for i in range(7):
                circle = circle.retreat()
            scores[player_index] += circle.value
            circle = circle.remove()
        else:
            circle = circle.advance()
            circle.insert(marble)
            circle = circle.advance()
        player_index += 1
        player_index %= num_players

    print(max(scores))

