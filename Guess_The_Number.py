import random 

num = random.randint(1,3)
num_trys = 3

for i in range(0, 3): 
    
    print("You only get this many tries :", num_trys)
    user = int(input("Guess the number : "))
    if user == num:
        print("You Win!")
        break
    if user != num:
        num_trys = num_trys -1 

        if num_trys > 0:
            print("Keep trying!")
        if num_trys == 0: 
            print("You lost")
            break
    
