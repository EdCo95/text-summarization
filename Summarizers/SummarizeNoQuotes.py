# Concrete implementation of a summarizer.
# Written by Ed Collins 06 / 07 / 2016

# Imports and global variables
from Summarizer import Summarizer
from MetricCalculators.MetricCalculator import MetricCalculator
from MetricCalculators.BasicCalculator import BasicCalculator
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from file_reader import Reader
from operator import itemgetter
import string
import math

class SummarizeNoQuotes(Summarizer):
    """Summarizes articles by analysing each sentence in the article and then giving it a score. The highest scored sentences are kept which generate a summary of the article. This version ignores all quotations."""

    def __init__(self, summary_percentage):
        self._article = ""
        self._summary = ""
        self._summary_percentage = summary_percentage
        self._metric_calculator = BasicCalculator()

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
    def summary_percentage(self):
        return self._summary_percentage

    @summary_percentage.setter
    def summary_percentage(self, new_value):
        self._summary_percentage = new_value

    @property
    def metric_calculator(self):
        return self._metric_calculator

    @metric_calculator.setter
    def metric_calculator(self, new_calculator):
        if isinstance(new_calculator, MetricCalculator):
            self._metric_calculator = new_calculator
        else:
            print "The new metric calculator must be an instance of MetricCalculator"

    def summarize(self, article):
        """Invokes other methods of the class in order to create a summary of an article from its component sentences."""
        common_words = self.readCommonWords()
        counted_words = self.countWords(article, common_words)
        sentences = self.separateSentences(article)
        sentences_and_scores = self.scoreSentences(sentences, counted_words)
        final_summary = self.createSummary(sentences_and_scores)
        self.printSummary(final_summary)
        return final_summary

    def countWords(self, article, common_words):
        """Counts the number of occurences of each words that is not a common word in the article."""

        # Split the article into a list of words
        article = article.split()

        # Start with two empty lists - one for the non-common words that appear in the article and another for the count of how many times they occur.
        words = []
        counts = []

        for word in article:
            # Perform some basic formatting to each word, removing punctuation and making it lower case, for purposes of comparision with the common words list.
            word = word.translate(string.maketrans("", ""), string.punctuation)
            word = word.lower()

            # If the word is a common word, skip over it.
            if word in common_words:
                continue

            # Add the word to the words list if it is not already present
            if word not in words:
                words.append(word)

        # Initialise the counts list to be all zeros
        for i in range(0, len(words)):
            counts.append(0)

        for word in article:
            word = word.lower()
            word = word.translate(string.maketrans("", ""), string.punctuation)

            if word in common_words:
                continue

            # Add one to the count every time a word is seen
            counts[words.index(word)] += 1

        # Zip the words and counts together to form tuples of (word, number of occurences)
        words_and_counts = zip(words, counts)

        # Sort list of words and counts by the number of occurences of each word
        sorted_word_list = sorted(words_and_counts, key = itemgetter(1))

        return sorted_word_list

    def separateSentences(self, article):
        """This method returns a list of tuples of the form (sentence, sentence with formatting removed). The sentences with formatting removed are necessary for scorring the sentences."""

        sentence_list = sent_tokenize(article)
        raw_list = []
        quote = "\""
        for sentence in sentence_list:
            if quote in sentence:
                sentence_list.remove(sentence)
            formated_sentence = sentence.lower()
            formated_sentence = formated_sentence.translate(string.maketrans("", ""), string.punctuation)
            raw_list.append(formated_sentence)

        sentence_list = zip(sentence_list, raw_list)
        return sentence_list

    def readCommonWords(self):
        """Reads the list of common words that should not be included in the scoring of each sentence such as \"and\" and \"or\"."""
        common_words = Reader("common_words.txt").open_file()
        return common_words

    def scoreSentences(self, sentences, word_counts):
        """Makes use of the MetricCalculator object to calculate the score for each sentence and thus whether it should be included."""
        scores = self.metric_calculator.calculateMetrics(sentences, word_counts)
        return scores

    def createSummary(self, sentences_and_scores):
        """Creates the actual summary of the article using the list of sentences and their respective scores."""

        # Calculate how many sentences should be included in the summary as a percentage of the total number in the article
        num_of_sentences = len(sentences_and_scores)
        sentences_to_summarize = int(math.ceil(num_of_sentences * self.summary_percentage))

        # Get the sentences that summarize the article
        summary_sentences = sentences_and_scores[0:sentences_to_summarize]

        # Sort them according to the order that they appear so that the summary makes sense
        ordered_summary_sentences = sorted(summary_sentences, key = itemgetter(2))

        # Generate the summary
        summary = ""

        for item in ordered_summary_sentences:
            summary += " " + item[0][0]

        return summary

    def printSummary(self, summary):
        """Prints the summary in a pretty manner."""

        print "\n\n"
        print "\t\t*****************************************"
        print "\t\t************ ARTICLE SUMMARY ************"
        print "\t\t*****************************************"
        print "\n\n"
        print summary
        print "\n\n"
