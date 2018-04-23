def master_yoda(text):
    list1 = list(text)
    list1.append(" ")
    list2 = []
    str = ""
    
    for i in list1:
        
        str += i
        if (i == ' '):
            #print(str)
            list2.append(str)
            str = ""
            
    #print(list2)
    revlist = list2[::-1]
   
    strfinal = ' '.join(revlist)
    print(strfinal)
 
