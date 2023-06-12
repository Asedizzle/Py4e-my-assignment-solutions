file = input("Please input the name of the file")

dict_1 ={}

if len(file) < 1:
    file = "mbox-short.txt"
with open(file) as fhand:
    for line in fhand:
        if line.startswith("From "):
            words = line.split()
            sender = words[1]
            dict_1[sender] = dict_1.get(sender, 0) + 1
            
#print(dict_1)
            
highest = 0
big_word = None



for key,value in dict_1.items():
    if value > highest:
        highest = value
        big_word = key
        
print(big_word, highest)
            