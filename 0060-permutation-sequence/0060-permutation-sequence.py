from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert k to 0-based index
        result = []

        for i in range(n, 0, -1):
            f = factorial(i - 1)
            index = k // f
            result.append(numbers.pop(index))
            k %= f

        return ''.join(result)
