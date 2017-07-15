def longest_palindromic_substring(s):
    inverse = s[::-1]
    length = len(s)
    values = [[0 for x in range(length)] for y in range(length)]
    max_length = max_end = 0
    for i in range(length):
        for j in range(length):
            if s[i] == inverse[j]:
                cur_length = values[i][j] = values[i - 1][j - 1] + 1 if i > 0 and j > 0 else 1
                if cur_length >= max_length and length - 1 - j == i - cur_length + 1:
                    max_length = cur_length
                    max_end = i
    return s[max_end-max_length+1:max_end+1]

print(longest_palindromic_substring('babad'))
