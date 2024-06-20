def commas(str):
    x=str.replace('-',',')[1:-1]
    return x
x="Apple"
print(repr(commas(x)))

