# A 
# B C 
# C D E 

def pattern(no):
    for i in range(1,no+1):
        char = "A"
        char = chr(ord(char)+i-1)
        for j in range(1,i+1):
            print(f"{char} ", end="")
            char = chr(ord(char)+1)
        print("")


no = int(input("Enter the number: "))
pattern(no)