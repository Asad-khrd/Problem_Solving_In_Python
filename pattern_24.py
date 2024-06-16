# Enter the number: 7
#    *   
#   * *  
#  *   * 
# *     *
#  *   * 
#   * *  
#    * 

def pattern(no):
    for i in range(1,((no+1)//2)+1):
        print(" "*((no//2)-(i-1)),end="")
        for j in range(1):
            print("*",end="")
        print(" "*(i-1),end="")
        for k in range(i-2,0,-1):
            print(" ",end="")
        if i>1 and i<((no+1)//2)+1:
            for l in range(1):
                print("*",end="")
        print("")
    for p in range(1,((no+1)//2)):
        print(" "*p,end="")
        for q in range(1):
            print("*",end="")
        print(" "*(((no+1)//2)-1-p),end="")
        print(" "*(((no+1)//2)-2-p),end="")
        if p>0 and p<(((no+1)//2)-1):
            print("*",end="")
        print("")

no = int(input("Enter the number: "))
pattern(no)
