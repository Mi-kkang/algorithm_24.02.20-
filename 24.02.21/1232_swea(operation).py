def operation(s, n) :               # 중위 순회의 방식이다.
    if s <= n and s != 0 :          # 나는 리스트로 만들었기 때문에 값이 0인지 아닌지도 확인해야 함!
        # 그냥 이진트리로 만들 경우, left[s] ==> s*2 / right[s] ==> s*2+1 로 하면 된다
        one = operation(left[s], n)
        oper = node_li[s]
        two = operation(right[s], n)

        if oper == '+' :
            return one + two
        elif oper == '-' :
            return one - two
        elif oper == '*' :
            return one * two
        elif oper == '/' :
            return one // two
        else :
            return int(oper)        # 만약 부모의 노드가 연산자가 아니면 숫자이기 때문에 int로 반환해준다.


t = 10                      # 테스트 케이스 개수 10개 고정

for tc in range(1, t+1) :
    N = int(input())        # 정점의 개수 N
    E = N-1
    left = [0] * (N+1)      # 해당 인덱스의 왼쪽 자식 노드를 저장할 리스트
    right = [0] * (N+1)     # 해당 인덱스의 오른쪽 자식 노드를 저장할 리스트
    # par = [0] * (N+1)       # 해당 인덱스의 부모 노드를 저장할 리스트
    node_li = [0] * (N+1)   # 해당 인덱스의 노드에 저장되어 있는 값(연산자)을 저장할 리스트

    for i in range(N) :
        li = input().split()

        if len(li) == 4 :       # 받은 노드가 왼쪽, 오른쪽 자식이 다 있을 경우,
            left[int(li[0])] = int(li[2])
            right[int(li[0])] = int(li[3])
            node_li[int(li[0])] = li[1]
        elif len(li) == 3 :     # 받은 노드가 왼쪽 자식만 있을 경우, (그런데 이게 필요할까?)
            left[int(li[0])] = int(li[2])
            node_li[int(li[0])] = li[1]
        else :                  # 받은 노드가 자식이 없을 경우(리프 노드일 경우)
            node_li[int(li[0])] = li[1]

    # print(left)

    ans = operation(1, N)
    print(f'#{tc} {ans}')