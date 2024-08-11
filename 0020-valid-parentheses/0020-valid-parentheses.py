from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        Parentheses ={')':'(',']':'[','}':'{'}
        for i in s :
            if i in Parentheses.values() :
                stack.append(i)
            elif i in Parentheses.keys() :
                if not stack or Parentheses[i] != stack.pop() :
                    return False
            else :
                return False
        return len(stack)==0

        


        


            