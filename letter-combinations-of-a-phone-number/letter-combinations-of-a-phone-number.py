class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num=[0,0,2,3,4,5,6,7,8,9]
        letter_list =  [0,0,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        
        res = [""] if digits else []
        
        for digit in digits:
            letters = letter_list[int(digit)]
            temp = []
            for letter in letters:
                for item in res : 
                    temp.append(item + letter)
            res = temp
        
        return res