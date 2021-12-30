def add (x, y):
    return x + y
def sub (x, y):
    return x - y
def mutliply (x, y):
    return x * y
def div (x,y):
    return x / y
exit = False
while exit == False:

    exit_ = input("Keep using? Y or N: ")

    if exit_ == "n".lower():
        break

    
    x = int(input("Pick a number: "))

    y = int(input("Pick another number: "))

    op = int(input("1:Add , 2:Sub  , 3:Mutli , 4:Div : "))

    if op == 1: 
        print(add(x,y))

    if op == 2:
        print(sub(x,y))

    if op == 3:
        print(mutliply(x,y))

    if op == 4:
        print(div(x,y))





