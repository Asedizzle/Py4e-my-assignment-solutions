'''7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''

list_of_numbers = []
count = 0
filename = input("Please input the name of a file")
if len(filename) < 1:
        print("Please enter a valid file name")
with open(filename ,"r") as fhand:
    

    for line in fhand:
        if line.startswith("X-DSPAM-Confidence: "):
            count += 1
            words = line.split()
            value = float(words[-1])
            list_of_numbers.append(value)
        

#since I cant use sum
finalvalue = 0
for value in list_of_numbers:
    finalvalue = finalvalue + value
average = (finalvalue/count)
print("Average spam confidence:",average)