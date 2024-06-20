def invert_content(dic):
    invert_dec={}
    invert_dec={k:v for v,k in dic.items()}
    return invert_dec
n=int(input("number of values"))
dic={}
for i in range(n):
    key=input("Enter key")
    value=input("Enter value")
    dic[key]=value
print(dic)
print(invert_content(dic))