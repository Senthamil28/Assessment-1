l=[]
i=int(input("Enter number of elements:"))
for s in range(0,i):
    t=input("Enter a element:")
    l.append(t)
sa=input("Which element's potition is you need?")
print(l.index(sa))
