from typing import List, Tuple

def binary_search_day(money: List[int], price: int, left: int, right: int) -> int:
    if price > money[-1]:
        return -1
    mid = (left + right) // 2
    if money[mid] >= price and (money[mid-1] < price or mid == 0):
        return mid+1
    elif money[mid] >= price:
        return binary_search_day(money, price, left, mid)
    elif money[mid] < price:
        return binary_search_day(money, price, mid+1, right)

def read_input() -> Tuple[List[int], int]:
    _ = int(input())
    money = [int(x) for x in input().strip().split()]
    price = int(input())
    return money, price

def main(money: List[int], price: int) -> None:
    day1 = binary_search_day(money, price, left=0, right=len(money))
    day2 = binary_search_day(money, price*2, left=0, right=len(money))
    print(day1, day2)

if __name__ == '__main__':
    main(*read_input())
