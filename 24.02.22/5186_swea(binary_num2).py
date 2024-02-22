t = int(input())                # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = float(input())          # 0보다 크고 1미만인 십진수 N
    ans = ''                    # 소수점 이진수를 저장할 변수 생성
    count = -1                  # 소수점 이진수의 제곱수 설정 (초기값 -1이다)

    while N :                       # N이 0 이상일 때만 반복한다.
        num = 1 * (2 ** count)      # 소수점 이진수를 했을 때 값을 저장한다.

        if len(str(num)) <= 14 :    # 총 길이가 14이내일때, (str로 바꾸면 앞에 0과 .도 숫자에 포함되어서 14자리다)
            if N >= num :           # 만약 저장한 값이 N보다 작거나 같으면
                ans += '1'          # 유효한 값이니 1을 더해서 저장해준다.
                N -= num            # N에서 num을 빼준다.
                count -= 1          # 제곱수 자리는 하나 뒤로 가준다.
            else :                  # 저장한 값이 N보다 크면
                ans += '0'          # 사용할 수 없으니 0을 더해서 저장해준다.
                count -= 1          # 제곱수 자리는 하나 뒤로 가준다.

        else :                      # 소수점 아래가 13 이상이 되면
            ans = 'overflow'        # overflow를 저장하고 반복문 탈출!
            break

    print(f'#{tc} {ans}')