t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N x M 배열을 받는다.
    arr = [list(map(str, input())) for _ in range(N)]   # 암호코드가 들어있는 배열 받기
    code_li = []

    for i in range(N) :                 # 반복문을 돌면서 16진수로 표현되어 있는 문자열을 2진수로 바꿔준다.
        for j in range(M) :
            if arr[i][j] != '0' :
                arr[i][j] = bin(int(arr[i][j], 16))

            # elif arr[i][j] == '0' and (0<=j-1<M and (arr[i][j-1] != '0')):
            #     arr[i][j] = bin(int(arr[i][j], 16))
            #
            # elif arr[i][j] == '0' and (0<=j+1<M and (arr[i][j+1] != '0')):
            #     arr[i][j] = bin(int(arr[i][j], 16))

    # print(arr)

    for i in range(N) :
        for j in range(M) :
            if arr[i][j] != '0' :
                code =''
                while 0<=i<N and 0<=j<M and arr[i][j] != '0' :
                    piece = arr[i][j][2:]
                    if len(piece) == 3 :
                        piece = '0' + piece
                    elif len(piece) == 2 :
                        piece = '00' + piece
                    elif len(piece) == 1 :
                        piece = '000' + piece
                    code += piece
                    arr[i][j] = '0'
                    j = j + 1

                # print(code)

                while code[len(code)-1] == '0' :
                    code = code[:(len(code)-1)]
                    # print('after : ', code)

                while code[0] == '0' :
                    code = code[1:]

                if len(code) % 56 != 0 :
                    plus = 56 - (len(code) % 56)
                    code = ('0' * plus) + code
                if code in code_li :
                    continue
                else :
                    code_li.append(code)


    print(code_li)


    # print(arr)