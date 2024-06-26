class Solution(object):
    def divide(self, dividend, divisor):
        quotient = 0
        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)
        while dividend_abs>=divisor_abs:
            multiple = 1
            current_divisor = divisor_abs
            while dividend_abs >= (current_divisor << 1):
                current_divisor <<= 1
                multiple <<= 1
            dividend_abs -= current_divisor
            quotient += multiple
        if dividend * divisor < 0:
            quotient = -quotient
        if quotient > (2**31) - 1:
            return (2**31) - 1
        elif quotient < -2**31:
            return -2**31
        return quotient