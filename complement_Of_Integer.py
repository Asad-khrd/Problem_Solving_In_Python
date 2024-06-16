class Solution(object):
    def bitwiseComplement(self, no):
        binary = 0
        i=0
        if no == 0:
            return 1
        else:     
            while no!=0:
                bit = no&1
                bit_rev = 1-bit
                binary = (bit_rev*(10**i))+binary
                no = no>>1
                i+=1
            ans = 0
            i=0
            while binary!=0:
                digit = binary%10
                ans = (digit*(2**i))+ans
                binary = binary//10
                i+=1
            return ans
        