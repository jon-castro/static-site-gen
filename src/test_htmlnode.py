import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_new_node(self):
        node = HTMLNode("tag", "value", [HTMLNode(tag="tag1"), HTMLNode(tag="tag2")], {"target": "_blank", "test": "true"})
        assert node.tag == "tag"
        assert node.value == "value"
        assert node.children[0].tag == "tag1"
        assert node.children[1].tag == "tag2"
        assert node.props == {"target": "_blank", "test": "true"}
        
    def test_props_to_html(self):
        node = HTMLNode(props={"target": "_blank", "test": "true"})
        html_props = node.props_to_html()
        assert ' target="_blank"' in html_props
        assert ' test="true"' in html_props
        
    def test_htmlnode_without_attributes(self):
        node = HTMLNode()
        assert node.tag is None
        assert node.value is None
        assert node.children is None
        assert node.props is None