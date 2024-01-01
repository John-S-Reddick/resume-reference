from utilities import *
from tkinter import *

#Create Windows
def makeEntries(root, values, insQ):
    x = 0
    for(lab) in values:
        if(lab != "br"):
            Label(root, text=lab).grid(row = x)

            values[lab] = Entry(root, bd =5)
            values[lab].grid(row = x, column = 2)
        else:
            Label(root, text="").grid(row = x)
        x = x + 1;

    submit = Button(root, text = 'Submit', command = insQ)
    submit.grid(row = x)
    root.mainloop()

def viewTableWin(str):
    root = Tk()
    i = 1
    data = viewTable(str)
    for row in data:
        for j in range(len(row)):
            e = Label(root, text=row[j],borderwidth=2,relief='ridge', anchor="w")
            e.grid(row=i, column=j)
        i=i+1

    root.mainloop()

#Course
def addCourseWin():
    values = {
        "Course name": None,
        "Course description": None,
        "Course number": None,
        "Number of semester hours": None,
        "Level": None,
        "Offering department": None
    }

    def addCourse():
        insCourse([
            values["Course name"].get(),
            values["Course description"].get(),
            values["Course number"].get(),
            int(values["Number of semester hours"].get()),
            values["Level"].get(),
            values["Offering department"].get()
            ])

    makeEntries(Tk(), values, addCourse)

def viewCourse():
    viewTableWin("SELECT * FROM Course")

#Department
def addDeptWin():
    values = {
        "Department Name": None,
        "Department Code": None,
        "Office number": None,
        "Office phone": None,
        "College": None
    }

    def addDept():
        insDept([
            values["Department Name"].get(),
            values["Department Code"].get(),
            values["Office number"].get(),
            values["Office phone"].get(),
            values["College"].get()
            ])

    makeEntries(Tk(), values, addDept)

def viewDept():
    viewTableWin("SELECT * FROM Department")


#Section
def addSectionWin():
    values = {
        "Instructor": None,
        "Semester": None,
        "Year": None,
        "Course": None,
        "Section Number": None
    }

    def addSection():
        insSection([
            values["Instructor"],
            values["Semester"],
            values["Year"],
            values["Course"],
            values["Section Number"]
            ])

    makeEntries(Tk(), values, addSection)

def viewSect():
    viewTableWin("SELECT * FROM Section")


#Student
def addStudentWin():
    values = {
        "First Name": None,
        "Last Name": None,
        "N number": None,
        "SSN": None,
        "br": None,
        "Birth Date": None,
        "Sex": None,
        "br": None,
        "Class": None,
        "Major": None,
        "Minor": None,
        "br": None,
        "Current Address": None,
        "Current City": None,
        "Current State": None,
        "Current Zip": None,
        "Current Phone": None,
        "br": None,
        "Permanent Address": None,
        "Permanent City": None,
        "Permanent State": None,
        "Permanent Zip": None,
        "Permanent Phone": None
        }

    def addStudent():
        insStudent([
            values["First Name"].get(),
            values["Last Name"].get(),
            values["N number"].get(),
            values["SSN"].get(),
            values["Birth Date"].get(),
            values["Sex"].get(),
            values["br"].get(),
            values["Class"].get(),
            values["Major"].get(),
            values["Minor"].get(),
            values["Current Address"].get(),
            values["Current City"].get(),
            values["Current State"].get(),
            values["Current Zip"].get(),
            values["Current Phone"].get(),
            values["Permanent Address"].get(),
            values["Permanent City"].get(),
            values["Permanent State"].get(),
            values["Permanent Zip"].get(),
            values["Permanent Phone"].get()
        ])

    makeEntries(Tk(), values, addStudent)

def viewStudent():
    viewTableWin("SELECT * FROM Student")

def addGradeWin():
    values = {
        "Nnumber": None,
        "Course": None,
        "Section": None,
        "Grade": None
        }

    def addGrade():
        insGrade([
        values["Nnumber"].get(),
        values["Course"].get(),
        values["Section"].get(),
        values["Grade"].get()
        ])

    makeEntries(Tk(), values, addGrade)

def getReport():
    root = Tk()

    Label(root, text="N number").grid()
    gradeReport = Entry(root, bd =5)
    gradeReport.grid(row = 1)

    def showReport():
        viewTable("SELECT * FROM Grade WHERE nnum =" + gradeReport.get())

    Button(root, text = 'Get', command = showReport).grid(row = 1, column = 7)
    root.mainloop()



#Main ui
def menuWin():
    root = Tk()
    Label(root, text="Course").grid(row = 1)
    Button(root, text = 'Recreate', command = createCourse).grid(row = 1, column = 3)
    Button(root, text = 'Add Entry', command = addCourseWin).grid(row = 1, column = 5)
    Button(root, text = 'View', command = viewCourse).grid(row = 1, column = 7)

    Label(root, text="Department").grid(row = 2)
    Button(root, text = 'Recreate', command = createDept).grid(row = 2, column = 3)
    Button(root, text = 'Add Entry', command = addDeptWin).grid(row = 2, column = 5)
    Button(root, text = 'View', command = viewDept).grid(row = 2, column = 7)

    Label(root, text="Section").grid(row = 3)
    Button(root, text = 'Recreate', command = createSect).grid(row = 3, column = 3)
    Button(root, text = 'Add Entry', command = addSectionWin).grid(row = 3, column = 5)
    Button(root, text = 'View', command = viewSect).grid(row = 3, column = 7)

    Label(root, text="Student").grid(row = 4)
    Button(root, text = 'Recreate', command = createStudent).grid(row = 4, column = 3)
    Button(root, text = 'Add Entry', command = addStudentWin).grid(row = 4, column = 5)
    Button(root, text = 'View', command = viewStudent).grid(row = 4, column = 7)

    Label(root, text="Grade").grid(row = 5)
    Button(root, text = 'Recreate', command = createGrade).grid(row = 5, column = 3)
    Button(root, text = 'Add Entry', command = addGradeWin).grid(row = 5, column = 5)
    Button(root, text = 'Report', command = getReport).grid(row = 5, column = 7)

    #Department Search
    Label(root, text="-").grid(row = 6)
    Label(root, text="Department Search").grid(row = 7)
    deptSearch = Entry(root, bd =5)
    deptSearch.grid(row = 8)
    var = 0

    #Department Radio Button
    dept1 = Radiobutton(root, text="Code", variable=var, value=1)
    dept1.grid(row = 8, column = 3)
    dept2 = Radiobutton(root, text="Name", variable=var, value=2)
    dept2.grid(row = 8, column = 5)

    def searchDept():
        if var == 1:
            str = "SELECT * FROM Course WHERE dept =" + deptSerch.get()
        else:
           str = "SELECT * FROM Course JOIN Department ON Course.dept = Department.dcode WHERE Department.dname = " + deptSearch.get()

        viewTable(str)

    Button(root, text = 'Search', command = searchDept).grid(row = 8, column = 7)
    root.mainloop()
