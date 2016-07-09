import unittest
import sys
sys.path.append("../")

from TextSummarization.TextSummarizer import TextSummarizer
from TextSummarization.Summarizers.Summarizer import Summarizer
from TextSummarization.Summarizers.SummarizeBySentenceAnalysis import SummarizeBySentenceAnalysis


class SentenceAnalysisSummarizerTestCases(unittest.TestCase):
    """Tests for \"SummarizeBySentenceAnalysis.py\"."""

    def test_the_getters_and_setters_of_article(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        summarizer.article = "hello"
        self.assertEqual(summarizer.article, "hello")

    def test_the_getters_and_setters_of_summary(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        summarizer.summary = "hello"
        self.assertEqual(summarizer.summary, "hello")

    def test_the_getters_and_setters_of_summary_percentage(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        summarizer.summary_percentage = 0.2
        self.assertEqual(summarizer.summary_percentage, 0.2)

    def test_the_getters_and_setters_of_metric_calculator(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        summarizer.metric_calculator = "hello"
        #This test is not equal because you shouldn't be able to set the metric calculator variable to anything other than a MetricCalculator object.
        self.assertNotEqual(summarizer.metric_calculator, "hello")

    def test_the_initialisation_of_the_summary_percentage(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        self.assertEqual(summarizer.summary_percentage, 0.5)

    def test_that_the_summarize_method_returns_something(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        self.assertNotEqual(summarizer.summarize("hello"), None)

    def test_that_the_separate_sentences_method_separates_sentences(self):
        summarizer = summarizer = SummarizeBySentenceAnalysis(0.5)
        sentence = "Hello! Goodbye!"
        self.assertEqual(summarizer.separateSentences(sentence), [("Hello!", "hello"), ("Goodbye!", "goodbye")])

    def test_that_the_read_common_words_method_has_read_something(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        self.assertNotEqual(summarizer.readCommonWords(), None)

    def test_that_the_count_words_method_does_not_count_common_words(self):
        summarizer = SummarizeBySentenceAnalysis(0.5)
        self.assertEqual(summarizer.countWords("hello of", summarizer.readCommonWords()), [("hello", 1)])


if __name__ == '__main__':
    unittest.main()
