N = int(input())
arr = [[0]*7 for _ in range(2)]
plus = N
minus = N

for i in range(4) :
    arr[0][i] = N + i
    arr[1][6-i] = N - i

# print(arr)
print(arr[0])
print(arr[1])