class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        s = s.lstrip()
        sign = 0
        if len(s)>=1 and s[0] == '-' :
            sign = '-'
            s = s.lstrip('0')
            s = s[1:]
        elif len(s)>=1 and s[0] == '+' :
            s = s[1:]
        for i in s :
            if i.isnumeric() :
                ans += i 
            else :
                break 
        
        if len(ans) == 0 :
            return 0 
        if sign == '-' :
            ans = sign+ans
        if int(ans) > -2**31 and int(ans) < 2**31-1 :
            return int(ans) 
        else :
            if sign == '-' :
                return -2147483648 
            else :
                return 2147483647

            
        