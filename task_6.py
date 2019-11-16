temp_list=[1,1,2,3,5,8,13,21,34,55,89]
a=0
b=0
while(a<len(temp_list)):
    if(temp_list[a]<5):
        if(temp_list==b):
            print("\n"+str(temp_list[a]))
        else:
            print("\n"+str(temp_list[a]))
            b=temp_list[a]
        
        
    a=a+1
