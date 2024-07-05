import pickle
fp=open("picklefile.txt",'wb')
cn=["navya","prasu","neeru"]
pickle.dump(cn,fp)
fp.close()