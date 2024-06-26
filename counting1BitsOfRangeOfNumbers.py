class Solution(object):
    def countBits(self, n):
        arr = [0]*(n+1) # Setting all values of array to zero
        for i in range(n+1):
            arr[i] = arr[i>>1]+(i&1) 
        return arr
        
        # Line 5 computes the no of 1 of each  i value
        # For exp: when i=2: arr[2]=arr[2//1] + 1(if i is odd, else not adding 1)