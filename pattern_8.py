# 1 
# 2 1 
# 3 2 1 

def pattern(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(f"{i} ", end="")
            i-=1
        print("")


no = int(input("Enter the number: "))
pattern(no)