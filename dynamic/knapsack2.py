'''
knapsack with only one use each
'''

W = 5
w = [1,1,1]
v = [2,3,5]
n = len(w)

T = [[0 for j in range(n)] for i in range(W)]

print T
	
for j in range(0, W):
	for i in range(1, n): # Start at 1, i-1 becomes 0
		if j >= w[i]:
			T[j][i] = max( T[j][i-1] , T[j-w[i]][i-1] + v[i] )
		else:
			T[j][i] = T[j][i-1]
	print T

