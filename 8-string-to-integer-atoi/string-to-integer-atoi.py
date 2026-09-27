class Solution(object):

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        i = 0
        n = len(s)

        # 1. Leading spaces ignore karo
        while i < n and s[i] == ' ':
            i += 1

        # 2. Sign check karo
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Digits read karo
        num = 0

        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # 4. Sign apply karo
        num = num * sign

        # 5. 32-bit integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX

        return num