import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertEqual(node, node)
        
    def test_non_eq_type(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a test node", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)
    
    def test_non_eq_text(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        node2 = TextNode("This is another test node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)
        
    def test_null_url(self):
        node = TextNode("This is a test node", TextType.BOLD_TEXT)
        self.assertEqual(node.url, None)
        
    def test_non_null_url(self):
        node = TextNode("This is a test node", TextType.CODE_TEXT, "http://example.com")
        self.assertNotEqual(node.url, None)
        
if __name__ == "__main__":
    unittest.main()