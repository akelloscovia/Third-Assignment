student_names = ['Sandra','Patricia','Phiona','Anita']
student_marks =[80, 56,78,90]
# print Patricia,Faith,Phiona and Anita
#Add Marsha at the fourth position
#Update the name Phiona to Phiona Aladina 
#Display the length of the student list
#Print all student names using a for loop
#Calculate the total marks for the student marks variable


#answer(i)
print(student_names[1:3])


#answer(ii)
student_names.insert(3, "Marsha") 
print(student_names.insert(3,"Marsha"))

#answer(iii)
student_names[2] = 'Phionah Aladinah'
print (student_names)

#answer(iv) 
#the length of the student list
length = len(student_names)
print(length)

#answer(v)
print("Student names:")
for name in student_names:
    print(name)

#answer(vi)
total_marks = sum(student_marks)
print("Total marks:", total_marks)

