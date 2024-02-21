t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N x M 의 배열을 만들기 위한 숫자 받기
    arr = [list(map(int, input().split())) for _ in range(N)]   # 풍선 배열 받기
    max_v = 0       # 종이 꽃가루가 최대로 나오는 경우를 저장할 변수 저장

    di = [0, 1, 0, -1]      # 델타를 사용할 예정이다.
    dj = [1, 0, -1, 0]

    for i in range(N) :     # 배열의 크기만큼 반복한다.
        for j in range(M) :
            cnt = 0
            num = arr[i][j] # 배열에 저장되어 있는 꽃가루의 개수를 센다
            cnt += num

            for k in range(4) :             # 상하좌우를 확인 할 예정인데,
                for l in range(1, num+1) :  # 꽃가루의 개수만큼 확인하자!
                    dni = i + di[k] * l
                    dnj = j + dj[k] * l

                    if 0<= dni < N and 0<= dnj < M :    # 풍선을 확인해볼 자리가 배열 안에 있으면
                        cnt += arr[dni][dnj]            # 추가해준다.

            if max_v <= cnt :       # 종이 꽃가루가 제일 많이 날리는 상황과 비교해서
                max_v = cnt         # 더 크면 재할당 해준다.

    print(f'#{tc} {max_v}')