class Solution(object):
    def baseNeg2(self, no):
        ans = 0
        i = 0
        while no!=0:
            remainder = no % (-2)
            no = no // (-2)

            if remainder < 0:
                remainder += 2
                no += 1

            ans = (remainder*(10**i))+ans
            i+=1

        return str(ans)
        