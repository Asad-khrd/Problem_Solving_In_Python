# Enter the number: 5
#     1    
#    121   
#   12321  
#  1234321 
# 123454321
#  1234321 
#   12321  
#    121   
#     1

def pattern(no):
    for i in range(1,no+1):
        print(" "*(no-i),end="")
        for j in range(1,i+1):
            print(f"{j}", end="")
        for k in range(i-1,0,-1):
            print(f"{k}", end="")
        print("")
    for l in range(1,no):
        print(" "*l,end="")
        for m in range(1,no+1-l):
            print(f"{m}", end="")
        for n in range(no-1-l,0,-1):
            print(f"{n}",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)