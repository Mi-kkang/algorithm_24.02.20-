# def find_point(i, j, k) :           # 2가 나오는 행렬의 행 i 열 j, 델타를 위한 k
#     global cnt
#     while 0<= i < N and 0<= j < N : # 배열 범위 안에 있을 때만 반복하기
#         ni = i + di[k]
#         nj = j + di[k]
#
#         if 0<= ni < N and 0<= nj < N :
#             cnt += arr[ni][nj]
#         i = ni
#         j = nj


t = int(input())                # 테스트 케이스의 개수 받기

for tc in range(1, t+1) :
    N = int(input())            # N x N 배열을 만들 N 받기
    arr = [list(map(int, input().split())) for _ in range(N)]       # 풍선 배열을 받는다.
    max_v = 0           # 최대 점수를 넣을 변수 생성

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    for i in range(N) :
        for j in range(N) :
            cnt = 0

            for k in range(N) :
                cnt += arr[i][k]

            for l in range(N) :
                cnt += arr[l][j]

            cnt -= arr[i][j]

            if max_v < cnt :
                max_v = cnt

            # for k in range(4) :
            #     find_point(i, j, k)

    print(f'#{tc} {max_v}')
