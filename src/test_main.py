import unittest

from main import *

class TestTextNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        print("Main Test: test_text_node_to_html_node")
        text_node = TextNode("Normal Text", TextType.TEXT)
        self.assertIsInstance(text_node_to_html_node(text_node), LeafNode)

    def test_leaf_node_html(self):
        print("Main Test: test_leaf_node_html")
        text_node = TextNode("Link", TextType.LINK, "https://www.google.com")
        self.assertEqual(text_node_to_html_node(text_node).to_html(), '<a href="https://www.google.com">Link</a>')

if __name__ == "__main__":
    unittest.main()