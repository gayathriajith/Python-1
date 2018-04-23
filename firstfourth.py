def old_macdonald(name):
    list1=list(name)
    a = list1[0].upper()
    b = list1[3].upper()
    new = ""
    list1[0]=a
    list1[3]=b
    for i in list1:
        new +=i
    return new
