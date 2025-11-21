from BST.final_review import BST, BT

def main():
    # Create and populate a BST
    bst_tree = BST()
    bst_tree.root = BST.Node(10)
    bst_tree.root.left = BST.Node(5)
    bst_tree.root.right = BST.Node(15)
    bst_tree.root.left.left = BST.Node(3)
    bst_tree.root.left.right = BST.Node(7)
    bst_tree.root.right.left = BST.Node(12)
    bst_tree.root.right.right = BST.Node(18)
    
    print("Binary Search Tree Demo")
    print("=" * 40)
    print("\nTree structure:")
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     / \\   / \\")
    print("    3   7 12  18")
    print("\n" + "=" * 40)
    
    print("\nPrint values between 6 and 16 (recursive):")
    bst_tree.print_between_recursive(6, 16)
    
    print("\nPrint values between 6 and 16 (iterative):")
    bst_tree.print_between_iterative(6, 16)
    
    print("\n" + "=" * 40)

    bt_tree = BT()
    bt_tree.root = BT.Node(10)
    bt_tree.root.left = BT.Node(5)
    bt_tree.root.right = BT.Node(15)
    bt_tree.root.left.left = BT.Node(3)
    bt_tree.root.right.left = BT.Node(12)
    bt_tree.root.right.right = BT.Node(18)
    bt_tree.root.right.right.right = BT.Node(2)
    bt_tree.root.right.right.right.left = BT.Node(7)

    print("Binary Tree Demo")
    print("=" * 40)
    print("\nTree structure:")
    print("        10")
    print("       /  \\")
    print("      5    15")
    print("     /      / \\")
    print("    3     12  18")
    print("                \\")
    print("                  2")
    print("                 /")
    print("                7")
    print("\n" + "=" * 40)

    print(bt_tree.height())

if __name__ == "__main__":
    main()
