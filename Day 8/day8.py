# DATA = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
# parsed_data = [int(x) for x in DATA.split()]

parsed_data = [int(x) for x in open("input.txt").read().split()]

class Node:
    def __init__(self, num_childs, num_meta, children, meta):
        self.num_childs = num_childs
        self.num_meta = num_meta
        self.children = children
        self.meta = meta


def get_nodes(inputs, start=0):
    num_children = inputs[start]
    num_metadata = inputs[start+1]
    start += 2
    children = []
    
    for _ in range(num_children):
        child, start = get_nodes(inputs, start)
        children.append(child)    
    
    metadata = inputs[start:start+num_metadata]

    return Node(num_children, num_metadata, children, metadata),(start + num_metadata)

root_node, useless = get_nodes(parsed_data)

def sum_metadata(node):
    return sum(node.meta) + sum(sum_metadata(child) for child in node.children)

meta_data_sum = sum_metadata(root_node)
print(meta_data_sum)

def value(node):

    if node.num_childs == 0:
        return sum(node.meta)
    else:
        child_values = {i: value(child) for i, child in enumerate(node.children)}
        return sum(child_values.get(i - 1, 0) for i in node.meta)

print(value(root_node))

