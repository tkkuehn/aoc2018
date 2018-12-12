#!/usr/bin/python3


contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

initial_state_string = contents[0][15:]
min_state = 0
max_state = len(initial_state_string) - 1
state = set()
    
for i in range(max_state + 1):
    if initial_state_string[i] == '#':
        state.add(i)

state_transitions = {}
state_transitions_string = contents[2:]

for state_transition in state_transitions_string:
    state_transitions[state_transition[0:5]] = state_transition[9]

for i in range(20):
    # Need to include anything that will consider the current state
    new_state = set()
    for j in range(min_state - 2, max_state + 3):
        context = []
        for k in range(-2, 3):
            if j + k in state:
                context.append('#')
            else:
                context.append('.')
        if state_transitions[''.join(context)] == '#':
            new_state.add(j)
    min_state = min(new_state)
    max_state = max(new_state)
    state = new_state

print(sum(state))

