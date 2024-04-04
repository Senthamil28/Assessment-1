dic={}
sa=int(input("Enter the number of key pairs:"))
for i in range(sa):
    key=input("Enter key:")
    value=input("Enter value:")
    dic[key]=value
print(dic)
sas=list(dic.keys())
print("The keys are -",sas)
