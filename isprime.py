# def isPrime(no):
#         if no==0 or no==1:
#             return False
#         elif no==2:
#             return True
#         elif no>2:
#             for i in range(2,no):
#                 if no%i==0:
#                     return False
#                     break
#             return True
    

# print(isPrime(8))

def countPrimeSetBits(left, right):
    count_prime = 0
    for i in range(left,right+1):
        count = 0
        while i!=0:
            if i&1:
                count+=1
            i>>=1
        if count==0 or count==1:
            count_prime +=0
        elif count==2:
            count_prime+=1
        elif count>2:
            for j in range(2,count):
                if count%j==0:
                    count_prime+=0
                    break
            else:
                count_prime+=1
    return count_prime    
  
print(countPrimeSetBits(10,15))




