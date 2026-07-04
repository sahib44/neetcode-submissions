class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowdupes = [[0]*9 for _ in range(9)]
        coldupes = [[0]*9 for _ in range(9)]
        boxdupes = [[0] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                element = board[r][c]
        
                if element == ".":
                    continue
            
                val = int(element) - 1
                boxi = (r//3)*3+(c//3)

                if rowdupes[r][val] == 1 or coldupes[c][val] == 1 or boxdupes[boxi][val] == 1:
                    return False
                
                boxdupes[boxi][val] = 1
                rowdupes[r][val] = 1
                coldupes[c][val] = 1
        
        return True