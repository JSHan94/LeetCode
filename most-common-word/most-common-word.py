class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        a = re.findall("[\w]+",paragraph.lower())
        cnt = defaultdict(int)
        for item in a:
            cnt[item]+=(1)
        max_cnt = 0 
        res = ""
        for k,v in cnt.items() :
            if max_cnt < v and k not in banned:
                max_cnt = v
                res = k
        print(cnt)
        return res
            