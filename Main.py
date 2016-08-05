from TextSummarizer import TextSummarizer
from Summarizers.file_reader import Reader

FILE_TO_READ = "Articles/professional_shortcomings.txt"
article = Reader(FILE_TO_READ).open_file_single_string()
udata = article.decode("utf-8")
article = udata.encode("ascii", "ignore")
ts = TextSummarizer(article)
ts.summarize()
