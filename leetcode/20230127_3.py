#link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/886291332/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        answer = 0 
        min_value = sys.maxsize

        for price in prices : 
            min_value = min(min_value, price)
            answer = max(answer, price - min_value)

        if answer < 0 :
            return 0 
        return answer
