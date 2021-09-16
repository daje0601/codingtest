from scipy.special import comb


def threeSum(nums):
    answer = []
    nums.sort()

    # 두번째, 세번째 숫자가 와야하므로 -2를 해줌 
    for i in range(len(nums)-2):

        # i가 1 일 때 0번째와 같다면 넘어갈 수 있도록 예외처리를 해줌
        # 나는 참 아이러니한게 i가 2일 때 0이랑 같은지는 확인을 못하는데 괜찮은 건가?
        # 왜 바로 전에 숫자와만 비교를 해서 안같다면 괜찮은거지? 정렬을 했기 때문이다! 
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # i를 기준으로 left와 right를 구하고 그 친구들을 쭉쭉 더해오는 식으로 코드를 구상해보았다. 
        # 처음에는 순열조합을 만들어서 적용을 해보았으나, 시간복잡도가 너무 높아져서 코드가 통과가 되지 않았다. 
        left, right = i+1, len(nums)-1

        # 당연히 left가 right를 넘어갈 수 있으므로 그 전까지만 반복해서 코드가 작동될 수 있도록 한다.  
        while left < right :
            sum = nums[i]+nums[left]+nums[right]
            
            # 정렬을 해 놓았기 때문에 sum이 0보다 작으면 left를 한칸 앞으로 이동하고 
            if sum < 0 :
                left += 1
            # 0보다 크면 뒤로 한칸 이동하게 한다. 
            elif sum > 0 :
                right -= 1
            # 0일때는 answer에 넣어주고, left와 right를 동시에 움직이게 한다. 
            # 단, 중복된 값이 있을 수 있으므로 left와 right에 예외처리를 해줘야 한다. 
            else:
                answer.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
                
    return answer
