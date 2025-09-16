from math import sqrt as S
out = []
number = int(input().strip())
for i in range(0,number):
    A = int(input().strip())
    out.append(round(S(A),4)) # or out.append(f"{S(A):.4f}")
print(out)