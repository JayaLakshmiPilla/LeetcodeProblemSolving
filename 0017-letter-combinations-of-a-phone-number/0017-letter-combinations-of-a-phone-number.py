class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digit_mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        ans = [] 
        def backtrack(idx,comb) :
            if idx == len(digits) :
                ans.append(comb[:])

                return 
            for letter in digit_mapping[digits[idx]] :
                backtrack(idx+1,comb+letter)




        ans = [] 
        backtrack(0,"")
        return ans

            

        