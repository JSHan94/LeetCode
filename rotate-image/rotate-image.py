class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #transpose -> reverse = transpose
        n=len(a)
        for i in range(n):
            for j in range(i,n):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        
        for i in range(n):
            a[i] = a[i][::-1]
            
        