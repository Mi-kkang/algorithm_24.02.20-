def in_order(T, N) :
    if T <= N :                 # 존재하는 노드면
        in_order(T*2, N)        # 왼쪽자식 방문
        print(tree[T], end='')  # 부모노드 처리
        in_order(T*2+1, N)      # 오른쪽자식 방문


t = 10

for tc in range(1, t+1) :
    N = int(input())
    tree = [0] * (N+1)      # N번까지 있고, 노드가 비어있는 완전이진트리

    for _ in range(N) :
        node = list(input().split())        # int(node[0]) : node 번호, node[1] : 저장할 글자
        tree[int(node[0])] = node[1]
    print(f'#{tc}', end=' ')
    in_order(1, N)
    print()