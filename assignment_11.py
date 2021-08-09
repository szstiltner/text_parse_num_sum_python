import re

# Parses text file, extracts numbers in file and computes sum 

name = input("Enter file:")
if len(name) < 1 : name = "assignment_11.txt"
handle = open(name)
numlist = list()

for line in handle:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    for num in nums:
        num = int(num)
        if num == 0: continue 
        numlist.append(num)

print(sum(numlist))






# for line in handle:
#     words = line.split()
#     print(words)