import re

def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    
    blocks = re.split(r'\n\s*\n', markdown)
    blocks = ['\n'.join(map(str.lstrip, block.splitlines())) for block in blocks]
    
    print(blocks)
    return blocks
