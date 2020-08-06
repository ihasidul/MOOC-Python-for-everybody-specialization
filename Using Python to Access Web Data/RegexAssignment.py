import re
name = "regex_sum_755663.txt" 
handle = open(name,'r')
#print(handle.read())
y = re.findall('[0-9]+',handle.read())
sum = 0
for num in y:
    sum += int(num)

print(sum)


