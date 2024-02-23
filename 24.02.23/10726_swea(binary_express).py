t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    # M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 확인할 예정이다.
    N, M = map(int, input().split())    # N과 M 받기
    # 마지막 N개의 비트가 모두 1로 켜져 있는지를 확인하기 위한 num 만들어주기
    # 만약 N = 4 라면 이진수 1111이 나와야 한다. 10000 - 1 을 하면 1111이 나온다.
    num = (1<<N) - 1

    if M & num == num :         # AND를 사용해서 뒷자리가 모두 1인지 확인해본다.
        print(f'#{tc} ON')
    else :
        print(f'#{tc} OFF')