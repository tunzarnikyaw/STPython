from random import randint

students = [
    "Hla Aye Myint", 
    "Kyaw Htet Aung", 
    "Myo Aung Hlaing", 
    "Shine Ko Oo",
    "Thant Sin Htet",
    "Thein Htike",
    "Thu Maung",
    "Thuta Zaw",
    "Ye Htet"
    ]

for i in range(3):
    r = randint(0, len(students)-1 )  # 0 ~ len()-1
    print( students[r] )
    students.remove( students[r] )
