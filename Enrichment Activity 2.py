name = str(input("Enter name of student: "))
english = float(input("Enter English marks: "))
while(english>50):
   english = float(input("Enter English marks less than 50: "))
   if(english<=50):
       continue
maths = float(input("Enter Maths marks: "))
while(maths>50):
   maths = float(input("Enter Maths marks less than 50: "))
   if(maths<=50):
       continue
hindi = float(input("Enter Hindi marks: "))
while(hindi>50):
   hindi = float(input("Enter Hindi marks less than 50: "))
   if(hindi<=50):
       continue
science = float(input("Enter Science marks: "))
while(science>50):
   science = float(input("Enter Science marks less than 50: "))
   if(science<=50):
       continue
social_science = float(input("Enter Social Science marks: "))
while(social_science>50):
   social_science = float(input("Enter Social Science marks less than 50: "))
   if(social_science<=50):
       continue

total = english + maths + hindi + science + social_science
percentage = (total/250)*100

print("\n\nMarksheet of ",name)
print("\nSUBJECT MARKS")
print("\nEnglish: ",english)
print("\nMaths: ",maths)
print("\nHindi: ",hindi)
print("\nScience: ",science)
print("\nSocial Science: ",social_science)
print("\nTOTAL MARKS: ",total)
print("\nPERCENTAGE: ",percentage,"%\n")


if(percentage>=75):
    print("DIVISION: Distinction")
elif(percentage<75 and percentage>60):
    print("DIVISION: First Division")
elif(percentage<=60 and percentage>=40):
    print("DIVISION: Second Division")
else:
    print("DIVISION: Fail")


