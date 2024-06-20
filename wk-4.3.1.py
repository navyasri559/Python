def commas(s):
    b=s.replace(' ',',')[1:-1]
    return b
print(repr(commas("Apple")))