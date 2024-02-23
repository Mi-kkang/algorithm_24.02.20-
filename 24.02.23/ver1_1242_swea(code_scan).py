t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N x M 배열을 받는다.
    arr = [list(map(str, input())) for _ in range(N)]   # 암호코드가 들어있는 배열 받기
    code_li = []

    for i in range(N) :
        for j in range(M) :
            if arr[i][j] != '0' :
                code = ''
                while 0<=i<N and 0<=j<M and arr[i][j] != '0' :
                    code += arr[i][j]
                    j  = j + 1
                if code not in code_li :
                    code_li.append(code)

    print(code_li)