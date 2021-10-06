class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        
        def isValidBox(x,y):
            target = board[x][y]
            box_x = x-x%3
            box_y = y-y%3
            for i in range(box_x,box_x+3):
                for j in range(box_y,box_y+3):
                    if board[i][j] == target and (i!=x or j!=y):
                        print("Box error",i,j)
                        return False
            
            return True
        def isValidLine(x,y):
            target = board[x][y]
            for i in range(9):
                if target == board[x][i] and i != y:
                    print("Line x error",i)
                    return False
                if target == board[i][y] and i != x:
                    print("Line y error",i)
                    
                    return False
            return True
        

        for row in range(n):
            for col in range(n):
                if board[row][col] != "." :
                    if isValidBox(row,col) and isValidLine(row,col) :
                        pass
                    else:
                        return False
                
        return True