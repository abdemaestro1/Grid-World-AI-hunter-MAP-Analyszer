#PROBLEM 1 
#print("*****converter programme******")
#kil=eval(input("Enter your distance en Kilometers: "))
#miles= kil*0.621371
#print("your distance in miles is:",miles)

#PROBLEM 2 

print("*****investment_calculator programme*****")
IniP=eval(input("Enter you primary amount:"))
AnnPR=float(input("Set your annual internet rate(en decimal ,n/100):"))
Contrub_Amount=eval(input("how much do you want to more invest(per year):"))
Num_Year=eval(input("how much years:"))


for i in range(Num_Year):
    IniP=IniP+Contrub_Amount
    intrest_earn=AnnPR*IniP
    total=IniP+intrest_earn
print("your total is:",total)

    
# investment.py

print("***** Investment Calculator *****")

# 1. Get user inputs with explicit data types
principal = float(input("Enter your primary amount: "))
apr = float(input("Set your annual interest rate (in decimal, e.g., 0.05): "))
annual_contribution = float(input("How much do you want to invest per year?: "))
years = int(input("How many years to invest?: "))

# 2. Counted for loop to update principal each year
for i in range(years):
    # Calculate interest earned on current balance
    interest_earned = principal * apr

    # Update principal by adding interest earned and annual contribution
    principal = principal + interest_earned + annual_contribution

# 3. Output final balance formatted to 2 decimal places
print(f"Your total balance after {years} years is: ${principal:.2f}")