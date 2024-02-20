arr = [[0]*100 for _ in range(100)]     # 큰 면적을 넣는다.
count = 0
for n in range(4) :
    st_x, st_y, en_x, en_y = map(int, input().split())      # 4개의 수를 받는다.

    # print(f'시작점 ({st_x}, {st_y}), 종점 ({en_x}, {en_y})')

    for i in range(st_x, en_x) :            # 시작점부터 끝점까지의 면적을 칠해보자
        for j in range(st_y, en_y) :
            arr[i][j] = 1

# print(arr)

for k in range(100) :                       # 칠해진 부분을 확인해서 면적을 잰다.
    for l in range(100) :
        if arr[k][l] == 1 :
            count += 1

print(count)