import sys
sys.stdin = open("VATSUA.INP", "r")
sys.stdout = open("VATSUA.OUT", "w")

n = int(input())
l = [0] + list(map(int, input().split()))
result = []
ltemp = []
for i in range(n+1):
    ltemp.append(l[i])
ltemp.sort()
temp = 0
for i in range(1, n+1):
    temp+=(ltemp[i] * i)
result.append(temp)
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    
    ltemp = []
    for i in range(n+1):
        ltemp.append(l[i])
    ltemp[a] = b
    ltemp.sort()
    temp = 0
    for i in range(1, n+1):
        temp+=(ltemp[i] * i)
    result.append(temp)
for temp in result:
    print(temp)

sys.stdin.close()
sys.stdout.close()
