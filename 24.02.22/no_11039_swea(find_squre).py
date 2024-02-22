t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # N x N 배열의 길이 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    r_li = []
    c_li = []

    for i in range(N) :
        for j in range(N) :
            if arr[i][j] == 1 :
                r_li.append(i)
                c_li.append(j)

    r_len = len(r_li)
    c_len = len(c_li)

    print(r_li)
    print(c_li)

    garo = r_li[r_len-1] - r_li[0] + 1
    sero = c_li[c_len-1] - c_li[0] + 1

    area = garo * sero

    # print(f'#{tc} {area}')