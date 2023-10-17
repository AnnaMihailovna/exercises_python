# 87254756
from typing import List, Tuple

def read_input() -> Tuple[int, List[int]]:
	# с табами непонятная ситуация, у меня
	# открывается нормально, в 4 пробела
	length = int(input())
	numbers_houses = [int(num) for num in input().strip().split()]
	return length, numbers_houses

def get_nearest_zero(length: int, numbers_houses: List[int]) -> List[int]:
	distance = [0] * len(numbers_houses)
	index_zero = None
	for i, value in enumerate(numbers_houses):
		if value == 0:
			index_zero = i
			continue
		if index_zero is not None:
			distance[i] = i - index_zero
		else:
			distance[i] = length
	index_zero = None
	for i, value in reversed(list(enumerate(numbers_houses))):
		if value == 0:
			index_zero = i
			continue
		if (index_zero != None and
            distance[i] > index_zero - i):
			distance[i] = index_zero - i
	return distance

def main() -> None:
	length, numbers_houses = read_input()
	print(*get_nearest_zero(length, numbers_houses), sep=' ')

if __name__ == '__main__':
	main()