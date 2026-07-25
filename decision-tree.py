import math

# Calculate Entropy
def entropy(data):
    yes = 0
    no = 0

    for row in data:
        if row[-1] == "Yes":
            yes += 1
        else:
            no += 1

    total = yes + no

    if yes == 0 or no == 0:
        return 0

    p1 = yes / total
    p2 = no / total

    return -(p1 * math.log2(p1) + p2 * math.log2(p2))


# Calculate Information Gain
def information_gain(data, col):
    total_entropy = entropy(data)
    groups = {}

    for row in data:
        key = row[col]
        if key not in groups:
            groups[key] = []
        groups[key].append(row)

    sub_entropy = 0
    total = len(data)

    for key in groups:
        prob = len(groups[key]) / total
        sub_entropy += prob * entropy(groups[key])

    return total_entropy - sub_entropy


# Build Decision Tree
def build_tree(data, attributes):

    classes = [row[-1] for row in data]

    if classes.count(classes[0]) == len(classes):
        return classes[0]

    if len(attributes) == 0:
        return max(set(classes), key=classes.count)

    gains = []

    for col in attributes:
        gains.append(information_gain(data, col))

    best = attributes[gains.index(max(gains))]

    tree = {best: {}}

    values = set(row[best] for row in data)

    for value in values:
        subset = [row for row in data if row[best] == value]

        new_attr = attributes.copy()
        new_attr.remove(best)

        tree[best][value] = build_tree(subset, new_attr)

    return tree


# Print Tree
def print_tree(tree, names, level=0):

    if type(tree) != dict:
        print(":", tree)
        return

    for key in tree:
        for value in tree[key]:
            print("  " * level + names[key] + " =", value, end="")
            print_tree(tree[key][value], names, level + 1)


# ---------------- Example ----------------

data = [
["Young","High","Good","Yes"],
["Young","Low","Good","Yes"],
["Middle","High","Poor","No"],
["Old","Medium","Good","Yes"],
["Old","Low","Average","Yes"],
["Old","High","Poor","No"],
["Middle","Low","Average","Yes"],
["Young","Medium","Poor","No"],
["Young","Low","Average","Yes"],
["Middle","Medium","Good","Yes"],
["Old","Medium","Average","Yes"],
["Middle","High","Good","Yes"],
["Young","Medium","Average","Yes"],
["Old","High","Average","No"]
]

# Attribute Names
names = ["Age", "Income", "Credit"]

print("\nDecision Tree\n")

tree = build_tree(data, [0, 1, 2])
print_tree(tree, names)
