hours = float(input("Please enter the number of hours you work"))
rate = float(input("Please enter the rate per hour"))   

def computepay(hours,rate):
    
    if hours <= 40:
        pay = hours * rate
    
    else:
       pay = (40 * rate) + ((hours - 40)*(rate)*(1.5))
    
    return pay
    
your_pay = computepay(hours, rate)
print("Pay", your_pay)
   
