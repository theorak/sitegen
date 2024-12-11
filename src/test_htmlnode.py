import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_init_htmlnode(self):
        print("HTMLNode Test: test_init_htmlnode")        
        html_node = HTMLNode("b","Bold Text")
        self.assertIsInstance(html_node, HTMLNode)

    def test_props_to_html(self):
        print("HTMLNode Test: test_props_to_html")
        html_node = HTMLNode("a", "Google Link", [], {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(html_node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()