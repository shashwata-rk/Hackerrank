n = int(input())
s = set(map(int, input().split()))
m = int(input())
l = set(map(int, input().split()))
print(len(s.union(l)))


