def solution(n):
    def backtrack(row, queens, columns, diagonals1, diagonals2):
        if row == n:
            # If we have placed all queens, add the solution
            results.append(queens[:])
            return
        
        for col in range(n):
            # Check if placing a queen here is valid
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            
            # Place the queen
            queens.append(col)
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            
            # Move to the next row
            backtrack(row + 1, queens, columns, diagonals1, diagonals2)
            
            # Backtrack
            queens.pop()
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
    
    results = []
    backtrack(0, [], set(), set(), set())
    return results
