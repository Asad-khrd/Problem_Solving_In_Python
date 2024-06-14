#   1
#  23
# 456

def pattern(no):
    val = 1
    for i in range(1,no+1):
        print(" "*(no-i),end="")
        for j in range(1,i+1):
            print(f"{val}",end="")
            val+=1
        print("")

no = int(input("Enter the number: "))
pattern(no)
