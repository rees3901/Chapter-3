income = float(input("Enter the annual income: "))
tax = 0

  #if the citizen's income was not higher than 85,528 thalers, 
#the tax was equal to 18% of the income minus 556 thalers and 2 cents 
#(this was the so-called tax relief)
if income <= 85528:
    tax = (income *0.18)- 556.02
    #get 18% of the income (put in in brackets to calc first), then minus 556.02 from that 
    
else: #income > 85,528:
    #tax = income - 14,839.02- NO this is wrong
    surplus = (income - 85528)
    tax = surplus *0.32 +14839.02
#other, minus

#if the income was higher than this amount, 
#the tax was equal to 14,839 thalers and 2 cents, 
#plus 32% of the surplus over 85,528 thalers.
# Write your code here.
#

tax = round(tax, 2)
print("The tax is:", tax, "thalers")
