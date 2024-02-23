t = int(input())            # 테스트 케이스 개수 받기

for tc in range(1, t+1) :
    N = int(input())                            # 당근의 개수 N
    carrot = list(map(int, input().split()))    # 당근의 크기 리스트
    size = 0                # 처음 사이즈 / 초기화 했을 때 사이즈 저장용 변수 생성
    max_c = 0               # 연속으로 커지는 당근 개수의 최대값을 저장할 변수

    