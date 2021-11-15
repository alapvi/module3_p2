import ControllerStudent, Student
import re

def readDNI():
    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    while True:
        try:
            dni = input("DNI:")
            letter = dni[-1].upper()
            number = dni[:-1]
            if (len(dni) == 9 and number.isdigit()):
                number = int(dni[:-1])
            else:
                print("Incorrect DNI")
                continue
        except:
            print("Incorrect format DNI")
            continue

        mod = number%23
        if letters[mod] == letter:
            return dni
        else:
            print("Incorrect Letter!")


def readName():
    while True:
        name = input("Name:")
        if (len(name) > 0):
            return name
        else:
            print("Input a valid name")


def readAge():
    while True:
        try:
            age = int(input("Age:"))
            if age > 0:
                return age
            else:
                print("Age must be >0")

        except:
            print("Age error!")

def readSurname():
    while True:
        surname = input("Surname:")
        if (len(surname) > 0):
            return surname
        else:
            print("Input a valid surname")

def readCity():
    while True:
        city = input("City:")
        if (len(city) > 0):
            return city
        else:
            print("Input a valid city")

def readProvince():
    while True:
        prov = input("Province:")
        if (len(prov) > 0):
            return prov
        else:
            print("Input a valid prov")

def readEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    while True:
        email = input("Email:")
        if(re.fullmatch(regex, email)):
            return email
        else:
            print("Input a valid Email")


controller = ControllerStudent.ControllerStudent()

while (True):
    print("1.- Add Student")
    print("2.- Delete Student")
    print("3.- Modify Student")
    print("4.- Search Student")
    print("5.- Exit")
    
    option = input("Choose an option:")
    if (option == "5"):
        break
    elif (option == "1"):
        dni = readDNI()
        name = readName()
        surname = readSurname()
        age = readAge()
        city = readCity()
        province = readProvince()
        email = readEmail()
        if controller.addStudent(dni,name,surname,age,city,province,email):
            print("Student added successfully!")
        else:
            print("Error, the student is already created!")

    elif (option == "2"):
        dni = readDNI()
        student = controller.delStudent(dni)
        if student != None:
            print("The student ",student.getName()," has been deleted!")
        else:
            print("The DNI doesn't exists!")
    elif (option == "3"):
        dni = readDNI()
        student = controller.searchStudent(dni)
        if student != None:
            print("Modification of student with DNI:", student.getDni())
            print("1.- Modify Name")
            print("2.- Modify Surname")
            print("3.- Modify Age")
            op = input("What do you want to modify:")
            if (op == "1"):
                newName = readName()
                prop = {'Name': newName}
                controller.modifyStudent(dni,prop)
            if (op == "2"):
                newSur = readSurname()
                prop = {'Surname': newSur}
                controller.modifyStudent(dni,prop)
            if (op == "3"):
                newAge = readAge()
                prop = {'Age': newAge}
                controller.modifyStudent(dni,prop)
        else:
            print("The DNI doesn't exists!")
    elif (option == "4"):
        dni = readDNI()
        student = controller.searchStudent(dni)
        if student != None:
            print("Name", student.getName())
            print("Surname", student.getSurname())
            print("email", student.getEmail())
        else:
            print("The DNI doesn't exists!")


    
    


