class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curRow=[1]
        for i in range(1,rowIndex+1):    
            
            a,b = ([0]+curRow), (curRow+[0])
            
            curRow = [c+d for c,d in zip(a,b)]
         
        return curRow
        #print(newRow)
                