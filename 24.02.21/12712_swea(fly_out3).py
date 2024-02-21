t = int(input())                # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # 파리가 있는 배열의 길이 N, 파리채 배열 길이 M
    arr = [list(map(int, input().split())) for _ in range(N)] # 파리 배열 받기
    max_v = 0

    di = [0, 1, 0, -1]                      # 행열을 확인하기 위한 델타
    dj = [1, 0, -1, 0]

    di2 = [1, 1, -1, -1]                    # 대각선을 확인하기 위한 델타
    dj2 = [1, -1, 1, -1]

    for i in range(N) :
        for j in range(N) :
            cnt1 = 0                        # 행, 열의 파리를 잡은 수를 넣을 변수
            cnt2 = 0                        # 대각선의 파리를 잡은 수를 넣을 변수

            # for k in range(4) :
            #     for l in range(1, M) :
            for l in range(1, M) :
                for k in range(4) :
                    ni = i + di[k] * l
                    nj = j + dj[k] * l

                    nni = i + di2[k] * l
                    nnj = j + dj2[k] * l

                    if 0<= ni < N and 0<= nj < N :
                        cnt1 += arr[ni][nj]

                    if 0<= nni < N and 0<= nnj < N :
                        cnt2 += arr[nni][nnj]

            cnt1 += arr[i][j]
            cnt2 += arr[i][j]

            if max_v < cnt1 :
                max_v = cnt1
            if max_v < cnt2 :
                max_v = cnt2

    print(f'#{tc} {max_v}')