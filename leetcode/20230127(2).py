#link : https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums):
        ans, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            ans[i] *= pre            
            pre *= nums[i]
            ans[-1-i] *= suf
            suf *= nums[-1-i]
        return ans
