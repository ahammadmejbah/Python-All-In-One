def longest_substr(s):
    count = 0
    maxcount = 0
    result = 0
    for char in range(len(s) - 1):
        if (s[char] <= s[char + 1]):
            count += 1
            if count > maxcount:
                maxcount = count
                result = char + 1
        else:
            count = 0
    startposition = result - maxcount
    return startposition, result


# parent string
s = 'azbeggaklbeggh'

# longest substring indexes
start, end = longest_substr(s)

print('Longest substring in alphabetical order is:',
      s[start:end + 1])
