def fibonacci(n):
	if n in(1, 2):
		return 1
	return fibonacci(n-1) + fibonacci(n-2)

def main():
	n = int(input()) + 1
	result = fibonacci(n)
	print(result)

if __name__ == '__main__':
	main()
