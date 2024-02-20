t = int(input())            # 테스트 케이스 개수 받기

def in_order(T) :           # 중위 탐색
    global n
    if T :
        in_order(left[T])
        num_li[T] = n
        n += 1
        in_order(right[T])

for tc in range(1, t+1) :
    N = int(input())        # 1~N 까지의 자연수를 이진 탐색 트리에 저장할 예정 / 노드가 N개라는 의미
    left = [0] * (N+1)      # 부모 인덱스에 왼쪽 자식을 저장할 리스트
    right = [0] * (N+1)     # 부모 인덱스에 오른쪽 자식을 저장할 리스트
    parent = [0] * (N+1)    # 자식 인덱스에 부모를 저장할 리스트
    num_li = [0] * (N+1)    # 이진 탐색 트리 노드 번호에 따른 값 리스트
    n = 1                   # 1부터 시작하는 숫자 넣기 / 를 위한 n 만들기

    for i in range(1, N+1) :    # 완전 이진 트리를 만들기 위한 반복문이다.
        # 규칙을 살펴볼 때, 부모 노드와 자식 노드의 숫자가 각각 부모 : i  왼쪽자식 : 2*i 오른쪽자식 : 2*i + 1이다.
        # 이 규칙을 이용하여 각각의 리스트에 저장해준다. 이때, 규칙의 숫자가 우리의 노드 개수보다 작거나 같아야 한다.
        if i * 2 <= N :
            left[i] = i * 2
            parent[i*2] = i
        if (i * 2) + 1 <= N :
            right[i] = (i * 2) + 1
            parent[(i*2)+1] = i

    root = 1                # 이진 탐색 트리는 루트가 1로 고정
    in_order(root)
    ans1 = num_li[root]
    ans2 = num_li[N//2]

    print(f'#{tc} {ans1} {ans2}')