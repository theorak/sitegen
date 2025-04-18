import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("TextNode Test: test_eq")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        node2 = TextNode("This is a text node", TextType.ITALIC)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(node2, node3)

        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node4, node5)


    def test_not_eq(self):
        print("TextNode Test: test_not_eq")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        print("TextNode Test: test_url_none")
        node = TextNode("This is a text node", TextType.LINK)
        self.assertIsNone(node.url)

        node2 = TextNode("This is a text node", TextType.IMAGE)
        self.assertIsNone(node2.url)


if __name__ == "__main__":
    unittest.main()