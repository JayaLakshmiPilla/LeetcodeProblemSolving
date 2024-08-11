class Solution(object):
    def romanToInt(self, s):
        symbol = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0 
        l = len(s)
        for i in range(l) :
            if i<l-1 and symbol[s[i]] < symbol[s[i+1]]  :
                    num -= symbol[s[i]]
            else :
                num += symbol[s[i]]
        return num

        