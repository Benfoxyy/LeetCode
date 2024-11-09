dic = {}
strs = [""]
for i in strs:
    for idx,j in enumerate(i):
        dic[i[:idx+1]] = dic.get(i[:idx+1],0) + 1

if len(dic) and max(dic.values()) > 1 and len(strs) == max(dic.values()):
    print(max(dic, key=lambda k: (dic[k],len(k))))
elif len(dic) == 1 and len(strs) == 1:
    print(max(dic, key=dic.get))
else:
    print('')