#!/usr/bin/python3

num_recipes = '513401'

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

head = Node(3)
head.insert(7)
tail = head.advance()
elf_1_node = head
elf_2_node = tail

last_7_scores = ['3', '7']
last_7_scores_str = '37'
score_len = 2

t = 0

found = False

# This still takes minutes but it does work
while num_recipes not in last_7_scores_str:
    elf_1_score = elf_1_node.value
    elf_2_score = elf_2_node.value

    # Add new recipes to the scoreboard
    score_sum = elf_1_score + elf_2_score
    sum_str = str(score_sum)
    for digit in sum_str:
        tail.insert(int(digit))
        tail = tail.advance()
        score_len += 1

        last_7_scores.append(digit)
        if len(last_7_scores) > 7:
            last_7_scores.pop(0)

    last_7_scores_str = ''.join(last_7_scores)

    # Pick new recipes
    for i in range(elf_1_score + 1):
        elf_1_node = elf_1_node.advance()
    for i in range(elf_2_score + 1):
        elf_2_node = elf_2_node.advance()
    t += 1

scores = []
index = head
for i in range(score_len):
    scores.append(index.value)
    index = index.advance()

scores_string = ''.join([str(x) for x in scores])
print(len(scores_string[0:scores_string.index(num_recipes)]))
