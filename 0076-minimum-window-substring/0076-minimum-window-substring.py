from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)        # Count of characters in t
        window_count = {}
        required = len(t_count)     # Unique characters needed
        formed = 0                  # Unique characters with desired frequency in window

        l, r = 0, 0                 # Left and right pointers
        min_len = float("inf")
        min_window = (0, 0)

        while r < len(s):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                left_char = s[l]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1

            r += 1

        if min_len == float("inf"):
            return ""
        
        start, end = min_window
        return s[start:end + 1]
