def spy_game(nums):
    x = 0
    zero1 = 0
    zero2 = 0
    seven = 0
    for i in nums:
        x+=1
        
        if(zero2==1)and(i==7):
            seven=1
            return True
            break
            
        if(x==len(nums) and seven==0 ):
            return False
            break
            
        if(zero1==1)and (i==0):
            zero2=1
            continue
                     
        if(x==len(nums) and seven==0):
            return False
            break
        
        if(i!=0):           
            continue
            
        if(i==0):
            zero1=1        
            continue
