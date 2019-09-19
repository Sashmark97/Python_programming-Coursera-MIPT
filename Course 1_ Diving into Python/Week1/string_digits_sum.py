import sys
digit_string = sys.argv[1]
res = 0
for letter in digit_string:
    res += int(letter)
print(res)