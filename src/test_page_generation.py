import unittest

from page_generation import extract_title

class TestMain(unittest.TestCase):
    def test_basic_title(self):
        markdown = "# Hello World\nSome content"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_title_with_extra_whitespace(self):
        markdown = "#    Lots of spaces    \nContent here"
        self.assertEqual(extract_title(markdown), "Lots of spaces")

    def test_title_with_special_chars(self):
        markdown = "# Title with *formatting* and **bold**\nMore content"
        self.assertEqual(extract_title(markdown), "Title with *formatting* and **bold**")

    def test_multiline_content(self):
        markdown = "Some intro\n# The Real Title\nMore content"
        self.assertEqual(extract_title(markdown), "The Real Title")

    def test_no_title_raises_exception(self):
        markdown = "No title here\nJust content"
        with self.assertRaises(Exception):
            extract_title(markdown)

    def test_ignore_second_level_header(self):
        markdown = "## This is not a title\nContent"
        with self.assertRaises(Exception):
            extract_title(markdown)

if __name__ == "__main__":
    unittest.main()