import unittest
import sys
sys.path.append("../")
from TextSummarization.TextSummarizer import TextSummarizer
from TextSummarization.Summarizers.Summarizer import Summarizer

class TextSummarizerTestCases(unittest.TestCase):
    """Tests for \"TextSummarizer.py\""""

    def test_initialisation_of_an_article_in_a_text_summarizer_object(self):
        ts = TextSummarizer("hello")
        self.assertEqual(ts.article, "hello")

    def test_setting_of_an_article_in_a_text_summarizer_object(self):
        ts = TextSummarizer("hello")
        ts.article = "new article!"
        self.assertEqual(ts.article, "new article!")

    def test_that_the_summarize_method_has_returned_something(self):
        ts = TextSummarizer("hello")
        self.assertNotEqual(ts.summarize(), None)

    def test_that_the_summarizer_object_is_an_instance_of_a_summarizer_object(self):
        ts = TextSummarizer("hello")
        self.assertIsInstance(ts.summarizer, Summarizer)

if __name__ == '__main__':
    unittest.main()
