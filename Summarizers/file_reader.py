# Class to simplify the reading of text files in Python.
# Created by Ed Collins on Tuesday 7th June 2016.

class Reader:
    """Simplifies the reading of files to extract a list of strings. Simply pass in the name of the file and it will automatically be read, returning you a list of the strings in that file."""

    def __init__(self, name):
        """\"name\" is the name of the file to open. The file should be a series of lines, each line separated with a newline character."""
        self.name = name;

    def open_file(self):
        """Reads the file given by the file name and returns its contents as a list of seperate strings, each string being a line in the file."""
        with open(self.name) as fp:
            contents = fp.read().split()

        fp.close()
        return contents

    def open_file_single_string(self):
        """Reads the file given by the file name and returns its contents as a list of seperate strings, each string being a line in the file."""
        with open(self.name) as fp:
            contents = fp.read()

        fp.close()
        return contents
