class Node:
    def __init__(self, value, left=None, right=None):
        # add your Node class code
        self.value = value
        self.left = left
        self.right = right
  

# list = [1, 4, 7]
def oneToSeven():
    # manually create the BST
    # then return the root node
    # pass
    node_1 = Node(1)
    node_7 = Node(7)
    node_4 = Node(4, node_1, node_7)
    return node_4

# list = [10, 40, 45, 46, 50]
def tenToFifty():
    # pass
    node_10 = Node(10)
    node_40 = Node(40, node_10)
    node_50 = Node(50)
    node_46 = Node(46, None, node_50)
    node_45 = Node(45, node_40, node_46)
    return node_45



# list = [-20, -19, -17, -15, 0, 1, 2, 10]
def negativeToPositive():
    # pass
    node_neg_20 = Node(-20)
    node_neg_17 = Node(-17)
    node_neg_19 = Node(-19, node_neg_20, node_neg_17)
    node_0 = Node(0)
    node_10 = Node(10)
    node_1 = Node(1, node_0)
    node_2 = Node(2, node_1, node_10)
    node_neg_15 = Node(-15, node_neg_19, node_2)
    return node_neg_15
# // YOU COULD ALSO DO THIS (THERE ARE MORE WAYS STILL!)
# // BUT WE GENERALLY DON'T WANT TO MAKE TREES LIKE THIS, YOU'LL FIND OUT WHY LATER
# //   10
# //     40
# //       45
# //         46
# //           50
# // function tenToFifty() {
# //   const fifty = new Node(50);
# //   const fortySix = new Node(46, null, fifty);
# //   const fortyFive = new Node(45, null, fortySix);
# //   const forty = new Node(40, null, fortyFive);

# //   return new Node(10, null, forty);
# // }

# // list = [-20, -19, -17, -15, 0, 1, 2, 10]
# //          -15
# //    -19         2
# //  -20  -17    0    10
# //                1


# if (require.main === module) {
#   # add your own tests in here if you want
# }

# module.exports = {
#   Node,
#   oneToSeven,
#   tenToFifty,
#   negativeToPositive
# };

# Please add your pseudocode to this file
# And a written explanation of your solution
