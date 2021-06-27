def fib(n):
	result = []
	a = 0
	b = 1
	while b < n:
		result.append(b)
		a = b
		b = a + b
	return result
	
	

