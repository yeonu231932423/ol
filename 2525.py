h,m=map(int, input().split())
c=int(input())

m = m+c
h = (h + m//60)%24
m = 