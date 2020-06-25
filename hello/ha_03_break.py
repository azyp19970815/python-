result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        if i == 50:
            break
        result += i
        print("i=%d  result=%d" % (i, result))
    i +=1
