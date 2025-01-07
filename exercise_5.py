class Department(object):
    nameOfDepartment = ''
    employeesCount = None
    managerName = ''

    def __init__(self, nameOfDepartment):
        self.nameOfDepartment = nameOfDepartment

    def setDepartmentInformation(self, employeesCount, managerName):
        self.employeesCount = employeesCount
        self.managerName = managerName

    def getDepartmentInformation(self):
        return """        Name of department: {}
        Manager's name: {}
        Employees count: {}
        """.format(self.nameOfDepartment, self.managerName, self.employeesCount)
    

class PartOfDepartment(Department):
    partName = ''
    employees = []

    def __init__(self, nameOfDepartment, partName):
        super().__init__(nameOfDepartment)
        self.partName = partName

    def setEmployees(self, employees):
        for i in employees:
            self.employees.append(i)
        # self.employees = employees # .sort()???

    def getEmployees(self):
        stri = ""
        for i in self.employees:
            if stri == "":
                stri = stri + i
            else:
                stri = stri + ", " + i
        return """{}'s {}'s employees: {}.""".format(self.nameOfDepartment, self.partName, stri)

d1 = Department("Restaurant")
d2 = Department("Sales management")
d1.setDepartmentInformation(12, "Inga Indziņa")

p1 = PartOfDepartment("Administration", "Customer Service")
p2 = PartOfDepartment("Restaurant", "Kitchen")
p1.setDepartmentInformation(4, "Ingus Ingusiņš")
p1.setEmployees(["Ilze", "Ilga", "Aigars", "Aivars"])

print(d1.getDepartmentInformation())
print(p1.getDepartmentInformation())
print(p1.getEmployees())
    



