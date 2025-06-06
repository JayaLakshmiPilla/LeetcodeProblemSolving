from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)  # Memoize to avoid redundant work
        def helper(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):  # Quick check to eliminate impossible cases
                return False

            n = len(a)
            for i in range(1, n):
                # Check if no swap
                if helper(a[:i], b[:i]) and helper(a[i:], b[i:]):
                    return True
                # Check if swapped
                if helper(a[:i], b[-i:]) and helper(a[i:], b[:-i]):
                    return True

            return False

        return helper(s1, s2)
