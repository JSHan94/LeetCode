class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for idx, num in enumerate(nums):
            if len(dic[num]) > 0 and idx - dic[num][-1] <= k :
                return True
            dic[num].append(idx)
        return False