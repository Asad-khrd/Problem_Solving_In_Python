# 1
# 22
# 333

def pattern(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(f"{i}", end="")
        print("")


no = int(input("Enter the number: "))
pattern(no)