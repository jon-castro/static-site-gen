import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node, node)
        
    def test_non_eq_type(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is a test node", TextType.CODE)
        self.assertNotEqual(node, node2)
    
    def test_non_eq_text(self):
        node = TextNode("This is a test node", TextType.BOLD)
        node2 = TextNode("This is another test node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_null_url(self):
        node = TextNode("This is a test node", TextType.BOLD)
        self.assertEqual(node.url, None)
        
    def test_non_null_url(self):
        node = TextNode("This is a test node", TextType.CODE, "https://example.com")
        self.assertNotEqual(node.url, None)

    def test_text_html_node(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold_html_node(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        
    def test_italic_html_node(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        
    def test_code_html_node(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")
        
    def test_link_html_node(self):
        node = TextNode("This is a link node", TextType.LINK, "https://example.com")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        
    def test_image_html_node(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://example.com")
        html_node = node.text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props, {"src": node.url, "alt": node.text})
    
if __name__ == "__main__":
    unittest.main()