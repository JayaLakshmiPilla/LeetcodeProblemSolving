class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if not s or s[0] == '0':
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1  # base case: empty string
        dp[1] = 1  # base case: first char is valid since s[0] != '0'

        for i in range(2, n + 1):
            # One-digit decode (s[i-1])
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            # Two-digit decode (s[i-2:i])
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
