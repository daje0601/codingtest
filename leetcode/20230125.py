height = [0,1,0,2,1,0,1,3,2,1,2,1]

solution1
def trap(height):
    stack = []
    volume = 0 
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break 
            
            distance = i - stack[-1] - 1 
            waters = min(height[i], height[stack[-1]]) - height[top]
            volume += waters * distance
        stack.append(i)
    return volume



#solution2
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_value = -1
        volume = 0 
        max_value_index = height.index(max(height))
        right = height[:max_value_index+1]
        left = height[max_value_index:]
        # 정방향 
        for i in range(len(right)):
            if right[i] < max_value:
                water = max_value - right[i]
                volume += water
                max_value = max(max_value, right[i])
            else: 
                max_value = right[i]

        # 역방향 
        r_max_value = -1
        r_volume = 0 
        for i in reversed(range(len(left))):
            if left[i] <= r_max_value:
                water = r_max_value - left[i]
                r_volume += water
                r_max_value = max(r_max_value, left[i])
            else: 
                r_max_value = left[i]

        return volume + r_volume


#solution3
def trap(height):
    for i in range(1, len(height)):
        answer = 0
        water = min(max(height[i:]), height[:i+1]) -height[i]
        answer += water 
    return answer 
