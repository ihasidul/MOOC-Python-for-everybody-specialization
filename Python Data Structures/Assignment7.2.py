# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fname = "mbox-short.txt"
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    cf = float(line[20:])
    total = total + cf 
    count += 1
    
    #print(len(line))
avg = total/count
print("Average spam confidence:",avg)