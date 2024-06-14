#   *
#  **
# ***

def pattern(no):
    for i in range(1,no+1):
        print(" "*(no-i),end="")
        for j in range(1,i+1):
            print("*",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)
