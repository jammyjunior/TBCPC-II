import sys
sys.stdin = open("LATNEN.INP", "r")
sys.stdout = open("LATNEN.OUT", "w")

n = int(input())
l = []
c = 0
for _ in range(2):
    l.append([0] + list(map(int, input().split()))+[0])
for i in range(1, n+1):
    if l[0][i] == 1:
        if l[0][i-1] == 0:
            c+=1
        if l[0][i+1] == 0:
            c+=1
        if i%2==1:
            if l[1][i] == 0:
                c+=1

        else:
            c+=1

for i in range(1, n+1):
    if l[1][i] == 1:
        if l[1][i-1]==0:
            c+=1
        if l[1][i+1]==0:
            c+=1
        if i%2==1:
            if l[0][i] == 0:
                c+=1
        else:
            c+=1

print(c)

sys.stdin.close()
sys.stdout.close()
            
