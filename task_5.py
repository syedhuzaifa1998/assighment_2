num_list=[24,12,56,44]

temp1=1
a=0
while(a<len(num_list)):
    if(num_list[a]>temp1):
        temp1=num_list[a]
    a=a+1
print("Largest number is :"+str(temp1))
    

