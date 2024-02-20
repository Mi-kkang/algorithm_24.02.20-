t = 10                  # 테스트 케이스 10개 고정

def in_order(T) :       # 중위 순회
    global ans
    if T :
        in_order(left[T])
        ans += word[T]
        in_order(right[T])

for tc in range(1, t+1) :
    N = int(input())        # 정점의 개수 N
    left = [0] * (N+1)      # 부모의 왼쪽 자식을 저장하는 리스트
    right = [0] * (N+1)     # 부모의 오른쪽 자식을 저장하는 리스트
    parent = [0] * (N+1)    # 자식의 인덱스에 부모를 저장하는 리스트 ((근데 이게 꼭 필요할까? 모른다))
    word = [0] * (N+1)      # 각 노드 번호에 매칭되어 있는 영단어를 저장할 리스트
    ans = ''                # 단어를 저장할 변수 생성


    for i in range(N) :
        li = input().split()
        # print(li)
        if len(li) == 2 :                   # 자식이 없는 경우
            word[int(li[0])] = li[1]        # 글자 저장해주기
        elif len(li) == 3 :                 # 자식이 하나 있는 경우
            word[int(li[0])] = li[1]
            left[int(li[0])] = int(li[2])
            parent[int(li[2])] = int(li[0])
        else :                              # 길이가 4인 경우(자식이 둘인 경우)
            word[int(li[0])] = li[1]
            left[int(li[0])] = int(li[2])
            right[int(li[0])] = int(li[3])
            parent[int(li[2])] = int(li[0])
            parent[int(li[3])] = int(li[0])
    # print(word)

    root = 1        # 완전 이진 트리 형식이기 때문에 루트노드는 1이다.
    in_order(root)

    print(f'#{tc} {ans}')