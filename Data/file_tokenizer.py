"""This program reads in files and tokenizes them before writing them out, suitable for manual summary."""

# Import statements
from nltk.tokenize import sent_tokenize
import os

# Defines the number of files to tokenize
NUMBER_OF_FILES = 100

# Iterate over all of the files
for i in range(1, NUMBER_OF_FILES + 1):

    # Filename is a combination of "article" + number + ".txt"
    filename_to_read = "Data/Raw_Articles/article" + str(i) + ".txt"
    filename_to_write = "Data/Tokenized_Articles/article" + str(i) + ".txt"

    # Open and read the file, checking whether it already exists first
    if os.path.exists(filename_to_write):
        continue

    with open(filename_to_read) as fp:
        file_contents = fp.read()

    # Format the string correctly into ASCII to avoid strange errors - this could do with some more attention so the conversion to ASCII isn't necessary - work out how to do this all with UTF-8
    udata = file_contents.decode("utf-8")
    file_contents = udata.encode("ascii", "ignore")

    # Close the file
    fp.close()

    # Split into sentences
    sentences = sent_tokenize(file_contents)

    # Write the split sentences with a newline between each sentence
    fp = open(filename_to_write, "w+")

    for sentence in sentences:
        #sentence = sentence.replace('\n', '')
        fp.write(sentence + "\n\n\n")

    # Close the file for writing
    fp.close()
