import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    x=0
    for k in alphabet:
        x+=1
        if(k in str1):
            pass
        else:
           return False
           break
        if(x==len(alphabet) and k in str1):
            return True
            
