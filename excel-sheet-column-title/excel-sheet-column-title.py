class Solution:
    def convertToTitle(self, cN: int) -> str:
        res=""
        cN-=1
        while cN>=0:
            r = cN % 26 
            cN = cN // 26
            res += chr(ord('A')+r)
            cN -= 1
            
        return (res[::-1])