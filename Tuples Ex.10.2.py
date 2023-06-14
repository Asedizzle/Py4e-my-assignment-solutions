'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
time_list =[]
time_d ={}
file = "mbox-short.txt"
with open(file) as fhand:
    for line in fhand:
        if line.startswith("From "):
            #print(line)
            words = line.split()
            time =words[5]
            #print(time)
            time_parts = time.split(":")
            hour = time_parts[0]
            time_list.append(hour)
    
#print(time_list)
x = sorted(time_list)
#print(x)

for i in x:
 time_d[i] = time_d.get(i,0) + 1
 
#print(time_d)
for k,v in time_d.items():
    print(k,v)
