import re
num = []
fhand = open("Actual data.txt")
for line in fhand:
    x = re.findall("[0-9]+" , line)
    for i in x:
        num.append(int(i))
        
print(num)

print(sum(num))