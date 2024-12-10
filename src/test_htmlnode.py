import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_print_props(self):
        print("HTMLNode Test: print_props")
        html_node = HTMLNode("a", "Google Link", [], {
            "href": "https://www.google.com", 
            "target": "_blank",
        })
        self.assertEqual(html_node.props_to_html(), 'href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    unittest.main()