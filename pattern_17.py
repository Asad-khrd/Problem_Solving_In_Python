# 111
#  22
#   3

def pattern(no):
    for i in range(1,no+1):
        print(" "*(i-1),end="")
        for j in range(no-(i-1),0,-1):
            print(f"{i}",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)
