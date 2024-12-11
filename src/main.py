# imports
from textnode import TextNode, TextType
from leafnode import LeafNode

# main
def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node)   

# conversion of text nodes to html (leaf) nodes
def text_node_to_html_node(text_node: TextNode):
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

main()