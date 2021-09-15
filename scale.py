num = input()
scl = int(input())
data = []
alf = "0123456789ABCDEF"
ans = 0
for i in range (len(num)):
    data += [(alf.find(num[i]))]
data = list(map(int, data))
data.reverse()
for u in range(len(data)):
    ans += data[u]*(scl**u)
print(ans)
