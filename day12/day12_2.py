#!/usr/bin/python3


contents = []
with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

state_transitions = {}
state_transitions_string = contents[2:]

for state_transition in state_transitions_string:
    state_transitions[state_transition[0:5]] = state_transition[9]

print(state_transitions)

initial_state_string = contents[0][15:]
state = set()
left_index = 0
state_length = len(initial_state_string)
state_cache = {}
    
for i in range(state_length):
    if initial_state_string[i] == '#':
        state.add(i)

state = frozenset(state)

cycle_index = 0

for i in range(50000000000):
    # Need to include anything that will consider the current state
    new_state = set()
    if state in state_cache:
        new_state = state_cache[state]['next']
        left_index += state_cache[state]['min']
        state_length = state_cache[state]['length']
        state_cache[state]['rep_count'] += 1

        if state_cache[state]['rep_count'] == 2:
            print('cycle detected')
            state_cache[state]['cycle_index'] = cycle_index
            cycle_index += 1

        if state_cache[state]['rep_count'] == 3:
            # I think this just repeats infinitely now?
            base_sum = sum(new_state)
            iterations_left = 50000000000 - i

            print(sum(new_state) + (len(state) * ((left_index + (state_cache[state]['min'] * (50000000000 - (i + 1)))))))
            break
    else:
        for j in range(-2, state_length + 2):
            context = []
            for k in range(-2, 3):
                if j + k in state:
                    context.append('#')
                else:
                    context.append('.')
            if state_transitions[''.join(context)] == '#':
                new_state.add(j)

        current_min = min(new_state)
        left_index += current_min
        state_length = max(new_state) - current_min + 1
        new_state = frozenset([x - current_min for x in new_state])

        state_cache[state] = {}
        state_cache[state]['min'] = current_min
        state_cache[state]['next'] = new_state
        state_cache[state]['length'] = state_length
        state_cache[state]['rep_count'] = 0

    state = new_state

print(sum(state) + (len(state) * left_index))

