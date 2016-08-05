# Text Summarizer class for automatic text summary.
# Written by Ed Collins 06 / 07 / 2016

# Global variables and imports
from Summarizers.Summarizer import Summarizer
from Summarizers.SummarizeBySentenceAnalysis import SummarizeBySentenceAnalysis
from Summarizers.SummarizeNoQuotes import SummarizeNoQuotes
from Summarizers.BookSummarizer import BookSummarizer

DEBUG = True

class TextSummarizer(object):
    """Takes a piece of text, for example a news article, and automatically generates a summary of it. Designed according to the strategy design pattern.

    Attributes:
        article        The article to summarize.
        summary        The summary of the article.
        summarizer     The object used to summarize the article."""

    def __init__(self, article):
        self._article = article
        self._summary = ""
        self._summarizer = SummarizeBySentenceAnalysis(0.1)

    @property
    def article(self):
        return self._article

    @article.setter
    def article(self, new_article):
        self._article = new_article

    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, new_summary):
        self._summary = new_summary

    @property
    def summarizer(self):
        return self._summarizer

    @summarizer.setter
    def summarizer(self, new_summarizer):
        self._summarizer = new_summarizer

    def summarize(self):
        """Takes the article and produces a summary of it."""

        if self.summarizer == None:
            return "The summarizer has not been initialised"
        elif not isinstance(self.summarizer, Summarizer):
            raise TypeError("summarizer is not a Summarizer object")

        self.summary = self.summarizer.summarize(self.article)
        return self.summary
