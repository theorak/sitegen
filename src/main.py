# imports
import os, shutil
from textnode import TextNode, TextType
from nodeparser import Nodeparser

# main
def main():
    copy_recursive('static/', 'public/')

def copy_recursive(origin_path: str, target_path: str, level: int = 0):
    if os.path.exists(target_path) and level == 0:
        print(f"cleanup at '{target_path}'")
        shutil.rmtree(target_path)
        os.mkdir('public/')
    elif level == 0:
        os.mkdir('public/')
    
    if os.path.exists(origin_path):
        contents = os.listdir(origin_path)
        if len(contents) > 0:
            for content in contents:
                current_path = os.path.join(origin_path, content)
                current_target_path = os.path.join(target_path, content)
                if os.path.isfile(current_path):
                    print(f"copying '{current_path}' to '{current_target_path}'")
                    shutil.copy(current_path, current_target_path)
                else:
                    level += 1
                    print(f"creating '{current_target_path}'")
                    os.mkdir(current_target_path)
                    copy_recursive(current_path, current_target_path, level)

main()