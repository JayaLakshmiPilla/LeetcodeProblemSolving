class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=len(strs)
        list_a=[]
        string=""
        for i in range(l) :
            l_1=len(strs[i])
            list_a.append(l_1)
        list_a.sort()
        for i in range(list_a[0]) :
            let=strs[0][i]
            count=0 
            for j in range(l) :
                
                if let==strs[j][i] :
                    count=count+1
            if count==l :
                string+=let
            else :
                break
        return string
        




        