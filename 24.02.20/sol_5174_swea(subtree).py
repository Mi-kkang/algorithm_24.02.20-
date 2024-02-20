def f(T) :
    if T == 0 :         # 노드가 존재하지 않으면 방문한 노드수 0
        return 0
    else :                  # 노드 T가 존재하면
        r1 = f(left[T])     # 왼쪽 자식으로 이동, 왼쪽 서브트리 노드수 리턴
        r2 = f(right[T])    # 오른쪽 자식으로 이동, 오른쪽 서브트리 노드수 리턴
        return r1 + r2 + 1  # 좌우 서브트리 노드수 + T 노드


T = int(input())

for tc in range(1, T+1) :
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    V = E + 1       # 1에서 V번 정점 존재
    left = [0] * (V+1)  # left[T] T의 왼쪽자식 저장
    right = [0] * (V+1) # right[T] T의 오른쪽자식 저장

    for i in range(E) :
        p, c = arr[i*2], arr[i*2+1]
        if left[p] == 0 :
            left[p] = c
        else :
            right[p] = c

    result = f(N)

    print(f'#{tc} {result}')