i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, j * i), end="\t")  #\t 在控制台输出一个制表符，协助在输出文本时，在垂直方向保持对齐
        j += 1
    print("")
    i += 1 