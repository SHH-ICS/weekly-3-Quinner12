# I'm not sure who wrote this code, but it's got the exact same spelling errors in the comments as one of your classmates.  


import math
while True:
#pizza size imput
    print("What pizza size whould you like, Large or extra large ")
    PizzaSize = input()
    #loop
    if PizzaSize.lower() not in ["large", "extralarge"]:
        print("Thats not a size")
    else:
        break
#little comment
if PizzaSize=='Large':
    print("Good Pick")
elif PizzaSize== 'large':
    print("Good Pick")
else:
    print("Thats Big")
# adtifing price by size
if PizzaSize== 'large':
    PizzaSize= 6
elif PizzaSize== 'Large':
    PizzaSize= 6
else:
    PizzaSize= 10
#topping imput  
    print("How manny toppings whould you like 1-4")
while True:
    PizzaTop  = int(input(""))
    if PizzaTop > 4:
        print("We dont have that manny toppings pick a num 1-4")
        continue
    
    break
# identafying topping price
if PizzaTop == 1:
    PizzaTop= 1
elif PizzaTop == 2:
    PizzaTop= 1.75
elif PizzaTop == 3:
    PizzaTop= 2.50
else:
    PizzaTop= 3.35
#calculation
Pretotal = PizzaSize + PizzaTop 
Tax = Pretotal * 0.13
Total = Pretotal + Tax
print("Your Total is")
print(Total)
