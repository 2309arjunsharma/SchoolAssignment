name = str(input("Enter name of student: "))
english = float(input("Enter English marks: "))
maths = float(input("Enter Maths marks: "))
hindi = float(input("Enter Hindi marks: "))
science = float(input("Enter Science marks: "))
social_science = float(input("Enter Social Science marks: "))

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

#75 and above Distinction
#61 - 74 First Division
#40 - 60 Second Division
#Below 40 Fail

if(percentage>=75):
    print("DIVISION: Distinction")
elif(percentage<75 and percentage>60):
    print("DIVISION: First Division")
elif(percentage<=60 and percentage>=40):
    print("DIVISION: Second Division")
else:
    print("DIVISION: Fail")


