import random
player = int(input("我们出的拳是  石头[1],剪刀[2],布[3]："))
computer = random.randint(1, 3)
print("玩家出的%d，电脑出的%d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("电脑输了，哈哈哈~")
elif player == computer:
    print("平局，再战！")
else:
    print("太菜了，再练练吧！")
