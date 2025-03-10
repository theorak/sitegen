# imports
import shutil
from textnode import TextNode, TextType
from nodeparser import Nodeparser

# main
def main():
    copy_recursive('static/', 'public/')

def copy_recursive(origin_dir, target_dir):
    shutil.rmtree(target_dir)
    shutil.copy(origin_dir, target_dir)

main()