# 771. Jewels and Stones
# 링크 : https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = list(jewels)
        
        jewel_count = 0 
        for i in jewels:
            j = stones.count(i)
            jewel_count += j 
        
        return jewel_count
               
---

# 3. Longest Substring Without Repeating Characters
# 링크 : https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 사용된 단어인지 아닌지를 dict로 파악을 하고자 합니다. 
        # 앞에서 사용한 단어가 뒤에서 나오게 된다면 value 값을 업데이트 하게 됩니다. 
        used = {}
        
        start = max_length = 0 
        for index, char in enumerate(s):
            if char in used and start <= used[char]  :
                # 시작이 0부터 였으니, 1을 더해줘서 그 다음으로 넘어가게 합니다. 
                start = used[char] + 1
            else:
                max_length = max(max_length, index - start + 1)
        
            used[char] = index 
        
        return max_length 
    
   
