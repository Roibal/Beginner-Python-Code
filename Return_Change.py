import math

"""
The Purpose of this program is to calculate the amount of change required after a purchase,
and return the correct amount of Dollars, Quarters, Dimes, Nickels and Pennies.

Copyright Joaquin Roibal, 8/28/2016
"""

def ChangeCalculator(item_bill, cash_received):
    change = cash_received - item_bill          #Calculate Change Owed To Customer
    num_dollars = num_quarters = num_dimes = num_nickels = num_pennies = 0
    if change<0:
        return "You must pay an amount greater than the bill!"  #Demand Proper Payment!
    else:
        while change>0.01:                  #Until Returnable Change less than one penny
            if change>1:
                num_dollars = math.floor(change)        #Calculate Dollars
                change -= num_dollars
                change = round(change, 2)
                #print(change, num_dollars)
            elif change>0.25:
                num_quarters = math.floor(change/0.25)      #Calculate Quarters
                change -= num_quarters*0.25
                change = round(change, 2)
            elif change>0.10:
                num_dimes = math.floor(change/.1)           #Calculate Dimes
                change -= num_dimes*0.1
                change = round(change, 2)
            elif change>0.05:
                num_nickels = math.floor(change/0.05)       #Calculate Nickels
                change -= num_nickels*0.05
                change = round(change, 2)
            elif change>0.01:
                num_pennies = change/0.01                   #Calculate Pennies
                change -= num_pennies*0.01
                change = round(change, 2)
        return [num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]

def main():
    user_bill = input("What is the total cost of your items?")
    user_cash = input("How Much Are you paying?")
    ch = ChangeCalculator(float(user_bill), float(user_cash))
    print("Dollars: ", ch[0])
    print("Quarters: ", ch[1])
    print("Dimes: ", ch[2])
    print("Nickels: ", ch[3])
    print("Pennies: ", ch[4])

    rt = []
    examples = [(13.87, 20.00), (19.99, 20.00), (11.03, 40.00)]
    for ex in examples:
        rt.append(ChangeCalculator(ex[0], ex[1]))

    for ch in rt:
        print("Dollars: ", ch[0])
        print("Quarters: ", ch[1])
        print("Dimes: ", ch[2])
        print("Nickels: ", ch[3])
        print("Pennies: ", ch[4])

if __name__=="__main__":
    main()