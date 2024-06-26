class Solution(object):
    def isPowerOfTwo(self, no):
        if no==0:
            return False
        else: 
            while no!=1:
                remainder = no%2
                no = no//2
                if remainder!=0:
                    return False
            else:
                return True
        