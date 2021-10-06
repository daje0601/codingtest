# 문제 : 77. Combinations
# 링크 : https://leetcode.com/problems/combinations/submissions/
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
          
            return list(itertools.combinations(range(1, n+1), k))

        
        
# 문제 : 39. Combination Sum       
# 링크 : https://leetcode.com/problems/combination-sum/submissions/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        
        def dfs(csum, index, path):
            # 종료조건
            if csum < 0 :
                return 
            if csum == 0 :
                result.append(path)
                return 
            
            for i in range(index, len(candidates)):
                dfs(csum-candidates[i], i, path+[candidates[i]])
            
        
        dfs(target, 0, [])
        return result        
