#!/usr/bin/python3

with open('./resources/input.txt', 'r') as f:
    contents = f.read().splitlines()

    numbers = [int(x) for x in contents[0].split(' ')]

    class Tree:
        def __init__(self, num_children, num_metadata):
            self.num_children = num_children
            self.num_metadata = num_metadata
            self.children = []
            self.metadata = []

    def fill_tree(substring):
        tree = Tree(substring[0], substring[1])
        if tree.num_children == 0:
            tree.metadata = substring[2: 2 + tree.num_metadata]
            return (tree, substring[2 + tree.num_metadata:])
        else:
            new_substring = substring[2:]
            for i in range(tree.num_children):
                filled_tree = fill_tree(new_substring)
                tree.children.append(filled_tree[0])
                new_substring = filled_tree[1] 
            tree.metadata = new_substring[0:tree.num_metadata]
            new_substring = new_substring[tree.num_metadata:]
            return (tree, new_substring)

    root = fill_tree(numbers)[0]

    def node_value(node):
        if node.num_children == 0:
            return sum(node.metadata)
        else:
            children_value = 0
            for child in node.metadata:
                if (child - 1) >= 0 and (child - 1) < node.num_children:
                    children_value += node_value(node.children[child - 1])
            return children_value

    print(node_value(root))
