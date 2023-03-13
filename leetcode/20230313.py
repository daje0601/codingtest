class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right):
            if right >= left >= 0:
                if not right:
                    yield p
                for q in generate(p + '(', left-1, right): yield q
                for q in generate(p + ')', left, right-1): yield q
        return list(generate('', n, n))


class Solution:
    def generateParenthesis(self, n):
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left,right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):
        # open parentheses is right  
        # close parentheses is left  
        # 무조건 open으로 시작을 해야하기 때문 right의 수가 더 많아야한다. 
        # 즉, left가 더 많으면 끝나야한다는 것이다. 
        if right < left:
            return
        if not left and not right:
            ans.append(string)
            return
        if left:
            self.dfs(left-1, right, ans, string + "(")
        if right:
            self.dfs(left, right-1, ans, string + ")")
            
            
# 참고링크 : https://www.youtube.com/watch?v=s9fokUqJ76A
class Solution:
    def generateParenthesis(self, n : int) -> List[str]:
        stack = [] 
        res = [] 

        def backtrack(openN, closedN):
            if openN == closedN == n :
                res.append("".join(stack))
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN :
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res 
