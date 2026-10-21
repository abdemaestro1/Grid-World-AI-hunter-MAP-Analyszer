ism_dyali = """abderahmane ajbar is my first name """

print(len(ism_dyali))

print(ism_dyali[0:11])
print(ism_dyali[14:20])

print(ism_dyali.upper())
print(ism_dyali.lower())

print(ism_dyali.count("aj"))
print(ism_dyali.count("a"))

print(ism_dyali.find("aj"))
print(ism_dyali.find("bde"))

new = ism_dyali.replace("abderahmane","adam")
print(new)

age = 19
ism = "abde"
print(f"my name is {ism.capitalize()} i am {age} years old")

variable =f"i am {ism.upper()} i have {age} years old"
print(variable)

#print(dir(ism)) # KNOW WHAT FUNCTIONS YOU CAN USE IN THE STRING
#print(help(str))# KNOW WHAT  YOU CAN USE INTHE DATA TYPE 

#print(help(str.upper)) # know about a specifique function in the data type 

# SERIE 1 OF PRACTICE EXERCICES
my_string = "Automate Everything"  
user_input = "   learning python is FUN   "
plan = "i will learn javascript today"
print(len(my_string))

print(my_string[0])
print(my_string[18])

print(my_string[0:8])
print(my_string.find("Everything"))
print(my_string[9:])

print(user_input.lower())
print(user_input.upper())
print(user_input.count("n"))
print(user_input.find("python"))

new_plan= plan.replace("javascript","python") 
print(new_plan)

tool = "n8n"
task = "automation"
status = "complete"

print("n8n"+''+" automation"+''+" is"+''+" complete")
print(f"{tool.upper()} {task} is {status.upper()}!!")