def fib(n):
	'''Calculates the nth Fibonacci number. '''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

def fiblst(n):
	'''Calculates the first n Fibonacci numbers. O(n).'''
	if n == 0:
		return [0]
	elif n == 1:
		return [0, 1]
	else:
		pre = fiblst(n-1)
		curr = pre[len(pre)-1] + pre[len(pre)-2]
		return pre + [curr]

print fiblst(6)
