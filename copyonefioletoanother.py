fp1=open("cse.text","r")
fp2=open("ece.text","w+")
if fp1:
    print("File open successfully")
for i in fp1:
    fp2.write(i)
print("File is copied successfully")
fp2.seek(0,0)
content=fp2.read()
print(content)
fp1.close()
fp2.close()