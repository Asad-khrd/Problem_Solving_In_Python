class Solution:
    def reverseBits(self, no):
        ans = 0
        bit_length = 32  # Assuming we are dealing with 32-bit unsigned integers
        
        for i in range(bit_length):
            ans = (ans << 1) | (no & 1)
            no = no >> 1
        
        return ans