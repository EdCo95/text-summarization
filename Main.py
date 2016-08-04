from TextSummarizer import TextSummarizer
from Summarizers.file_reader import Reader

FILE_TO_READ = "Articles/1984.txt"
article = Reader(FILE_TO_READ).open_file_single_string()
ts = TextSummarizer(article)
ts.summarize()
