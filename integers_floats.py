# SERIE 2 OF PRACTICE EXERCICES (STRING AND INTEGERS PART)
item_price ="19.99"
quantity = "3"

item_price = float(item_price)
quantity = int(quantity)

total_cost = item_price * quantity
print(f"the total of {quantity} items with {item_price}$ is {total_cost}$ ")

data = "current Humidity: 45% "
slicing = data.find("45")
print(slicing)
print(data[slicing:slicing+2])
sliced= int(data[slicing:slicing+2])
sliced = sliced / 100
print(type(sliced))
print(sliced)

user = "Alex"
score = 85
max_score = 100
percenteg = (score/max_score)* 100
report=f"""The Name: {user.upper()}
The score: {score}
The percenteg: {percenteg}% """ 
print("    the Report Card    ")
print(report)
