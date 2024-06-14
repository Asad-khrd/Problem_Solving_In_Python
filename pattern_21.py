#   1
#  121
# 12321

def pattern(no):
    for i in range(1,no+1):
        print(" "*(no-i),end="")
        for j in range(1,i+1):
            print(f"{j}",end="")
        for k in range(i-1,0,-1):
            print(f"{k}",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)