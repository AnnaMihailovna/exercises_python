def fibonacci(n, k):
	a, b = 1, 1
	if n <= 1:
		return 1
	else:
		for _ in range(n-1):
			a, b = b, (b+a)%10**k
		return b

def main():
	n, k = map(int, input().split())
	result = fibonacci(n, k)
	print(result)

if __name__ == '__main__':
	main()
