print("Welcome to my calculator")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit")
print()

while True:
    a=int(input("Enter an option:"))
    if a==1:
        add()
    elif a==2:
        sub()
    elif a==3:
        mul()
    elif a==4:
        div()
    elif a==5:
        break
    else:
        print("enter correct option")
    
