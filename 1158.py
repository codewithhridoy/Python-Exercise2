N = int(input())
item_list = []

for i in range(N):
    X, Y = list(map(int, input().split()))

for item in range(1, Y):
    if((X % 2) != 0):
        item_list.append(X)
    X += 1
print(sum(item_list))
