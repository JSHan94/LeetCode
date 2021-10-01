class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        n = len(height)
        s,e = 0,n-1
        maxA = (e-s) * min(height[s],height[e])
        while s < e:
            target = (e-s) * min(height[s],height[e])
            if target > maxA :
                maxA = target
            if height[s] < height[e]:
                s+=1
            else:
                e-=1
        return maxA