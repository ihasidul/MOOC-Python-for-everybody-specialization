name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = list()
temp = list()
for line in handle:
    if line.startswith("From "):
        temp = line.split() 
        mails.append(temp[5])
#print(mails)
nums = list()
for time in mails:
    var = time.split(":")
    nums.append(var[0])
    #print(var)
cmail = dict()
for num in nums:
    cmail[num] = cmail.get(num,0) + 1
sortedNums = sorted(cmail)
for n in sortedNums:
    print(n, cmail[n])