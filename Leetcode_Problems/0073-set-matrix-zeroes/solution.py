class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = set()
        # cols = set()
        r = len(matrix)
        c = len(matrix[0])
        # i, j = 0, 0

        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        # for i in range(r):
        #     for j in range(c):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0

        is_col = False
        for i in range(r):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, r):
            for j in range(1, c):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(c):
                matrix[0][j] = 0

        if is_col:
            for i in range(r):
                matrix[i][0] = 0

