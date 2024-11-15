dic = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
output = 0

for i in dic.keys():
    while i in s:
        output += dic[i]
        s = s.replace(i, '', 1)
print(output)