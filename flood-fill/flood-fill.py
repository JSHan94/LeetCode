class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lr,lc = len(image), len(image[0])
        source_color = image[sr][sc]
        newImage=[[-1 for _ in range(lc)] for _ in range(lr)]
        def isConnected(r,c):
            if 0<=r<lr and 0<=c<lc and image[r][c] == source_color and newImage[r][c] == -1:
                    return True
            return False
        
        dx,dy = [1,-1,0,0], [0,0,1,-1]
        bfs =[(sr,sc)]
        newImage[sr][sc] = newColor
        while bfs:
            cur_r,cur_c = bfs.pop(0)
            for x,y in zip(dx,dy):
                new_r, new_c = cur_r+y, cur_c + x
                if isConnected(new_r,new_c):
                    newImage[new_r][new_c] = newColor
                    bfs.append((new_r,new_c))
                    
        for r in range(lr):
            for c in range(lc):
                if newImage[r][c] == -1:
                    newImage[r][c] = image[r][c]
                    
        return newImage
                    