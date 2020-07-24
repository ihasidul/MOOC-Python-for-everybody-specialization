fname = input("Enter file name: ")
#fname = "romeo.txt"
fh = open(fname)

lst = list()
words = list()
for line in fh:
    lst = line.split()
    for word in lst:
        if(word in words):
            continue 
        else:
            words.append(word)
words.sort()
print(words)
