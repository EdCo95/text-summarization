# Abstract class for Summarizers.
# Written by Ed Collins 06 / 07 / 2016

# Imports 
from abc import ABCMeta, abstractmethod

class Summarizer:
    """Abstract class for different strategies for text summarization."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def summarize(self, article):
        pass
