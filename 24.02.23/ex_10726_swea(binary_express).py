def test() :
    tar = M
    for i in range(N) :
        if tar & 0x1 == 0 :
            return False
        tar = tar >> 1
    return True


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M = map(int, input().split())    # M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져있는지 아닌지를 판별하기 위한 변수들 받기

    # m_bin = bin(M)
    count = 0

    for i in range(N) :
        if M & 0x1 != 0 :
            count += 1
        m_bin = M >> 1


    # print(test())

    # print(m_bin)
    #
    # for i in range(N) :
    #     if M & (i<<1) :
    #         count += 1
    #
    if N == count :
        print(f'#{tc} ON')
    else :
        print(f'#{tc} OFF')