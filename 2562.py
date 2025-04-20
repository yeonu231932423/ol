vmax = -999999999999
vc = -1
for i in range(9):
    v = int(input())
if vmax < v:
    vmax = v
    vc = i+1
print(vmax)
print(vc)