class Solution:
    def isValidSudoku(self, board: list[list[str]]):
        # create 9 sets for rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                num = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)  # unique index 0–8 for 3x3 boxes

                if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                    return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

        return True
