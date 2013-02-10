'''
knapsack with many uses
'''

W = 5
w = [1,1,1]
v = [2,3,5]
n = len(w)

T = [[0 for j in range(n)] for i in range(W)]

print T
	
for j in range(1, W):
	for i in range(0, n):
		if j >= w[i]:
			# Use the jth space to add an item
			T[j][i] = max( T[j-1][i] , T[j-w[i]][i] + v[i] )]
		else:
			# Don't use the extra space to add an item
			T[j][i] = T[j-1][i]
	print T

