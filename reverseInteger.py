class Solution(object):
    def reverse(self, no):
        no_abs = abs(no)
        ans = 0
        while no_abs!=0:
            digit = no_abs%10
            ans = (ans*10)+digit
            no_abs = no_abs//10
        if no<0:
            ans = ans*(-1)
        if ans <= (-2**(31)) or ans >= ((2**(31))-1):
            return 0
        else:
            return ans 