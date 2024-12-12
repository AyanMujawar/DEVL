student_scores = {"Ayan":90 , "OM":80 , "Meghan" : 70}

def add_student(name, score):
    student_scores[name] = score
    print("ADD STUDENT")
    

def update_score(name, new_score):
    if name in student_scores:
        student_scores[name] = new_score
        print("INFO UPDATED")
    else:
        print("STUDENT DATA NOT FOUND")

def delete_student(name):
    if name in student_scores:
        del student_scores[name]
        print(f"DELETED STUDENT")
    else:
        print("STUDENT NOT FOUND")

def highest_score():
    max_score = max(student_scores.values())
    for name, score in student_scores.items():
        if score == max_score:
            print(f"The highest score is held by {name}")         
        
while(1):

    choice= int(input("1.ADD A STUDENT\n"
                     "2.UPDATE SCORES\n"
                     "3.DELETE STUDENTS\n"
                     "4.FIND HIGHEST STUDENT MAKRS\n"
                     "5.DISPLAY RECORDS\n"
                     "6.EXIT\n"
                     "Enter your choice - "))
    if(choice==1):
        name=input("Enter name of student to add : ")
        marks=int(input("Enter Marks of The Student : "))
        add_student(name,marks)
    elif(choice==2):
        name=input("Enter name of student to update the Marks for : ")
        marks=int(input("Enter the updated marks : "))
        update_score(name,marks)
    elif(choice ==3 ):
        name=input("Enter name of student to Delete : ")
        delete_student(name)
    elif(choice==4):
        highest_score()
    elif(choice==5):
        print(student_scores)    
    elif(choice==6):
        print("EXITING PROGRAM")
        break
    else:
        print("INVALID CHOICE")