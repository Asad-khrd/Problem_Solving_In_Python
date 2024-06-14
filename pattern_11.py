# A B C 
# D E F 
# G H I 

def pattern(no):
    char = "A"
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(f"{char} ", end="")
            char = chr(ord(char)+1)
        print("")


no = int(input("Enter the number: "))
pattern(no)