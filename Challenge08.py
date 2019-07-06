# Python By Example Book
# Challenge 008 - Ask for the total price of the bill, then ask how many diners there are.
# Divide the total bill by the number of diners and show how muich each person myust pay.

totalBill = int(input("What is the total bill? "))
Diners = int(input("How many diners? "))
ToPay = totalBill / Diners

print("Each diner has to pay £", ToPay)