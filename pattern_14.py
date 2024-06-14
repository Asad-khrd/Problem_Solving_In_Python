# C 
# B C 
# A B C 

def pattern(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            char = "A"
            char = chr(ord(char)+(no-1)-(i-j))
            print(f"{char} ", end="")
        print("")


no = int(input("Enter the number: "))
pattern(no)

# 3 
# 2 3 
# 1 2 3 

def pattern_no(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(f"{no-(i-j)} ", end="")
        print("")

no = int(input("Enter the no: "))
pattern_no(no)