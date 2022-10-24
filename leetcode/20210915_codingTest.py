
# solution1 
nums = [1,2,3,4]
def productExceptSelf(self, nums: List[int]) -> List[int]:

	# 정답을 입력할 빈 배열을 만듭니다. 
	ans = [1 for _ in nums]

	# 그리고 numpy를 사랑하기 때무네 numpy의 prob을 이용하여 자기 자신을 제외한
    # 왼쪽과, 오른쪽 곱을 변수에 담아줍니다. 
    # 그리고 그것을 곱해서 ans에 넣어준다는 생각을 하였는데요 
    # 시간복잡도에서 O(n)이 초과되서 되지 않았습니다. 
	for i in range(len(nums)):

		right = int(np.prod(nums[i+1:]))
		left = int(np.prod(nums[:i]))
		ans[i] = right * left 
        
	return ans


# solution2
def productExceptSelf(self, nums: List[int]) -> List[int]:

	# 일단 똑같이 빈 배열을 만들어 줍니다. 
	answer = []
    
	p = 1
    # 첫번째 요소가 들어가지 않도록 먼저 p를 넣어줍니다. 
	for i in range(len(nums)):
		answer.append(p)
        # 그리고 p에 다가 하나씩 곱을 해주면서 나아갑니다. 
		p = p * nums[i]

	p = 1
    # range(총길이, 어디까지, 몇칸씩 움직일까)를 나타내는 것입니다.
    # 즉, len(nums)-1 길이 만큼, 끝까지, 뒤로 한칸씩 움직여줘라는 의미입니다. 
	for i in range(len(nums)-1, -1, -1):
    	# 이미 answer[4]에 들어가 있는 값을 그대로 넣어야하기 때문에 이렇게 쓰고 
		answer[i] = answer[i] * p  
        # p에는 맨 끝 요소가 들어가야하기 때문에 아래와 같이 업데이터를 해주면 됩니다. 
		p = p * nums[i]

	return  answer

# solution3
def productExceptSelf(nums):
        res = [1] * len(nums)   # res => [1 , 1, 1, 1]
        prefix = 1 
        postfix = 1
    
        for i in range(len(nums)) :  # [1,1,2,6], 24
            res[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums) - 1 , - 1 , - 1) :  # [24,24,12,4]
            res[i] *= postfix
            postfix *= nums[i]
        return res
