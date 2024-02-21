def min_heap(n) :
    global last     # 마지막 위치를 표시할 last 불러오기
    last += 1
    h[last] = n
    c = last
    p = c//2

    while p>=1 and h[p] > h[c] :    # 위에 부모가 있고, 부모의 노드가 자식의 노드보다 클 때 계속,
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2

def find_ans(v) :
    ans = 0             # 마지막 노드의 조상 노드에 저장된 정수의 합을 넣기 위한 변수 생성
    c = v               # 자식 변수에 받아온 변수(last 위치)를 할당한다
    p = c//2            # 부모 위치를 알아낸다

    while p>=1 :        # 위에 부모가 있으면 계속
        ans += h[p]     # 위에 부모 노드에 들어있는 정수를 ans에 더해준다.
        c = p           # 부모 노드를 자식 노드로 바꿔주기
        p = c//2        # 다시 부모 노드를 구해준다.
    return ans          # 우리가 원하는 결과값을 리턴해준다.

t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N =int(input())         # 서로 다른 자연수 개수 N
    n_li = list(map(int, input().split()))      # 자연수 받기
    h = [0] * (N+1)         # 힙 만들어주기 // (N+1)인 이유는 리스트를 1번부터 N번까지 쓰기 위해서
    last = 0                # 힙의 마지막 위치를 저장할 변수

    for i in n_li :
        min_heap(i)

    res = find_ans(last)
    print(f'#{tc} {res}')
