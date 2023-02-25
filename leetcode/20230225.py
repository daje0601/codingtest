# 문제 : https://leetcode.com/problems/valid-parentheses/
# 괄호유형 맞추기 
# 풀이1
# pop의 개념을 그냥 그대로 적용해본 풀이방법 
# 다행히 runtimeError 없이 풀렸음 
class Solution:
    def isValid(self, s: str) -> bool:
        lst = [] 

        for val1 in list(s):
            if val1 in ["(", "[", "{"]:
                lst.append(val1)
            elif val1 in [")", "]", "}"]:
                try :
                    val2 = lst.pop()
                    if (val2 == "(") and (val1 != ")"):
                        return False
                    elif (val2 == "{") and (val1 != "}"):
                        return False
                    elif (val2 == "[") and (val1 != "]"):
                        return False
                except :
                    return False
                  
        if len(lst):
            return False
        return True
      
# 풀이2
class Solution:        
    def isValid(self, s: str) -> bool:
        map_dict = {")":"(", "]":"[", "}":"{"}
        stack = [] 
        input_list = list(s)
        # len이 1인 것들을 빠르게 걸러내기 위해서 
        if len(input_list) <= 1:
            return False 
          
        for val in input_list:
            if val in ["[", "{", "("]:
                stack.append(val)
            # for문을 돌고 있는데 stack에 아무것도 없다는 것은 순서가 안맞는 괄호가 먼저 왔다는 것이기 때문에 바로 False 
            # 심지어 stack에 있다고 하여도 쌍이 맞지 않는 경우의 수를 대비하여 두번째 조건을 달아두었습니다. 
            elif not len(stack) or map_dict[val] != stack.pop():
                return False
        
        # 그럼에도 불구 하고 (()같은 경우를 대비하여 len 길이로 한번더 체크를 합니다. 
        if len(stack):
            return False 
        return True 
      
# 풀이3 
class Solution:        
    def isValid(self, s: str) -> bool:
        map_dict = {")":"(", "]":"[", "}":"{"}
        stack = [] 
        
        for val in list(s):
            if val in ["[", "{", "("]:
                stack.append(val)
            
            elif not len(stack) or map_dict[val] != stack.pop():
                return False
        # (()같은 경우를 대비하여 len 길이로 한번더 체크하는 것을 이렇게 줄일 수 있습니다. 
        return len(stack) == 0 
