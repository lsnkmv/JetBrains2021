from JetBrains_2021 import Node, AVL_Tree

import unittest

class UserModelCase(unittest.TestCase):
    def test_AVL_Tree(self):
        test_Tree = AVL_Tree()
        root = None

        root = test_Tree.insert_to_AVL(root, 65)
        root = test_Tree.insert_to_AVL(root, 50)
        root = test_Tree.insert_to_AVL(root, 25)
        root = test_Tree.insert_to_AVL(root, 75)
        root = test_Tree.insert_to_AVL(root, 85)
        root = test_Tree.insert_to_AVL(root, 150)
        root = test_Tree.insert_to_AVL(root, 125)
        root = test_Tree.insert_to_AVL(root, 100)
        root = test_Tree.insert_to_AVL(root, 175)

        test_Tree.result_AVL_tree(root)

        the_base_order = [75, 50, 25, 65, 125, 85, 100, 150, 175]
        self.assertEqual(test_Tree.root_order, the_base_order)

if __name__ == '__main__':
    unittest.main()