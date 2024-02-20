N = int(input())            # 줄을 서는 사람의 수 받기
card = list(map(int, input().split()))

# print(card)

arr = [i for i in range(1, N+1)]
new_line = [0] * (N)

# print('arr : ', arr)
# print('new_line : ', new_line)

for i in range(N) :
    new_line[i] = arr[i]    # 일단 배치해둔다.
    change = card[i]        # 얼마나 앞으로 갈 수 있는지를 저장해준다.

    # print('before : ', new_line)

    if i >= 1 :                                                         # 2번째 학생부터
        for j in range(i, i-change, -1) :                               # 학생이 위치한 자리부터 앞으로 갈 수 있는 자리까지 역순으로
            new_line[j], new_line[j-1] = new_line[j-1], new_line[j]     # 바로 앞 사람과 자리를 바꿔준다.

    # print('after : ', new_line)

print(*new_line)