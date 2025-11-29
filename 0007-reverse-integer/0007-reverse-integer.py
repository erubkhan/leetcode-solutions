class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reverse = ""
        neg = False
        for digit in reversed(str(x)):
            if digit != "-":
                reverse = reverse + digit
            else: 
                neg = True
        
        if int(reverse) < -2**31 or int(reverse) > 2**31 - 1:
            return 0
        if (neg):
            return -int(reverse)
        return int(reverse)