print("ТАБЛИЦА УМНОЖЕНИЯ".center(62))

for i in range(2):
    for j in range(2, 11):
        for k in range(2 + i * 4, 6 + i * 4):
            print(f'{k:2} * {j:2} = {j * k:2}', end='')
            if k == 5 or k == 9:
                if k == 5 and j == 10:
                    print('\n\n', end='')
                else:
                    print('\n', end='')
            else:
                print('\t', end='')