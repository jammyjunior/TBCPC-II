import sys
sys.stdin = open("COMBO.INP", "r")
sys.stdout = open("COMBO.OUT", "w")

n = int(input())
l = list(map(int, input().split()))
m = 0
for i in range(n):
    for j in range(i, n):
        times = 1
        for k in range(i, j+1):
            times*=l[k]
        m = max(m, sum(l[:i])+sum(l[j+1:])+ times)
print(m%(10**9-7))

sys.stdin.close()
sys.stdout.close()
