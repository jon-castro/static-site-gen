import unittest

from textnode import TextNode, TextType
from inline import (
    split_nodes_delimiter, 
    extract_markdown_images, 
    extract_markdown_links, 
    split_nodes_image, 
    split_nodes_link
)


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0], TextNode('This is text with a ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('bold', TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(' word', TextType.TEXT))
            
    def test_split_nodes_delimiter_italic(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0], TextNode('This is text with a ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('italic', TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(' word', TextType.TEXT))
        
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with `code` inside", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0], TextNode('This is text with ', TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode('code', TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(' inside', TextType.TEXT))
        
    def test_split_nodes_delimiter_but_only_plain_text(self):
        node = TextNode("This is text with no delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0], TextNode('This is text with no delimiters', TextType.TEXT))

    def test_split_nodes_delimiter_but_image(self):
        node = TextNode("This is text for an image", TextType.IMAGE, 'https://example.com')
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0], TextNode('This is text for an image', TextType.IMAGE, 'https://example.com'))
        
    def test_split_nodes_unmatched_delimiter(self):
        node = TextNode("This is text with **unmatched delimiters", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)
        
    def test_split_nodes_delimiter_with_empty_delimited_text(self):
        node = TextNode("This is text with an empty __ delimiter", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[1], TextNode('', TextType.ITALIC))

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"),
                              ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://www.google.com) and another [second link](https://www.bing.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://www.bing.com"
                ),
            ],
            new_nodes,
        )