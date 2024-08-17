class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        carry = 1
        for i in range(l-1,-1,-1) :
            sum = carry + digits[i]
            digits[i] = sum%10 
            carry = sum//10                                                                                                                                                                                                                                  
        if carry == 1 :
            result = [1] + digits 
            return result 
        return digits

        