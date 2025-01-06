import unittest

from textnode import TextNode,TextType
from leafnode import LeafNode
from nodeparser import Nodeparser

class TestNodeparser(unittest.TestCase):
    def test_text_node_to_html_node(self):
        print("Nodeparser Test: test_text_node_to_html_node")
        text_node = TextNode("Normal Text", TextType.TEXT)
        self.assertIsInstance(Nodeparser().text_node_to_html_node(text_node), LeafNode)

    def test_link_node_to_html_node(self):
        print("Nodeparser Test: test_link_node_to_html_node")
        text_node = TextNode("Link", TextType.LINK, "https://www.google.com")
        self.assertEqual(Nodeparser().text_node_to_html_node(text_node).to_html(), '<a href="https://www.google.com">Link</a>')

    def test_split_nodes_delimiter(self):
        print("Nodeparser Test: test_split_nodes_delimiter")
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = Nodeparser().split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_split_nodes_delimiter_error(self):
        print("Nodeparser Test: test_split_nodes_delimiter_error")
        node = TextNode("Wrong text to *bold", TextType.TEXT)
        with self.assertRaises(Exception):
            Nodeparser().split_nodes_delimiter([node], "*", TextType.BOLD)

    def test_markdown_parsers(self):
        print("Nodeparser Test: test_markdown_parsers")
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        tupels = Nodeparser().extract_markdown_images(text)
        self.assertEqual(tupels, [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])

        text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        tupels2 = Nodeparser().extract_markdown_links(text2)
        self.assertEqual(tupels2, [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def test_split_nodes_image(self):
        print("Nodeparser Test: test_split_nodes_image")
        node = TextNode(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
            TextType.TEXT,
        )
        new_nodes = Nodeparser().split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                TextNode(" and ", TextType.TEXT),
                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            new_nodes
        )

    def test_split_nodes_link(self):
        print("Nodeparser Test: test_split_nodes_link")
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = Nodeparser().split_nodes_link([node])
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ]
        )

    def test_split_nodes_image_edge(self):
        print("Nodeparser Test: test_split_nodes_image_edge")
        node = TextNode(
            "![edge case](https://i.imgur.com/aKaOqIh.gif)",
            TextType.TEXT,
        )
        new_nodes = Nodeparser().split_nodes_image([node])
        self.assertEqual(
            [
                TextNode("edge case", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            ],
            new_nodes
        )

    def test_text_to_textnodes(self):
        print("Nodeparser Test: test_text_to_textnodes")
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = Nodeparser().text_to_textnodes(text)
        self.assertEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ], nodes)


if __name__ == "__main__":
    unittest.main()