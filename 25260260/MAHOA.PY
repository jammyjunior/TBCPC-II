import sys
sys.stdin = open("MAHOA.INP", "r")
sys.stdout = open("MAHOA.OUT", "w")

n = input()

condition2 = n[:len(n)//2] == n[len(n)//2:]
condition3 = n[:len(n)//3] == n[len(n)//3:(len(n)//3)*2] == n[(len(n)//3)*2:]
if condition2 and condition3:
    print(int(n[:len(n)//3])+2026, int(n[:len(n)//2])+2026)
elif condition2:
    print(int(n[:len(n)//2])+2026)
elif condition3:
    print(int(n[:len(n)//3])+2026)
else:
    print(-1)

sys.stdin.close()
sys.stdout.close()
