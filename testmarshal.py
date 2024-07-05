import marshal
fp=open("Marsh1.txt","rb")
data=marshal.load(fp)
exec(data)