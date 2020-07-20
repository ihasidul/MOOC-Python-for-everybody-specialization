# Use words.txt as the file name
fname = input("Enter file name: ")
#fname = "words.txt"
fh = open(fname)
fullFile = fh.read();
print(fullFile.upper().rstrip())     
