class Solution(object):
    def toHex(self, num):
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32  # Convert negative numbers to their 32-bit two's complement form
        
        hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        hex_no = ""
        
        while num > 0:
            remainder = num&15  # Equivalent to num % 16
            hex_no = hex_list[remainder] + hex_no  # Prepend the hexadecimal digit
            num = num>>4  # Equivalent to num // 16 using bitwise right shift
        
        return hex_no