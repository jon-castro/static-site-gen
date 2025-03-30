import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        
    def test_leaf_image_tag(self):
        node = LeafNode("a", "Hello, world!", {"target": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a target="https://www.google.com">Hello, world!</a>')
        
    def test_leaf_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_parent_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertRaises(ValueError, parent_node.to_html)
        
    def test_parent_no_tag(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        self.assertRaises(ValueError, parent_node.to_html)