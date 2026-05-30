subject_marks ={
    "marks_subject_1": input("Enter the marks of 1st subject: "),
    "maarks_subject_2": input("Enter the marks of 2nd subject: "),
    "marks_subject_3": input("Enter the marks of 3rd subject: "),
}
print(subject_marks)

#OR

marks={}

marks_subject_1= int(input("Enter the marks of 1st subject: "))
marks.update({"1_subject" : marks_subject_1})

marks_subject_2= int(input("Enter the marks of 2nd subject: "))
marks.update({"2_subject" : marks_subject_2})

marks_subject_3= int(input("Enter teh marks of 3rd subject: "))
marks.update({"3_subject" : marks_subject_3})

print(marks)