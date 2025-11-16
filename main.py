from BST.final_review import BST

def main():
    # Create and populate a BST
    tree = BST()
    tree.root = BST.Node(10)
    tree.root.left = BST.Node(5)
    tree.root.right = BST.Node(15)
    tree.root.left.left = BST.Node(3)
    tree.root.left.right = BST.Node(7)
    tree.root.right.left = BST.Node(12)
    tree.root.right.right = BST.Node(18)
    
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
    tree.print_between_recursive(6, 16)
    
    print("\nPrint values between 6 and 16 (iterative):")
    tree.print_between_iterative(6, 16)
    
    print("\n" + "=" * 40)

if __name__ == "__main__":
    main()
