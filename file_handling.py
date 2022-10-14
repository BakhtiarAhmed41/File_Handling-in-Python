def stats(filename):
    file = open(filename, "r")
    read = file.read()
    print("The number of CHARACTERS in the given file is = ", len(read))
    spltlines = read.splitlines()
    print("The number of LINES in the given file =", len(spltlines))
    spltwords = read.split()
    print("The number of WORDS in the given file =", len(spltwords))

stats(r"C:\Users\dell\Documents\Counting.txt")          #you will give the file location inside the parenthesis
