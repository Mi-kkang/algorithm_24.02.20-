t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    code = input()
    bit_li = []

    for i in range(10) :
        bit = code[i*7 : (i*7)+7]       # 7자리씩 끊어서 만들어주기
        num = 0                         # 10진수로 변경된 숫자를 저장할 변수 생성

        for j in range(7) :                 # 2진수의 자리수는 7이기 때문에 7번 반복하자
            num += int(bit[6-j]) * (2**j)   # 2진수의 뒤쪽부터 2의 0승, 2의 1승... 등등을 해서 10진수를 바꿔서 더해준다.
        bit_li.append(num)                  # 다 바뀐 숫자를 리스트에 저장해준다(출력을 위해 모아둠)

    print(f'#{tc}', end=' ')
    print(*bit_li)              # 언패킹 해주기