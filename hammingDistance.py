class Solution(object):
    def hammingDistance(self, x, y):
        XORd_bits = x^y
        count = 0
        while XORd_bits !=0:
            if XORd_bits&1:
                count+=1
            XORd_bits = XORd_bits >> 1
        return count
        