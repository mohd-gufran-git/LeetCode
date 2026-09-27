class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = -1 if x < 0 else 1

        x = abs(x)

        rev = int(str(x)[::-1])

        rev = rev * sign

        # 32-bit signed integer range
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev