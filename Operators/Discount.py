'''Real world example using Operator
This program about user get 20 percent discount on total is greater than 11000 with tax '''

amount = 10000
tax = amount * 0.18 # 18% GST
total = amount+tax
print("Total Amount:",total)

if total > 11000:
    discount = total * 0.20 #20% discount
    total -= discount

print("Total Amount with Discount:",total)