def max_len_substring(string):
    max_substring = ''
    count = 0

    for i in string:
        if i not in max_substring:
            max_substring += i
        else:
            if count < len(max_substring):
                count = len(max_substring)
            max_substring = max_substring[max_substring.index(i) + 1:] + i

    return count if count > len(max_substring) else len(max_substring)


if __name__ == '__main__':
    string = input()
    print(max_len_substring(string))
