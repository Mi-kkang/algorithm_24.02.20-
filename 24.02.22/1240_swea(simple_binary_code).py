password = {'0001101' : 0,
            '0011001' : 1,
            '0010011' : 2,
            '0111101' : 3,
            '0100011' : 4,
            '0110001' : 5,
            '0101111' : 6,
            '0111011' : 7,
            '0110111' : 8,
            '0001011' : 9
            }

def find_end(N, M) :            # 뒤에서부터 1이 나오는 자리를 찾는 함수
    global end_i, end_j
    for i in range(N) :
        for j in range(M) :
            if arr[i][(M-1)-j] == 1 :
                end_i = i
                end_j = M-1-j
                return


t = int(input())                    # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # N x M 배열을 위한 N, M (가로가 M, 세로가 N)
    arr = [list(map(int, input())) for _ in range(N)]
    end_i = 0               # 암호의 끝자리가 위치한 배열의 행 숫자를 넣을 변수
    end_j = 0               # 암호의 끝자리가 위치한 배열의 열 숫자를 넣을 변수
    code = ''               # 56자리 암호 코드를 넣을 문자열
    bin_li = []             # 7자리 0과 1로 이루어진 암호를 넣을 리스트
    num_li = [''] * 9       # 암호를 해당 숫자로 바꾼 값을 저장할 리스트(편의를 위해 9칸을 만들었다)
    odd = 0                 # 인덱스 홀수번의 합을 저장할 변수
    even = 0                # 인덱스 짝수번의 합을 저장할 변수
    ans = 0                 # (홀수 자리의 합 x 3) + (짝수 자리의 합)

    find_end(N, M)              # 뒤에서부터 1이 나오는 것을 찾는다. 코드의 맨 뒷자리 1을 찾는 함수

    for j in range(end_j-55, end_j+1) :   # 찾았으면 56자리를 가져온다.
        code += str(arr[end_i][j])      # 하나씩 문자열에 저장해준다.(이때 행은 고정이다 / 변하지 않음)

    # print(code)
    # print(len(code))

    for i in range(8) :                 # 56자리 코드 문자열을 7자리씩 8개로 자르기 위한 반복문
        line = code[i*7:(i*7)+7]
        bin_li.append(line)             # 자른 코드 문자열을 리스트에 추가해준다.

    for k in range(8) :                     # 7자리 암호문을 숫자로 바꾸기 위한 반복문
        num_li[k+1] = password[bin_li[k]]   # 미리 저장해준 딕셔너리에서 변환값을 가져와서 숫자를 넣을 리스트에 해당 순서대로 넣어준다.

    for l in range(1, 9) :                  # 암호를 해독한 숫자를 하나씩 확인하자
        if l % 2 == 0 :                     # 숫자가 짝수번에 위치할 경우,
            even += num_li[l]
        else :                              # 숫자가 홀수번에 위치할 경우,
            odd += num_li[l]

    ans = (odd*3) + even                    # (홀수 자리의 합 x 3) + (짝수 자리의 합)

    if ans % 10 == 0 :                      # 구한 값이 10의 배수이면 모든 숫자의 합
        print(f'#{tc} {odd+even}')
    else :                                  # 10의 배수가 아니면 0 출력
        print(f'#{tc} 0')