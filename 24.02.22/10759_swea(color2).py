t = int(input())                # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    B = 10                              # 전체 영역 10 x 10
    arr = [[0]* B for _ in range(B)]    # 10 x 10 배열 만들기

    N = int(input())    # 칠할 영역의 개수

    for _ in range(N) :
        # 왼쪽 위 모서리 인덱스 r1, c1 / 오른쪽 아래 모서리 r2, c2 / 색상정보 color
        # +) color = 1(빨강), color = 2(파랑)
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1) :
            for j in range(c1, c2+1) :
                arr[i][j] += color

