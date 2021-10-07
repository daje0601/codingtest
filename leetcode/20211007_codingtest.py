# 78. Subsets
# 링크 : https://leetcode.com/problems/subsets/submissions/
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for n in nums:
            for i in range(len(res)): # range-1까지 i 값이 들어간다는것 
                res.append(res[i]+[n]) # []+[1] = [1]
        return res

      
# 332. Reconstruct Itinerary
# 링크 : https://leetcode.com/problems/reconstruct-itinerary/
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]
