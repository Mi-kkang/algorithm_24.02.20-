t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())        # N x N 배열의 길이 N
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 받기
    max_v = 0               # 사각형 넓이의 최대값을 저장할 변수 생성

    for i in range(N) :             # 배열을 다 돌아본다
        for j in range(N) :
            if arr[i][j] == 1 :     # 만약 사각 영역이라면, (가로 길이와 세로 길이를 재서 넓이를 구할 예정이다!)
                ni = i
                nj = j
                ni2 = i
                nj2 = j
                garo = 0
                sero = 0

                while 0<= ni < N and 0<= nj < N and arr[ni][nj] == 1 :      # 가로의 길이를 구한다.
                    garo += 1
                    ni = ni
                    nj = nj + 1

                while 0<= ni2 < N and 0<= nj2 < N and arr[ni2][nj2] == 1 :  # 세로의 길이를 구한다.
                    sero += 1
                    ni2 = ni2 + 1
                    nj2 = nj2

                area = garo * sero   # 구한 가로의 길이와 세로의 길이를 곱해 넓이를 구한다.

                if max_v < area :    # 기존의 저장되어 있는 최대 넓이보다 크면 새로 저장해준다.
                    max_v = area

    print(f'#{tc} {max_v}')