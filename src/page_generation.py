import os
import shutil

from block import markdown_to_html_node


def copy_directory(source, destination):
    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)

        if os.path.isdir(source_path):
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)
            copy_directory(source_path, destination_path)
        elif os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)


def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_directory(source, destination)


def extract_title(markdown):
    lines = markdown.split('\n')

    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception("No H1 header found in the markdown")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()
        
    with open(template_path, 'r') as f:
        template_content = f.read()
        
    title = extract_title(markdown_content)
    
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    
    final_html = template_content.replace("{{ Title }}", title)
    final_html = final_html.replace("{{ Content }}", html_content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, 'w') as f:
        f.write(final_html)
        
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)
                rel_path = os.path.relpath(from_path, dir_path_content)
                rel_path_html = os.path.splitext(rel_path)[0] + ".html"
                destination_path = os.path.join(dest_dir_path, rel_path_html)
                
                generate_page(from_path, template_path, destination_path)