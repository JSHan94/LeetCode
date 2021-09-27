class Solution:
    def longestPalindrome(self, st: str) -> str:
        
        new_st =[]
        for idx,i in enumerate(st):
            new_st.append(i)
            if idx != len(st)-1:
                new_st.append(0)
        pivot,s,e = 0,0,0
        max_res = []
        res = []
        while pivot < len(new_st):
            if not (0<=s<=pivot and pivot<=e<len(new_st)) or new_st[s]!= new_st[e]:
                if len(max_res) < len(res):
                    max_res = res
                res=[]
                pivot +=1
                s,e = pivot,pivot
            else:
                target = new_st[s]
                if s == pivot and target != 0:
                    res.append(target)
                elif target != 0 :
                    res.insert(0,target)
                    res.append(target)
                s-=1
                e+=1

        return "".join(max_res)