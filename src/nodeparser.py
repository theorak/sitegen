from textnode import TextNode, TextType
from leafnode import LeafNode
import re

class Nodeparser():   
    def __init__(self):
        pass

    # Conversion of text nodes to html (leaf) nodes
    def text_node_to_html_node(self, text_node: TextNode):
        match text_node.text_type:
            case TextType.TEXT:
                html_node = LeafNode(None, text_node.text)
            case TextType.BOLD:
                html_node = LeafNode("b", text_node.text)
            case TextType.ITALIC:
                html_node = LeafNode("i", text_node.text)
            case TextType.CODE:
                html_node = LeafNode("code", text_node.text)
            case TextType.LINK:
                html_node = LeafNode("a", text_node.text, {
                    "href": text_node.url
                })
            case TextType.IMAGE:
                html_node = LeafNode("img", None, {
                    "src": text_node.url,
                    "alt": text_node.text
                })
            case _:
                raise Exception("Unkown TextType for TextNode")
        return html_node

    # Splits nodes by delimiter into new nodes of the desired type
    def split_nodes_delimiter(self, old_nodes: list, delimiter: str, text_type: TextType):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT: # passthrough non-text nodes
                new_nodes.extend([node])
            else:
                parts = node.text.split(delimiter)
                if len(parts) == 3:
                    new_nodes.extend([
                        TextNode(parts[0], TextType.TEXT),
                        TextNode(parts[1], text_type),
                        TextNode(parts[2], TextType.TEXT)
                    ])
                elif len(parts) > 1:
                    raise Exception(f"Text Node does not properly terminate delimiters, should have two occurances of '{delimiter}'")
                else:
                    new_nodes.extend([node])
        return new_nodes

    # Markdown parser for images
    def extract_markdown_images(self, text: str):
        return  re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Markdown parser for links
    def extract_markdown_links(self, text: str):
        return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    # Splits nodes into new list by extracting images via regex
    def split_nodes_image(self, old_nodes: list):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT: # passthrough non-text nodes
                new_nodes.extend([node])
            else:
                matches = self.extract_markdown_images(node.text)  # list of tupels
                if len(matches) > 0:
                    text = node.text # will move through text
                    for match in matches:
                        image_alt = match[0]
                        image_link = match[1]
                        parts = text.split(f"![{image_alt}]({image_link})", 1) # split current position in text only once into image and rest
                        text = parts[1]
                        if parts[0] != "":
                            new_nodes.extend([
                                TextNode(parts[0], TextType.TEXT),
                            ])
                            
                        new_nodes.extend([
                            TextNode(image_alt, TextType.IMAGE, image_link),
                        ])

                    if text != "":
                        new_nodes.extend([
                            TextNode(text, TextType.TEXT)
                        ])
                else:
                    new_nodes.extend([node])
        return new_nodes

    # Splits nodes into new by extracting links via regex
    def split_nodes_link(self, old_nodes: list):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT: # passthrough non-text nodes
                new_nodes.extend([node])
            else:
                matches = self.extract_markdown_links(node.text)  # list of tupels
                if len(matches) > 0:
                    text = node.text # will move through text
                    for match in matches:
                        link_text = match[0]
                        url = match[1]
                        parts = text.split(f"[{link_text}]({url})", 1) # split current position in text only once into image and rest
                        text = parts[1]   
                        if parts[0] != "":
                            new_nodes.extend([
                                TextNode(parts[0], TextType.TEXT)
                            ])

                        new_nodes.extend([
                            TextNode(link_text, TextType.LINK, url)
                        ])

                    if text != "":
                        new_nodes.extend([
                            TextNode(text, TextType.TEXT)
                        ])
                else:
                    new_nodes.extend([node])
        return new_nodes

    # Uses above functions to split Text into nodes
    def text_to_textnodes(self, text):
        types_delimiters = TextNode.get_text_types_delimiters()
        nodes = [TextNode(text, TextType.TEXT)]
        for text_type, delimiter in types_delimiters.items():
            nodes = self.split_nodes_delimiter(nodes, delimiter, text_type)

        nodes = self.split_nodes_image(nodes)
        nodes = self.split_nodes_link(nodes)

        return nodes