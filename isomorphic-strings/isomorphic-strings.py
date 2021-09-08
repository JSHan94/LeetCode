class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a=[]
        
        for i,j in zip(s,t):
            if (i,j) in a :
                continue
            for item in a :
                if i in item[0] or j in item[1]:
                    return False
            a.append((i,j))
        
        return True