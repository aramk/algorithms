W = 10
w = [1,1,1]
v = [2,3,5]
n = len(w)

T = [[0 for j in range(W)] for i in range(n)]

print T

for i in range(1, n): # Start at 1, i-1 becomes 0
	for j in range(0, W):
		if j >= w[i]:
			T[i][j] = max( T[i-1][j] , T[i-1][j-w[i]] + v[i] )
		else:
			T[i][j] = T[i-1][j]

print T














# for i in T:
# 	for w in range(W):
# 		if i <= w and w > 0:
# 			K[i][tw] = max( K[w-1][tw], K[w-1][w - tw] + tv )
# print K

