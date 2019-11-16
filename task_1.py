print("\n\n\t\t\tSmart marksheet generator")
print("Enter Engrlish marks")
english=float(input())
print("Enter Maths marks")
maths=float(input())
print("Enter Physics marks")
physics=float(input())
print("Enter Chemistry marks")
chemistry=float(input())
print("Enter Urdu marks")
urdu=float(input())
total=english+maths+physics+chemistry+urdu
per=(total/500)*100
print("\t**********************************************************")
print("\t*                     Annual Exam Result                 *")
print("\t**********************************************************")
print("\t*Subjects              Total marks          Obtained marks")
print("\t**********************************************************")
print("\tEnglish                  100            "+"\t"+str(english))
print("\tMaths                    100            "+"\t"+str(maths))
print("\tPhysics                  100            "+"\t"+str(physics))
print("\tChemistry                100            "+"\t"+str(chemistry))
print("\tUrdu                     100            "+"\t"+str(urdu))
print("\t**********************************************************")
print("\tTotal                    500            "+"\t"+str(total))
print("\tPercentage :"+str(per))
if(per>=85 and per<=100):
    print("\tGrade      :A+")
elif(per>=75 and per<85):
    print("\tGrade      :A")
elif(per>=65 and per<75):
    print("\tGrade      :B+") 
elif(per>=55 and per<65):
    print("\tGrade      :B")
elif(per<50):
    print("\tYou are FAIL!!!")


