# imports
import os, shutil, re
from textnode import TextNode, TextType
from nodeparser import Nodeparser

# main
def main():
    copy_recursive('static/', 'public/')
    generate_page('content/index.md', 'template.html', 'public/index.html')

def generate_page(from_path: str, template_path: str, dest_path: str):
    if os.path.isfile(from_path) and os.path.isfile(template_path):
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")

        md_file = open(from_path)
        markdown = md_file.read()
        temp_file = open(template_path)
        template = temp_file.read()
        
        title = extract_title(markdown)
        html_node = Nodeparser().markdown_to_html_node(markdown)
        html_string = html_node.to_html()

        template = template.replace('{{ Title }}', title)
        template = template.replace('{{ Content }}', html_string)

        page_file = open(dest_path, 'wt')
        page_file.write(template)
        page_file.close()
        md_file.close()
        temp_file.close()
    else:
        print("Please provide a valid markdown and template files")

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

def extract_title(markdown: str):
    # Pattern to match a line starting with a single # followed by space and capture the rest
    pattern = r'^# (.+)$'
    match = re.search(pattern, markdown, re.MULTILINE)

    if match:
        return match.group(1).strip()
    else:
        raise Exception("No h1 header found")

main()