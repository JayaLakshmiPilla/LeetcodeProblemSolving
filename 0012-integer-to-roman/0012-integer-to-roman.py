class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1 : 'I',5 : 'V',10 : 'X',50:'L',100 : 'C',500 : 'D',1000 : 'M'}
        RomanNum = ""
        number = num
        i = 0
        while(num>0) :
            number = num%10  
            if i == 0 :
                if number<=3 :
                    RomanNum = 'I'*number +RomanNum 
                elif number>=5 and number <= 8 :
                    RomanNum = 'V'+'I'*(number-5) + RomanNum 
                elif number == 4 :
                    RomanNum = 'IV' +RomanNum 
                elif number == 9 :
                    RomanNum = 'IX' +RomanNum 
            elif i == 1 :
                if number<=3 :
                    RomanNum = 'X'*number +RomanNum 
                if number>=5 and number <= 8 :
                    RomanNum = 'L'+'X'*(number-5) + RomanNum 
                elif number == 4 :
                    RomanNum = 'XL' +RomanNum 
                elif number == 9 :
                    RomanNum = 'XC' +RomanNum 
            elif i == 2 :
                if number<=3 :
                    RomanNum = 'C'*number +RomanNum 
                if number>=5 and number <= 8 :
                    RomanNum = 'D'+'C'*(number-5) + RomanNum 
                elif number == 4 :
                    RomanNum = 'CD' +RomanNum 
                elif number == 9 :
                    RomanNum = 'CM' +RomanNum 
            elif i == 3 :
                if number <=3 :
                    RomanNum = 'M'*number +RomanNum 
            num = num//10
            i = i+1
        return RomanNum




        