class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_duplicates(array):
            seen = set()
            for element in array:
                # That means there are duplicates
                if element in seen and element != ".":
                    return True
                seen.add(element)
            return False
        
        # 1. Check condition 1 (rows)
        for row in board:
            if check_duplicates(row):
                return False

        # 2. Check condition 2 (columns)
        for idx in range(9):
            col = [row[idx] for row in board]
            if check_duplicates(col):
                return False

        # 3. Check condition 3 (grids)
        r,c = 0,0
        for _ in range(9):
            grid = [row[c:c+3] for row in board[r:r+3]]
            flattened_grid = [y for x in grid for y in x]
            
            if check_duplicates(flattened_grid):
                return False

            if (c + 3) < 8:
                c += 3
            else:
                r += 3
                c = 0

        return True