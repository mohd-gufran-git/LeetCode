class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m = len(s)
        n = len(p)

        # dp[i][j] = kya s ke first i characters
        # p ke first j characters se match karte hain?
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string aur empty pattern match
        dp[0][0] = True

        # Pattern jaise a*, a*b*, a*b*c* empty string ko match kar sakta hai
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # DP
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # Normal character ya '.'
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # '*'
                elif p[j - 1] == '*':
                    # '*' ko zero times use karo
                    dp[i][j] = dp[i][j - 2]

                    # '*' ko one/more times use karo
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]
        