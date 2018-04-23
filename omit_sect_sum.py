def summer_69(arr):
    six=0
    new=0
    for i in arr:
        
        if(six==1) and (i!=9):
            continue
        if(six==1):
            if(i==9):
                six=0
                continue
        if(i!=6):
            new=new+i
            
        if(i==6):
            six=1
            
    return new
