class BinaryTree():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

def get_height(root):
    if root == None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def check_bst_balanced(root):
    if root == None:
        return True
    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return check_bst_balanced(root.left) and check_bst_balanced(root.right)

def main():
    tree1 = BinaryTree(1, BinaryTree(1, None, None), BinaryTree(1, None, None))
    tree2 = BinaryTree(1, BinaryTree(1, BinaryTree(1, BinaryTree(1, None, None), None), None), BinaryTree(1, None, None))

    print check_bst_balanced(tree1)
    print check_bst_balanced(tree2)

if __name__ == '__main__':
    main()