"""Used to create the files to paste the raw articles into."""

for i in range(14, 100):
    filename = "Data/Raw_Articles/article" + str(i) + ".txt"
    fp = open(filename, "w+")
    fp.write("")
    fp.close()
