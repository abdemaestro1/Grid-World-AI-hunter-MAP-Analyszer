#Input 1      Input 2
#------------------------
#  0.731250     0.750360
#  0.766444     0.730729
#  0.698135     0.767707
#  0.822379     0.695499

def main():
    print("this is a chaotic function ")
    n=eval(input("how many times the loop must work:"))
    x= eval(input("enter a number between 1 and 10:"))
    y=eval(input("enter a number between 1 and 10:"))
    print("Input 1     Input 2")
    print("---------------------")
    for i in range(n):
       x= 3.9*x*(1-x)
       y= 3.9*y*(1-y)
       print(x,y)
main()  




