# 17. Letter Combinations of a Phone Number
# 링크 : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        
        char_map = { '2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno',
                     '7': 'pqrs','8': 'tuv','9': 'wxyz',}

        chars = []
        for digit in digits:
            chars.append([*(char_map[digit])])

        l = list(itertools.product(*chars))

        answer = []
        for i in l :
            answer.append("".join(i))
        
        return answer
      
      
      
# 46. Permutations
# 링크 : https://leetcode.com/problems/permutations/submissions/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        nPr = itertools.permutations(nums, len(nums))
        
        return nPr
