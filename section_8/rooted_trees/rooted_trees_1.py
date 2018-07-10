N = int(input())
A = [input() for i in range(N)]

def get_depth(node_dict):
    depth = 0
    parent = node_dict["parent"]
    while parent > -1:
        depth += 1
        parent = rooted_tree[parent]["parent"]
    return depth

def get_node_type(node_dict):
    if node_dict["parent"] == -1:
        return "root"
    if node_dict["left"] == -1:
        return "leaf"
    return "internal node"

def get_children(node_dict):
    left = node_dict["left"]
    if left == -1:
        return "[]"
    siblings = []
    siblings.append(str(left))
    while rooted_tree[left]["right"] > -1:
        right = rooted_tree[left]["right"]
        siblings.append(str(right))
        left = right
    return "[{}]".format(", ".join(siblings))

rooted_tree = [{"parent": -1, "left": -1, "right": -1} for i in range(N)]
for row in A:
    node, degree_and_children = row.split(" ", 1)
    node = int(node)
    degree = int(degree_and_children[0])
    if degree > 0:
        children_list = list(map(int, degree_and_children[1:].split()))
        rooted_tree[node]["left"] = children_list[0]
        for i in range(len(children_list)):
            child_node = children_list[i]
            right = -1
            if i < len(children_list)-1:
                right = children_list[i+1]
            rooted_tree[child_node]["right"] = right
            rooted_tree[child_node]["parent"] = node

for node in range(len(rooted_tree)):
    node_dict = rooted_tree[node]
    depth = get_depth(node_dict)
    node_type = get_node_type(node_dict)
    children = get_children(node_dict)
    print("node {}: parent = {}, depth = {}, {}, {}".format(node, node_dict["parent"], depth, node_type, children))