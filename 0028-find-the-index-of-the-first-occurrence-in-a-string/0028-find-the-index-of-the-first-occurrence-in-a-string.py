class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        l = len(needle)
        i = 0
        while (i <= n-l) :
            if(i+l <= n and haystack[i:i+l] == needle) :
                return i
            i += 1
        return -1