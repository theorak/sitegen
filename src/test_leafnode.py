import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_init_leafnode(self):
        print("LeafNode Test: test_init_leafnode")
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertIsInstance(leaf_node, LeafNode)

    def test_init_no_value(self):
        print("LeafNode Test: test_init_no_value")
        with self.assertRaises(ValueError):
            leaf_node = LeafNode("p")


    def test_to_html(self):
        print("LeafNode Test: test_to_html")
        leaf_node = LeafNode("p", "This is a paragraph of text.")          
        leaf_node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})        
        self.assertEqual(leaf_node.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(leaf_node2.to_html(),'<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()