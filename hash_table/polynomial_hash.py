def polinomial_hash(a, m, string):
    tmp = ord(string[-1])
    lenght = a
    for i in string[-2::-1]:
        tmp = (tmp + ord(i) * lenght)
        lenght = (lenght * a) % m
    print(tmp % m)


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    input_string = input()
    if input_string == '':
        print(0)
    else:
        polinomial_hash(a, m, input_string)
