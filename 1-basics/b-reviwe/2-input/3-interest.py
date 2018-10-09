import math
#ask user to enter current amount of saving
print("Please enter current amount of saving")
#read user respond


curent_amount=float(input())
#ask user to enter current amount of interest rate()
print("Please enter percantag interest rate")
Percent_rate=float(input())
#calculate the 
new_amount= (Percent_rate/100)*curent_amount
#print the result
New_Saving=curent_amount+new_amount
print("The new amount are:",round(New_Saving,2))

