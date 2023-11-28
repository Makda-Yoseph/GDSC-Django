student = {}

print("what would you like to do :\n 1.add student\n 2. view student ifo detail\n list all students\n3.update info fo a tudent.")
choice = int(input())
count = 0
if choice == 1:
    num = int(input("how many students you want to add"))
    while(count< num):
        info = []
        name=input("enter the name of the student")
        age = int(input("Enter age"))
        info.append(age)
        grade = int(input("Enter grade"))
        info.append(grade)
        Id= input("Enter ID")
        info.append(Id)
        student[name]= info
        count +=1
elif choice ==2:
    print("Here is students inforamtion list: ")
    print("-------------------------------------------")
    for key,value in student:
        print(key,student[key])
elif choice==3:
    update_key = input("what is the name of student you want to update?")
    print("please fill the updated information ")
    update=[]
    age = int(input("Enter age"))
    update.append(age)
    grade = int(input("Enter grade"))
    update.append(grade)
    Id= input("Enter ID")
    update.append(Id)
    student[update_key]= update



