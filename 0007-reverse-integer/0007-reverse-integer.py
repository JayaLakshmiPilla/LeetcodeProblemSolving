class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        
        if int(x)>0 :
            rev_str= int(x[::-1])
            if rev_str < 2147483647 :
                return rev_str
            else :
                return 0 
            
        else :
            num=x[1:]
            num_1=num[::-1]
            
            num_2=int(x[0]+num_1)
            if num_2 >-2147483648 :
                return num_2
            else :
                return 0
            
            
            
