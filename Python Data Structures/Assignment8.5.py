fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
mail = list()
words = list()
for line in fh:
        if(line.startswith("From:")):
            continue
        elif(line.startswith("From")):
            temp = line.split()
            print(temp[1])
            count += 1                
print("There were", count, "lines in the file with From as the first word")
                                                    
