h,m = map(int,input().split())
if m>=45:
    print(h,m-45)
else:
    h = h +24- 1
    m = m + 60 - 45
    print(h%24,m)