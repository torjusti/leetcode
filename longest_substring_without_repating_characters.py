def lengthOfLongestSubstring(s):
    cur_length = max_length = 0
    indexes = {}
    for i in range(len(s)):
        if s[i] in indexes and indexes[s[i]] >= (i - cur_length):
            cur_length = i - indexes[s[i]]
        else:
            cur_length += 1
        indexes[s[i]] = i
        max_length = max(max_length, cur_length)
    return max_length
