class Solution(object):
    def hasAlternatingBits(self, no):
        while no!=0:
            current_bit = no&1
            no = no>>1
            last_bit = current_bit
            if no!=0:
                current_bit = no&1
                if last_bit == current_bit:
                    return False
        else:
            return True
        