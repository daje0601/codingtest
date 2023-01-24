# link : https://leetcode.com/problems/diagonal-traverse/submissions/882747717/

#solution1
class Solution(object):
    def findDiagonalOrder(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        return [matrix[i][d-i]
                for d in range(m+n-1)
                for i in range(max(0, d-n+1), min(d+1, m))[::d%2*2-1]]

#solution2
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagonal_order = []
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = 0
        while len(diagonal_order) < n * m:
            while i >= 0 and j < m:  # we go upwards
                diagonal_order.append(matrix[i][j])
                i -= 1
                j += 1
            if j == m:
                i += 2
                j = m - 1
            else:
                i = 0
            while i < n and j >= 0:  # we go downwards
                diagonal_order.append(matrix[i][j])
                i += 1
                j -= 1
            if i == n:
                j += 2
                i = n - 1
            else:
                j = 0
        return diagonal_order
