'''def remove_word(str,w):
    return str,replace(w," ")
    str1="hello cmrec hello"
    print("before removing")
    print(str1)
    print("after removing")
    print(remove_word(str1,"hello"))'''
def remove_word(string,word):
    return string.replace(word," ")
strin=input("Enter a string")
rmv=input("Enter word to remove")
outstring=remove_word(strin,rmv)
print("Modified string="+outstring)