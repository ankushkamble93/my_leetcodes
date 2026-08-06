class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        expected_set = set(range(1, n+1))
        for i in range(n):
            rows_set = set(matrix[i])
            cols_set = {matrix[r][i] for r in range(n)}
            if rows_set != expected_set or cols_set != expected_set:
                return False
        return True