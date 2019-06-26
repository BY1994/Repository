"""
17294 귀여운 수

2019.06.25 PBY 최초작성
"""

k = input()

flag = 1
if len(k) > 1:
    step = int(k[1])-int(k[0])
    for i in range(len(k)-1):
        if int(k[i+1])-int(k[i]) != step:
            flag = 0
            break

if flag == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
