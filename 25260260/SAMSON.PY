import sys
sys.stdin = open("SAMSON.INP", "r")
sys.stdout = open("SAMSON.OUT", "w")

n = int(input())
l = list(map(int, input().split()))
count = {}
c = 0
t = 1
for i in l:
    count[i] = count.get(i, 0)+1
for v in count.values():
    if v!=1:
        t*=v
    c+=1
t = (2*t)%(10**9-7)
print(c, t)

sys.stdin.close()
sys.stdout.close()
