"""This program reads in tokenized files and scans for sentences that were manually marked, and then writes them into the Manual_Summaries folder."""

# Import statements
from nltk.tokenize import sent_tokenize

# Defines the number of files to tokenize
NUMBER_OF_FILES = 12

# Shows how many sentences are in all of the data gathered so far
SENTENCE_COUNT = 0

# Iterate over all of the files
for i in range(1, NUMBER_OF_FILES + 1):

    # Filename is a combination of "article" + number + ".txt"
    filename_to_read = "Data/Tokenized_Articles/article" + str(i) + ".txt"
    filename_to_write = "Data/Manual_Summaries/article" + str(i) + ".txt"

    # Open and read the file
    with open(filename_to_read) as fp:
        file_contents = fp.read()

    # Format the string correctly into ASCII to avoid strange errors - this could do with some more attention so the conversion to ASCII isn't necessary - work out how to do this all with UTF-8
    udata = file_contents.decode("utf-8")
    file_contents = udata.encode("ascii", "ignore")

    # Close the file
    fp.close()

    # Split into sentences
    sentences = sent_tokenize(file_contents)

    # Ascertain which sentences are part of the summary and create a list of them
    summary_sentences = []

    for sentence in sentences:
        SENTENCE_COUNT += 1
        if sentence[0] == "1":
            sentence = sentence[1:]
            summary_sentences.append(sentence)

    # Write the split sentences with a newline between each sentence
    fp = open(filename_to_write, "w+")

    for sentence in summary_sentences:
        fp.write(sentence + "\n\n")

    # Close the file for writing
    fp.close()

# Print the sentence count to see how many items of data we have gathered
print "Total number of sentences gathered to date: " + str(SENTENCE_COUNT)
