class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected_set = set(range(1,n+1))
        for i in range(n):
            row_set = set(matrix[i])
            col_set = {matrix[r][i] for r in range(n)}
            if row_set != expected_set or col_set != expected_set:
                return False
        return True
