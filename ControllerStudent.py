import Student

class ControllerStudent():

    def __init__(self):
        self.__students = {}
    
    def addStudent(self,dni,name,surname,age,city,province,email):

        student = Student.Student(dni,name,surname,age,city,province,email)
        if (dni in self.__students.keys()):
            return False
        else:
            self.__students[student.getDni()] = student
            return True


    def delStudent(self,dni):
        if dni in self.__students.keys():
            student = self.__students.pop(dni)
            return student
        else:
            return None

    
    def modifyStudent(self,dni, properties):
        student = self.__students[dni]
        for prop, value in properties.items():
            if (prop == "Name"):
                student.setName(value)
            if (prop == "Surname"):
                student.setSurname(value)
            if (prop == "Age"):
                student.setAge(value)

    def searchStudent(self,dni):
        return self.__students.get(dni)
    

