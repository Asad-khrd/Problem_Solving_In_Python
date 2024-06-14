# A B C 
# A B C 
# A B C 

def pattern(no):
    for i in range(1,no+1):
        char = "A"
        for j in range(1,no+1):
            print(f"{char} ", end="")
            char = chr(ord(char)+1)
        print("")


no = int(input("Enter the number: "))
pattern(no)