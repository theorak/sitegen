import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_init_parentnode(self):
        print("ParentNode Test: test_init_htmlnode")
        parent_node = ParentNode("p",
            [
                LeafNode("b", "Bold text")
            ]
        )
        self.assertIsInstance(parent_node, ParentNode)

        
    def test_init_no_children(self):
        print("ParentNode Test: test_init_no_children")        
        with self.assertRaises(ValueError):
            parent_node = ParentNode("p",
                []
            )
            parent_node = ParentNode("p",None)

    def test_to_html(self):
        print("ParentNode Test: test_to_html")
        parent_node = ParentNode("p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text")
            ]
        )
        self.assertEqual(parent_node.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_nested(self):        
        print("ParentNode Test: test_to_html_nested")
        parent_node = ParentNode("p",
            [
                LeafNode("h2", "Nested List coming up"),
                ParentNode("ol", [
                    LeafNode("li", "List Item 1"),
                    LeafNode("li", "List Item 2"),
                    LeafNode("li", "List Item 3")
                ])
            ]
        )
        self.assertEqual(parent_node.to_html(), '<p><h2>Nested List coming up</h2><ol><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li></ol></p>')



if __name__ == "__main__":
    unittest.main()