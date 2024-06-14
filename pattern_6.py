# 1 
# 2 3 
# 4 5 6 

def pattern(no):
    count = 1
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(f"{count} ", end="")
            count+=1
        print("")


no = int(input("Enter the number: "))
pattern(no)