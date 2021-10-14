# 787. Cheapest Flights Within K Stops
# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 노드가 k번째로 방문했는지 여부를 판단하기 위한 dist
        dist = []
        for _ in range(K + 2):
            dist.append(collections.defaultdict(int))
            
        # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
        Q = [(0, src, K)]

        # 우선 순위 큐 최소값 기준으로 도착점까지 최소 비용 판별
        while Q:
            price, node, k = heapq.heappop(Q)
            dist[k + 1][node] = price
            if node == dst:
                return price
            if k >= 0:
                    for v, w in graph[node]:
                        # v가 k번째로 방문한 적이 있는지 확인
                        if v not in dist[k]:
                            alt = price + w
                            heapq.heappush(Q, (alt, v, k - 1))
        return -1
    




# 104. Maximum Depth of Binary Tree
# 링크 : https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = self.maxDepth(root.left), self.maxDepth(root.right)
 
        return 1 + max(left, right)
