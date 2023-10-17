from typing import List, Optional


class OverFlowDeque(Exception):
    pass


class EmptyDeque(Exception):
    pass



class Deque:
	"""Класс двухсторонней очереди."""
	def __init__(self, max_length: int) -> None:
		self._deque: List[Optional[int]] = [None] * max_length
		self._max_length: int = max_length
		self._head: int = 0
		self._tail: int = -1
		self._size: int = 0
    
	def is_empty(self) -> bool:
		"""Возвращает True, если очередь пустая."""
		return self._size == 0
    
	def push_back(self, value: int) -> None:
		"""Добавляет элемент в конец очереди."""
		if self._size != self._max_length:
			self._tail = (self._tail + 1)%self._max_length
			self._deque[self._tail] = value
			self._size += 1
		else:
			raise OverFlowDeque
    
	def push_front(self, value: int) -> None:
		"""Добавляет элемент в начало очереди."""
		if self._size != self._max_length:
			self._head = (self._head - 1)%self._max_length
			self._deque[self._head] = value
			self._size += 1
		else:
			raise OverFlowDeque
    
	def pop_front(self) -> int:
		"""Удаляет крайний элемент с головы очереди
		и возвращает его.
		"""
		if self.is_empty():
			raise EmptyDeque
		else:
			value = self._deque[self._head]
			self._head = (self._head + 1)%self._max_length
			self._size -= 1
			return value
    
	def pop_back(self) -> int:
		"""Удаляет крайний элемент с хвоста очереди
		и возвращает его.
		"""
		if self.is_empty():
			raise EmptyDeque
		else:
			value = self._deque[self._tail]
			self._tail = (self._tail - 1)%self._max_length
			self._size -= 1
			return value


def main():
    """Основная логика программы."""
    n = int(input())
    max_length = int(input())
    deque = Deque(max_length)
    deque_methods = {
        'push_front': deque.push_front,
    	'push_back': deque.push_back,
        'pop_front': deque.pop_front,
    	'pop_back': deque.pop_back
	}
    for _ in range(n):
        try:
            command = input().split()
            if (len(command) == 1):
                function_call = deque_methods.get(command[0])()
                print(function_call)
            else:
                deque_methods.get(command[0])(int(command[1]))
        except Exception:
            print('error')
            # с помощью функции getattr сделала:
			# if(len(command)==1):
				# print(getattr(deque,command[0])())
			# else:
				# getattr(deque,command[0])(command[1])
		# except Exception:
			# print('error')

if __name__ == '__main__':
	main()
