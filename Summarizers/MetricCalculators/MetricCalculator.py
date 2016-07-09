# Abstract class for MetricCalculators.
# Written by Ed Collins 06 / 07 / 2016

# Imports
from abc import ABCMeta, abstractmethod

class MetricCalculator:
    """Abstract class for different strategies of metric calculation"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def calculateMetrics(self, sentences, word_counts):
        pass
