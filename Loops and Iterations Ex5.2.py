k = []
largest = None
smallest = None
while True:
   
    user_input = input("Please enter a number")
    if user_input == "done": 
            break
    
    try:
        x = int(user_input)
        k.append(x)
        
    except: 
        print("Please enter a valid number")
    
#print(k)
largest = max(k)
smallest = min(k)

print("Maximum is ", largest)
print("Minimum is ", smallest)