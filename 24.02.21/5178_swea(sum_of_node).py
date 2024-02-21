# def make_node(n) :
#     global N                # 노드의 개수를 글로벌 변수로 설정해주기
#     c = n
#     p = c//2
#
#     while p>=1 :
#         if c+1 <= N :       # 노드 번호가 노드의 개수보다 작거나 같을 때, (가능한 노드 번호일 때,)
#             h[p] = h[c] + h[c+1]
#         else :
#             h[p] = h[c]
#         c = p
#         p = c//2
# 처음에 위에 있는 함수 방식으로 시도해 보았으나, 이렇게 할 경우 중간에 채워지지 않는 노드가 있어서 값이 다르게 나옴

def make_node(n) :
    global N                        # 노드의 개수를 글로벌 변수로 설정해주기

    while n :                       # n이 1 이상일 경우 계속한다,
        c = n                       # 자식 노드 번호를 n으로 설정해준다
        p = c//2                    # 자식 노드를 통해 부모 노드를 생성
        if c+1 > N :                # 자식노드 +1 이 노드의 개수보다 크면
            h[p] = h[c]             # 부모 노드 숫자가 왼쪽 자식노드의 값이다
        else :                      # 아니라면
            h[p] = h[c] + h[c+1]    # 부모 노드의 숫자는 왼쪽 + 오른쪽 자식노드의 값이다.
        n -= 1                      # n의 값을 하나 줄여준다. (모든 값을 확인하기 위해서)


t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N, M, L = map(int, input().split())     # 노드의 개수 N, 리프 노드의 개수 M, 값을 출력할 노드 번호 L
    h = [0] * (N+1)                         # 노드를 저장할 힙을 만든다.
    last = 0                                # 마지막 노드를 저장할 변수를 만든다.
    for _ in range(M) :
        node_n, node_v = map(int, input().split())      # 리프 노드 번호와 그 노드에 들어갈 값을 받는다.
        h[node_n] = node_v

        if last < node_n and node_n % 2 == 0 :          # 나는 왼쪽 노드를 기준으로 보기 위해 이렇게 설정함.
            last = node_n

    make_node(last)
    # make_node(N) 도 가능하다! // 나는 왼쪽 노드를 기준으로 보고싶었기에 이렇게 설정했다!

    print(f'#{tc} {h[L]}')