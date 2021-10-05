# 347. Top K Frequent Elements
# 링크 : https://leetcode.com/problems/top-k-frequent-elements/submissions/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

#         counter = {}
#         for num in nums:
#           if num not in counter:
#             counter[num] = 0
#           counter[num] += 1
        
#         items = sorted(counter.items(), key=lambda kv:kv[1], reverse=True)[:k]
        

#         answer = []
#         for i in items:
#           answer.append(i[0])
#         return answer
        from collections import Counter
       
        return  list(zip(*Counter(nums).most_common(k)))[0]




# 200. Number of Islands
# 링크 : https://leetcode.com/problems/number-of-islands/submissions/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
  
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
