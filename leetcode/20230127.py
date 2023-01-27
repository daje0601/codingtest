# link : https://leetcode.com/problems/array-partition/solutions/?q=python&orderBy=most_relevant

#solution1
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        result = []
        for i in range(0,len(nums),2):
            result.append(nums[i:i+2])
        
        answer = 0 
        for res in result :
            answer += min(res)
        
        return answer 
    
#solution2
class Solution(object):
    def arrayPairSum(self, nums):    
        return sum(sorted(nums)[::2])
