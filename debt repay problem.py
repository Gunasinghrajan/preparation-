# Debt repay problem

p=int(input())
r=int(input())
y=int(input())

pa=float(p)
ri=float(r)
ys=float(y)

pi=(pa*ri*ys)/100
it=pa+pi
di=(2/100)*pi
fin=it-di


si=f"{pi:.2f}"
i=f"{it:.2f}"
dis=f"{di:.2f}"
fa=f"{fin:.2f}"

print(si)
print(i)
print(dis)
print(fa)
