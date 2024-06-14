class Solution(object):
    def subtractProductAndSum(self, no):
        prod = 1
        sum = 0
        while no>0:
            prod*=(no%10)
            sum+=(no%10)
            no = no//10

        return (prod-sum)