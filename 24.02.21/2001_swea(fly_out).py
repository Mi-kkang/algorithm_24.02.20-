t = int(input())                    # 테스트 케이스 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())        # 파리가 존재하는 배열 길이 N과 파리채 길이 M 받기
    arr = [list(map(int, input().split())) for _ in range(N)]       # 배열 받기
    max_v = 0               # 파리가 가장 많이 잡혔을 때를 저장하기 위한 변수 생성

    for i in range(N-M+1) :
        for j in range(N-M+1) :
            count = 0
            for k in range(i, i+M) :
                for l in range(j, j+M) :
                    count += arr[k][l]

            if max_v < count :
                max_v = count


    print(f'#{tc} {max_v}')