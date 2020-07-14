largest = None
smallest = None
while True:
    num = input()       
    if num == "done":
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    
    try:
        
        num = int(num)
        #this is for getting the largest number 
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
        elif largest > num:
            largest = largest
        #this if for getting the smallest number
        if  smallest is None:
            smallest = num
        elif smallest > num:
             smallest = num
        elif smallest < num:
            smallest = smallest
    except:
        print("Invalid input")
    


