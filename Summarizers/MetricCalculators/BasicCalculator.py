# Concrete implementation of a metric calculator.
# Written by Ed Collins 06 / 07 / 2016

# Imports and global variables
from MetricCalculator import MetricCalculator
from operator import itemgetter

class BasicCalculator(MetricCalculator):
    """Basic way of calculating the metric associated with each sentence."""

    def __init__(self):
        return None

    def calculateMetrics(self, sentences, word_counts):
        """Calculates a score for each sentence."""

        # Array to hold the scores for each sentence
        scores = []

        # Temporary variable to calculate the score for each sentence.
        total_score = 0

        # Remember that "sentences" is an array of tuples of the form (decorated sentence with punctuation and captials, lowercase and unpunctuated sentence)
        for sentence_tuple in sentences:

            # Word counts is also an array of tuples of the form (word, number of occurences in the article)
            for word in word_counts:
                if word[0] in sentence_tuple[1]:
                    total_score += word[1]

            scores.append(total_score)
            total_score = 0

        # Three things are zipped here - the sentences themselves, their scores, and ascending numbers which indicate the position of the sentence in the article, so that they can be correctly ordered when the summary is created.
        sentences_and_scores = zip(sentences, scores, range(1, len(sentences)))

        # Sort the sentence list according to their scores.
        sorted_sentences_and_scores = sorted(sentences_and_scores, key = itemgetter(1))

        # Reverse the list so that the most highly scored sentences come first
        sorted_sentences_and_scores = list(reversed(sorted_sentences_and_scores))
        
        return sorted_sentences_and_scores
