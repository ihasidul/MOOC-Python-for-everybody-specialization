name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mails = list()
temp = list()
for line in handle:
    if line.startswith("From "):
        #print(line)
        temp = line.split() 
        mails.append(temp[1])
cmail = dict()
for mail in mails:
    cmail[mail] = cmail.get(mail,0) + 1

themail = None
count = -1
#print(cmail)
for mail,val in cmail.items():
    if val > count:
        count = val 
        themail = mail
    
   
    
print(themail,count)
