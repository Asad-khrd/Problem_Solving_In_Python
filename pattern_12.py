# A B C 
# B C D 
# C D E 

def pattern(no):
    for i in range(1,no+1):
        char = "A"
        char = chr(ord(char)+i-1)
        for j in range(1,no+1):
            print(f"{char} ", end="")
            char = chr(ord(char)+1)
        print("")


no = int(input("Enter the number: "))
pattern(no)

# 1 2 3 
# 2 3 4 
# 3 4 5 

def pattern_no(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(f"{i} ", end="")
            i+=1
        print("")

no = int(input("Enter the number: "))
pattern_no(no)