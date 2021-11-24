N = int(input())
W = float(input())
L = float(input())
M = int(input())
O= int(input())

S = N*N
S_plochka = W * L
S_bench=M * O
S_final = (S-S_bench)/S_plochka
time = S_final * 0.2
print(round(S_final,2))
print(round(time,2))
