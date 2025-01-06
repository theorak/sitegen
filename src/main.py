# imports
from textnode import TextNode, TextType
from nodeparser import Nodeparser

# main
def main():
    text_node = TextNode("Starting Main", TextType.BOLD)
    print(text_node)   

main()