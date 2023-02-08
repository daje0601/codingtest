# 문제 링크 : https://leetcode.com/problems/zigzag-conversion/description/
# 문제 이름 : 6. Zigzag Conversion

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        curRow, step = 0, 1
        answers = [''] * numRows
        
        for character in s:
            answers[curRow] += character 
            if curRow == numRows - 1: 
                step = -1 
            elif curRow == 0 :
                step = 1 
            curRow += step 

        return "".join(answers)
# 2차원으로 풀어야하는 것을 차원 압축하여 푸는 방법 
