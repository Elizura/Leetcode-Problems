#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		distance = [float('inf')] * n
		distance[0] = 0
		def bellman_ford():
		    for src, des, cost in edges:
		        if distance[src] + cost < distance[des]:
		            distance[des] = distance[src] + cost
		for i in range(n - 1):
		    bellman_ford()
		ans = distance.copy()
		bellman_ford()
		temp = distance.copy()
		
		for i in range(len(ans)):
		    if ans[i] != temp[i]: return 1
		return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

# } Driver Code Ends