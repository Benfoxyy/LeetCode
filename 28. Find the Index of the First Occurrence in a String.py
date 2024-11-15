haystack = "hello"
needle = "ll"

if needle in haystack:
    print(len(haystack.split(needle)[0]))
    
print(-1)