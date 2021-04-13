def strStr(haystack, needle):
    if len(needle) < 1:
        print(0)
    else:
        print(haystack.find(needle))


haystack = "hello"
needle = "ll"
# Output: 2

strStr(haystack, needle)