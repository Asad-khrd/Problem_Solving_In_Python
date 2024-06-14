# This code calculates the number of '1' bits in binary representation of input number

class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n!=0:
            if n&1:
                count+=1
            n = n>>1
        return count