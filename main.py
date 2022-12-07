import random
print('[1][2][3]\n[4][5][6]\n[7][8][9]\nВведите кооринат удара (от 1-9): ')
res = []
fin = False
count = 0
while fin == False:
    for num in range(3):
        res.append(list())
        for num_sec in range(3):
            res[num].append(0)
    res[random.randint(0, 2)][random.randint(0, 2)] = 1
    finish = int(input())
    list1 = {1: res[0][0], 2: res[0][1], 3: res[0][2], 4: res[1][0], 5: res[1][1], 6: res[1][2], 7: res[2][0], 8: res[2][1], 9: res[2][2]}
    if list1[finish] == 1:
        print('Корабль уничтожен!')
        print(f'{count} попыток использованно')
        fin = True
    else:
        print('Вы промахнулись, попробуйте еще раз')
        count += 1

