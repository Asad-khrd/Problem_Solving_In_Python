# A A A 
# B B B 
# C C C 

def pattern(no):
    char = "A"
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(f"{char} ", end="")
        print("")
        char = chr(ord(char)+1)


no = int(input("Enter the number: "))
pattern(no)