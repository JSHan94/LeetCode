# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r=1,n
        while l<=r :
            mid = l + (r-l)//2
            mid1 = isBadVersion(mid-1)
            mid2 = isBadVersion(mid)
            if not mid1 and mid2:
                return mid
            elif not mid2 :
                l=mid+1
            elif mid1:
                r=mid-1
        
        