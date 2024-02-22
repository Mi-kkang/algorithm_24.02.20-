import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output01.txt', 'w')

# text = input()
# print(text)
a, b = map(int, input().split())
print(a + b)
print(a * b)