N = int(input())

binary_tree = [{"parent": -1, "sibling": -1} for _ in range(N)]
for _ in range(N):
    node_input = input()
    id, left, right = map(int, node_input.split())

    binary_tree[id]["left"] = left
    binary_tree[id]["right"] = right

    degree = 0
    if left != -1:
        degree += 1
        binary_tree[left]["parent"] = id
        binary_tree[left]["sibling"] = right
    if right != -1:
        degree += 1
        binary_tree[right]["parent"] = id
        binary_tree[right]["sibling"] = left
    binary_tree[id]["degree"] = degree


def measure_depth_and_height(id, depth):
    H[id] = max(H[id], depth)

    parent_id = binary_tree[id]["parent"]
    if parent_id == -1:
        return depth

    return measure_depth_and_height(parent_id, depth+1)

D = [0 for i in range(N)]
H = [0 for i in range(N)]
for id in range(N):
    depth = measure_depth_and_height(id, 0)
    D[id] = depth


def get_type(node):
    if node["parent"] == -1:
        return "root"
    if node["degree"] == 0:
        return "leaf"
    return "internal node"

for id in range(N):
    node = binary_tree[id]
    parent_id = node["parent"]
    sibling_id = node["sibling"]
    degree = node["degree"]
    node_type = get_type(node)
    print("node {}: parent = {}, sibling = {}, degree = {}, depth = {}, height = {}, {}".format(id, parent_id, sibling_id, degree, D[id], H[id], node_type))