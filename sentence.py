'''sentence="welcome to cmr engineering college"
with using built in functions
str=sentence.title()
print(str)
print(ord('='))
print(ord('&'))
print(ord('*'))
print(ord('+'))
print(ord('!'))
print(ord('~'))
print(chr(0))
print(chr(48))
print(chr(58))
print(chr(1))
print(chr(3))
print(chr(38))'''
def convert(str):
    ch=list(str)
    for i in range(len(str)):
        if(i==0 and ch[i]!=' '):
            if(ch[i]>='a' and ch[i]<='2'):
                ch[i]=chr(ord(ch[i])-ord('a')+ord('A'))

        str1="",ch[i]
    return str1
print(convert("hello good"))