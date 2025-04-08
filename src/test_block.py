import unittest

from block import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph
    
    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line
    
    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type_heading(self):
        block = "# Heading 1"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "###### Heading 6"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "####### Not a heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        block = "```python\nprint('hello')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "```python\nprint('hello')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "> Quote line 1\n> Quote line 2"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "> Quote line 1\nNot a quote line"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "- Item 1\n  - Subitem"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "1. First item\n3. Second item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        block = "2. Item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_paragraph(self):
        block = "This is a simple paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
            md = """
    This is **bolded** paragraph
    text in a p
    tag here

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
            )

    def test_paragraphs(self):
            md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

    def test_lists(self):
            md = """
    - This is a list
    - with items
    - and _more_ items

    1. This is an `ordered` list
    2. with items
    3. and more items

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
            )

    def test_headings(self):
            md = """
    # this is an h1

    this is paragraph text

    ## this is an h2
    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
            )

    def test_blockquote(self):
            md = """
    > This is a
    > blockquote block

    this is paragraph text

    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
            )

    def test_code(self):
            md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )