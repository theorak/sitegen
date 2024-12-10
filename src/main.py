from textnode import TextNode, TextType
from htmlnode import HTMLNode


# main
def main():
    text_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(text_node)

    html_node = HTMLNode("a", "Google Link", [], {
        "href": "https://www.google.com", 
        "target": "_blank",
    })
    print(html_node)
    print(html_node.props_to_html())

main()