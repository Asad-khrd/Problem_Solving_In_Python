# 1234554321
# 1234**4321
# 123****321
# 12******21
# 1********1

def pattern(no):
    for i in range(1,no+1):
        for j in range(1,no+1-(i-1)):
            print(f"{j}",end="")
        print("*"*((i*2)-2), end="")
        for k in range(no-(i-1),0,-1):
            print(f"{k}",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)