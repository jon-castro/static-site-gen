from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        elif node.text_type == TextType.TEXT:
            text = node.text
            split_parts = text.split(delimiter)
            if len(split_parts) == 1:
                new_nodes.append(node)
                continue
            if len(split_parts) % 2 == 0:
                raise Exception(f"Invalid markdown: unmatched delimiter {delimiter}")
            
            for i in range(len(split_parts)):
                part = split_parts[i]
                if i % 2 == 0:
                    if part:
                        new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(part, text_type))                 
    
    return new_nodes