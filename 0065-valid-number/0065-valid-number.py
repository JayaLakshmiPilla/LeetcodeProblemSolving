class Solution:
    def isNumber(self, s: str) -> bool:
        def isInteger(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            return s.isdigit()

        def isDecimal(s):
            if not s:
                return False
            if s[0] in ['+', '-']:
                s = s[1:]
            if '.' not in s:
                return False
            integer_part, dot, fractional_part = s.partition('.')
            if not integer_part and not fractional_part:
                return False
            if integer_part and not integer_part.isdigit():
                return False
            if fractional_part and not fractional_part.isdigit():
                return False
            return True

        # Split on 'e' or 'E'
        if 'e' in s or 'E' in s:
            base, _, exp = s.lower().partition('e')
            return (isInteger(base) or isDecimal(base)) and isInteger(exp)
        else:
            return isInteger(s) or isDecimal(s)
