s = "["
dic = {')':'(',']':'[','}':'{'}
for i in range(int(len(s)/2)):
    if s[int(len(s)/2-i-1)] == dic.get(s[int(len(s)/2+i)]) and len(s) > 1:
        print(True)
    else:
        print(False)
        break


# print(len(s))