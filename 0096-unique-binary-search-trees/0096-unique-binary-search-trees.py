class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] will store the number of unique BSTs with i nodes
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # empty tree
        dp[1] = 1  # single node
        
        # Calculate dp values for 2 to n
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = dp[root - 1]      # number of unique BSTs in left subtree
                right = dp[nodes - root] # number of unique BSTs in right subtree
                total += left * right
            dp[nodes] = total
        
        return dp[n]
