class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        string_props_list = []
        for key, value in self.props.items():
            string_props_list.append(
                f' {key}="{value}"'
            )
        joined_props = "".join(string_props_list)
        return joined_props
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.tag == "img":
            return f'<img{self.props_to_html()}>'
        elif self.value is None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag is None:
            return f'{self.value}'
        elif not self.props:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        elif self.children is None or len(self.children) == 0:
            raise ValueError("All parent nodes must have children")
        else:
            inner_html = "".join(child.to_html() for child in self.children)
            return f'<{self.tag}{self.props_to_html()}>{inner_html}</{self.tag}>'