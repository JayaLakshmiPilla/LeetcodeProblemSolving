from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start: int, path: List[int]):
            result.append(path[:])  # Append a copy of the current subset
            for i in range(start, len(nums)):
                path.append(nums[i])         # Include nums[i]
                backtrack(i + 1, path)       # Recurse with next starting index
                path.pop()                   # Backtrack: remove last element

        backtrack(0, [])
        return result
