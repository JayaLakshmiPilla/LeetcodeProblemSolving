class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start=0, path=[]):
            # If we have 4 parts and reached the end, it's a valid IP
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return
            
            # Try all splits of length 1 to 3
            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start+length]

                # Leading 0s are invalid unless part is '0'
                if len(part) > 1 and part[0] == '0':
                    continue

                if int(part) > 255:
                    continue

                backtrack(start + length, path + [part])

        backtrack()
        return res
