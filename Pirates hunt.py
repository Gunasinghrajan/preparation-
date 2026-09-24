# Treasure hunt problem

x=int(input())
y=int(input())
z=int(input())

sl=int((y/100)*x)
sb=int((z/100)*(x-sl))
sp=int((x-(sl+sb))/3)

print(sl)
print(sb)
print(sp)
