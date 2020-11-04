names = [
    'Gabriel','Paul','John','Temi','Amaka',
    'Sandra','Helen','Samuel','Moses','Chidinma'
]

courses = ['Web Design','Python Bootcamp','Data Science','Web Development']

students = {
    #regno:[#names,course,age]
}

#regno: 6 digit

import random as rd
rd.seed(57)

count = 1
while count <= 1000:
    regNo = rd.randrange(100000,999999)
    Fullname = names[rd.randrange(0,9)] + ' ' + names[rd.randrange(0,9)]
    picked_course = courses[rd.randrange(0,3)]
    student_age = rd.randrange(15,45)
    
    students[regNo] = (Fullname,picked_course,student_age)
    
    count = count + 1

#verification
reg = int(input('Enter your Reg No: \n'))

if reg in students:
    print(f"""
    --------------------------------------
    |SUCCESSFULLY VERIFIED!              |
    |====================================|
    |NAME: {students[reg][0]}............|
    |COURSE: {students[reg][1]}..........|
    |AGE: {students[reg][2]}.............|
    --------------------------------------
    """)
else:
    print("""
    --------------------------------------
    |We could'nt verify your certificate |
    --------------------------------------
    """)
