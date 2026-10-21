#claulate the pourcentage of the molecules and precis molecular wight
carbon=int(input("how many you have of carbon:"))
oxygen=int(input("how many you have of oxygen:"))
hydrogen=int(input("how many you have of hydrogen:"))

Cweight=carbon*12.011
Hweight=hydrogen*1.00794
Oweight=oxygen*15.9994

total_weight=(Cweight)+(Hweight)+(Oweight)
print(f"the total wieght of your molecule is {total_weight:.4f}")

#The pourcentage of each Element 
Pcweight=(Cweight*100)/total_weight
Phweight=(Hweight*100)/total_weight
Poweight=(Oweight*100)/total_weight
print(f"we have:{Pcweight:.2f}% of carbone")
print(f"we have:{Phweight:.2f}% of hydrogene")
print(f"we have:{Poweight:.2f}% of oxygene")