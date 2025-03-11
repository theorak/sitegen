from enum import Enum
from textnode import TextNode, TextType, TextTypeDelimiters
from leafnode import LeafNode
from parentnode import ParentNode
from htmlnode import HTMLNode
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

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
            case TextType.ITALIC2:
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
    def split_nodes_delimiter(self, old_nodes: list):
        new_nodes = []
        for node in old_nodes:
            if node.text_type != TextType.TEXT: # passthrough non-text nodes
                new_nodes.append(node)
            else:
                parts = re.split(TextTypeDelimiters.PATTERN.value, node.text) # split text into occourences, then sort into typed nodes and plain text
                for part in parts:
                    if part.startswith(TextTypeDelimiters.BOLD.value) and part.endswith(TextTypeDelimiters.BOLD.value):
                        new_nodes.append(TextNode(part[2:-2], TextType.BOLD))
                    elif (part.startswith(TextTypeDelimiters.ITALIC.value) and part.endswith(TextTypeDelimiters.ITALIC.value)):
                        new_nodes.append(TextNode(part[1:-1], TextType.ITALIC))
                    elif (part.startswith(TextTypeDelimiters.ITALIC2.value) and part.endswith(TextTypeDelimiters.ITALIC2.value)):
                        new_nodes.append(TextNode(part[1:-1], TextType.ITALIC))
                    elif part.startswith(TextTypeDelimiters.CODE.value) and part.endswith(TextTypeDelimiters.CODE.value):
                        new_nodes.append(TextNode(part[1:-1], TextType.CODE))
                    else:
                       new_nodes.append(TextNode(part, TextType.TEXT))
                
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
    def text_to_textnodes(self, text: str):
        nodes = [TextNode(text, TextType.TEXT)]

        nodes = self.split_nodes_delimiter(nodes)
        nodes = self.split_nodes_image(nodes)
        nodes = self.split_nodes_link(nodes)

        return nodes
    
    # Creates list of blocks/paragraphs by splitting text along markdown (no nesting yet)
    def markdown_to_blocks(self, markdown: str):
        markdown = markdown.strip()
        lines = markdown.split('\n\n')
        lines = list(filter(lambda x : x.strip(), lines))
        lines = list(filter(lambda x : x is not None, lines))
        return lines
    
    # return block type for each markdown syntax, checking first 3 characters
    def block_to_block_type(self, markdown: str):
        first = markdown[0]
        second = markdown[1:2]
        three = markdown[:3]
        if first == "#":
            return BlockType.HEADING
        elif first == ">":
            return BlockType.QUOTE
        elif three == "```":
            return BlockType.CODE
        elif (first == "*" or first == "-") and second == " ":
            return BlockType.UNORDERED_LIST
        elif first.isnumeric() and second == ".":
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH

    # Finally turns markdown into html nodes, including nested children            
    def markdown_to_html_node(self, markdown: str) -> ParentNode:
        blocks = self.markdown_to_blocks(markdown)
        children = []
        for block in blocks:
            html_node = self.block_to_html_node(block)
            children.append(html_node)
        return ParentNode('div', children, None)    
    
    # Using helper functions below to format a ParentNode (HTMLNode) for each BlockType
    def block_to_html_node(self, block):
        block_type = self.block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            return self.paragraph_to_html_node(block)
        if block_type == BlockType.HEADING:
            return self.heading_to_html_node(block)
        if block_type == BlockType.CODE:
            return self.code_to_html_node(block)
        if block_type == BlockType.ORDERED_LIST:
            return self.olist_to_html_node(block)
        if block_type == BlockType.UNORDERED_LIST:
            return self.ulist_to_html_node(block)
        if block_type == BlockType.QUOTE:
            return self.quote_to_html_node(block)
        raise ValueError("invalid block type")
    
    # Collector for children nodes, appends each TextNode
    def text_to_children(self, text):
        text_nodes = self.text_to_textnodes(text)
        children = []
        for text_node in text_nodes:
            html_node = self.text_node_to_html_node(text_node)
            children.append(html_node)
        return children

    def paragraph_to_html_node(self, block):
        lines = block.split("\n")
        paragraph = " ".join(lines)
        children = self.text_to_children(paragraph)
        return ParentNode("p", children)

    def heading_to_html_node(self, block):
        level = 0
        for char in block:
            if char == "#":
                level += 1
            else:
                break
        if level + 1 >= len(block):
            raise ValueError(f"invalid heading level: {level}")
        text = block[level + 1 :]
        children = self.text_to_children(text)
        return ParentNode(f"h{level}", children)

    def code_to_html_node(self, block):
        if not block.startswith("```") or not block.endswith("```"):
            raise ValueError("invalid code block")
        text = block[4:-3]
        raw_text_node = TextNode(text, TextType.TEXT)
        child = self.text_node_to_html_node(raw_text_node)
        code = ParentNode("code", [child])
        return ParentNode("pre", [code])

    def olist_to_html_node(self, block):
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[3:]
            children = self.text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ol", html_items)

    def ulist_to_html_node(self, block):
        items = block.split("\n")
        html_items = []
        for item in items:
            text = item[2:]
            children = self.text_to_children(text)
            html_items.append(ParentNode("li", children))
        return ParentNode("ul", html_items)

    def quote_to_html_node(self, block):
        lines = block.split("\n")
        new_lines = []
        for line in lines:
            if not line.startswith(">"):
                raise ValueError("invalid quote block")
            new_lines.append(line.lstrip(">").strip())
        content = " ".join(new_lines)
        children = self.text_to_children(content)
        return ParentNode("blockquote", children)