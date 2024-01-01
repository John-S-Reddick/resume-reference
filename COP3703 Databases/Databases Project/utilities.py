import cx_Oracle

#Networking
def connect():
    return cx_Oracle.connect(
        user='G8', password='Fall2021G8',
        dsn= cx_Oracle.makedsn(
            host='cisvm-oracle.unfcsd.unf.edu',
            port=1521, sid='orcl'))

#Standard Sql
def createTable(sql):
    conn = connect()
    cur1 = conn.cursor()
    try:
        cur1.execute(sql)
    except cx_Oracle.DatabaseError:
        pass

    conn.commit()

def insToTable(sql, args):
    conn = connect()
    cur1 = conn.cursor()
    cur1.execute(sql, args)
    conn.commit()

def viewTable(str):
    conn = connect()
    cur1 = conn.cursor()
    cur1.execute(str)
    return cur1

#Course
def createCourse():
    createTable("""
        CREATE TABLE Course(
        cname varchar(255) NOT NULL,
        cdesc varchar(255) NOT NULL,
        cnum varchar(255) PRIMARY KEY NOT NULL,
        shours int NOT NULL,
        clevel varchar(255) NOT NULL,
        dept varchar(255) NOT NULL)
        )""")

def insCourse(args):
     insToTable("""
        INSERT INTO Course(cname,cdesc, cnum, shours, clevel, dept)
        VALUES (:cname, :cdesc, :cnum, :shours, :clevel, :cdept)
        """,args)


#Department
def createDept():
    createTable("""
        CREATE TABLE Department(
        dname varchar(255) NOT NULL,
        dcode varchar(255) PRIMARY KEY NOT NULL,
        onum varchar(255)  NOT NULL,
        ophone varchar(255) NOT NULL,
        college varchar(255) NOT NULL
        )""")

def insDept(args):
    insToTable("""
        INSERT INTO Department(dname, dcode, onum, ophone, college)
        VALUES (:dname, :dcode, :onum, :ophone, :college)
        """,args)


#Grades
def createGrade():
    createTable("""
        CREATE TABLE Grade(
        course varchar(255) NOT NULL,
        section varchar(255) NOT NULL,
        nnum varchar(255) NOT NULL,
        lgrade varchar(2)NOT NULL,
        FOREIGN KEY course REFERENCES Course(cnum)
        FOREIGN KEY section REFERENCES Section(snum)
        UNIQUE (nnum, course, section)
        )""")

def insGrade(args):
     insToTable("""
        INSERT INTO Grade(nnum, course, section, lgrade)
        VALUES (:nnum, :course, :section, :lgrade)
        """,args)


#Section
def createSect():
    createTable("""
        CREATE TABLE Section(
        instructor varchar(255) NOT NULL,
        sem varchar(255) PRIMARY KEY NOT NULL,
        year varchar(255)  NOT NULL,
        course varchar(255) NOT NULL,
        snum varchar(255) NOT NULL
        UNIQUE (year, snum, section, course, year)
        )""")

def insSect(args):
    insToTable("""
        INSERT INTO Section(instructor, sem, year, course, snum)
        VALUES (:instructor, :sem, :year, :course, :snum)
        """,args)


#Students
def createStudent():
    createTable("""
        CREATE TABLE Student(
        fname varchar(255) NOT NULL,
        lname varchar(255) NOT NULL,
        nnum varchar(255) NOT NULL UNIQUE,
        sssn varchar(255) NOT NULL UNIQUE,
        bday date NOT NULL,
        sex char NOT NULL,
        class varchar(255) NOT NULL,
        major varchar(255) NOT NULL,
        minor varchar(255),
        caddr varchar(255) NOT NULL,
        ccity varchar(255) NOT NULL,
        cstate varchar(255) NOT NULL,
        czip varchar(255) NOT NULL,
        cphone varchar(255) NOT NULL,
        paddr varchar(255) NOT NULL,
        pcity varchar(255) NOT NULL,
        pstate varchar(255) NOT NULL,
        pzip varchar(255) NOT NULL,
        pphone varchar(255) NOT NULL,
        PRIMARY KEY(sssn, nnum)
        )""")


def insStudent(args):
    insToTable("""
        INSERT INTO Student(
            fname,lname,nnum,sssn,
            bday,sex,
            class,major,minor,
            caddr,ccity,cstate,czip,cphone,
            paddr,pcity,pstate,pzip,pphone)
        VALUES (
            :fname,:lname,:nnum,:sssn,
            :bday,:sex,
            :class,:major,:minor,
            :caddr,:ccity,:cstate,:czip,:cphone,
            :paddr,:pcity,:pstate,:pzip,:pphone
            )""",args)
