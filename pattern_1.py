# 111
# 222
# 333

def print_stars(no):
    num = 0
    for i in range(no):
        num += 1
        for j in range(no):
            print(f"{num}", end="")
        print("")

no = int(input("Enter the number:"))
print_stars(no)