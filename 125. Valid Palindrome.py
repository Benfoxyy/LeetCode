s = "1a2"
xs = ""
for char in s:
    if char.isalpha() or char.isdigit():
        xs += char
if xs.lower() == xs.lower()[::-1]:
    print(True)
print(False)