class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total=0
        p=0
        for i in s[::-1]:
            c=roman[i]
            if c<p:
                total=total-c
            else:
                total=total+c
            p=c
        return total
