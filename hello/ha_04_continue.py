result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        if (i == 96) or (i == 98):
            i +=1     #防止陷入死循环
            continue
        result += i
        print("i=%d  result=%d" % (i, result))
    i +=1