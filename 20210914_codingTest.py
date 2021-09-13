# leetcode 561 Array Partition I

"""
문제가 이해하기 참 어려웠다. 
2n개로 이루어진 array nums를 n pairs를 만들고, 그 만든 각각의 pair에서 최소값을 구한 다음 
그 최소값들이 max가 되는 값을 찾으라는 문제이다. 

문제를 어렵게 써놓아서 그렇지 이해를 해보면 간단하다..

nums = [1,2,3,4]를 예를 들어보면 
앞에서부터 오름차순으로 인전 요소 페이러르 만들면 가장 큰 a1과 a2 페어들을 만들 수 있고 이 페어들의 합이 곧 만들 수 있는 최대합이 된다. 
문제의 Example1에 보면 자세한 설명이 나와 있다. 
"""

# 풀이1
def arrayPairs(nums):
  nums.sort()
  pair = []
  sum = 0 
  
  # nums를 반복하여 pair에 넣어주고 
  for i in nums:
    pair.append(i)
    
    # 페어는 항상 2개씩 묶이므로 len(pair)가 2라면 최소값을 구해서 sum에 더해준다. 
    if len(pair) == 2:
      sum = sum + min(pair)
      # 다시 새로운 값을 받기 위해 pair를 초기화해준다. 
      pair = []
  
  return sum 
  
  
# 풀이2
def arrayPairs(nums):
  nums.sort()
  pair = []
  sum = 0 
  
  # nums를 반복하여 pair에 넣어주고 
  for i, n in enumerate(nums):
    if i % 2 == 0 :
      sum += n
    
  return sum 


# 풀이3
def arrayPairs(nums):
  return sum(sorted(nums)[::2])
