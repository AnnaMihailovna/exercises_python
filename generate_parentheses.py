def gen(length: int, open: int=0, closed: int=0, prefix: str='') -> None:
    if length * 2 == len(prefix):
        print(prefix)
    else:
        if open < length:
            gen(length, open+1, closed, prefix+'(')
        if closed < open:
            gen(length, open, closed+1, prefix+')')

def main() -> None:
    n = int(input())
    gen(n)

if __name__ == '__main__':
    main()
