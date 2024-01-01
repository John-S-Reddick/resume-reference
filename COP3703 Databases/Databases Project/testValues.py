import names
import random
from utilities import *
from datetime import datetime

def ranPhone():
    return "%d-%d-%d"%(random.randrange(000,999), random.randrange(000,999), random.randrange(0000,9999))

def ranState():
    return random.choice(
        ["AL","AK","AZ","AR","CA",
        "CZ","CO","CT","DE","DC",
        "FL","GA","GU","HI","ID",
        "IL","IN","IA","KS","KY",
        "LA","ME","MD","MA","MI",
        "MN","MS","MO","MT","NE",
        "NV","NH","NJ","NM","NY",
        "NC","ND","OH","OK","OR",
        "PA","PR","RI","SC","SD",
        "TN","TX","UT","VT","VI",
        "VA","WA","WV","WI","WY"])

def className():
    return random.choice([
        "Accounting","Advertising",
        "African and Asian | Languages, Literatures, and Cultures",
        "African Studies","African-American Studies",
        "Agricultural and Biological Engineering",
        "Agricultural and Life Sciences | General",
        "Agricultural Education and Communication",
        "Agricultural Operations Management","Agronomy",
        "Akan | Languages, Literatures, and Cultures",
        "Amharic | Languages, Literatures, and Cultures",
        "Animal Sciences","Anthropology",
        "Applied Physiology and Kinesiology",
        "Arabic | Languages, Literatures, and Cultures",
        "Architecture","Art + Art History",
        "Astronomy and Astrophysics",
        "Biochemistry and Molecular Biology",
        "Biology | Botany | Zoology",
        "Biomedical Engineering","Botany",
        "Business","Chemical Engineering","Chemistry",
        "Chinese | Languages, Literatures, and Cultures",
        "Civil and Coastal Engineering","Classics",
        "Clinical and Health Psychology",
        "Computer & Information Science & Engineering",
        "Construction Management",
        "Criminology","Czech | Languages, Literatures, and Cultures",
        "Dial Center for Written and Oral Communication",
        "Digital Worlds Institute","Dutch | Languages, Literatures, and Cultures",
        "Economics","Education | School of Human Development and Organizational Studies",
        "Education | School of Special Education, School Psychology and Early Childhood Studies",
        "Education | School of Teaching and Learning",
        "Electrical and Computer Engineering","Engineering","English",
        "Entomology and Nematology","Environmental Engineering Sciences",
        "Environmental Horticulture","Environmental Science",
        "European Studies","Family, Youth and Community Sciences",
        "Film and Media Studies","Finance, Insurance, and Real Estate",
        "Fine Arts","Fire and Emergency Services",
        "Fisheries and Aquatic Sciences","Food and Resource Economics",
        "Food Science and Human Nutrition",
        "Forest, Fisheries, and Geomatics Sciences",
        "French | Languages, Literatures, and Cultures",
        "Gender, Sexualities, and Women’s Studies",
        "Geography","Geological Sciences","Geomatics",
        "German | Languages, Literatures, and Cultures",
        "Greek Studies","Haitian Creole | Languages, Literatures, and Cultures",
        "Health Education & Behavior","Health Professions",
        "Health Science","Hebrew | Languages, Literatures, and Cultures",
        "Hindi-Urdu | Languages, Literatures, and Cultures","History",
        "Honors Program","Horticultural Sciences","Hungarian | European Studies",
        "Industrial and Systems Engineering","Information Systems and Operations Management",
        "Innovation Academy","Interdisciplinary Studies","Interior Design",
        "Italian | Languages, Literatures, and Cultures",
        "Japanese | Languages, Literatures, and Cultures",
        "Jewish Studies","Journalism","Korean | Languages, Literatures, and Cultures",
        "Landscape Architecture","Languages, Literatures, and Cultures",
        "Latin American Studies","Latin | Classics","Lingala | Languages, Literatures, and Cultures",
        "Linguistics","Management","Marketing","Mass Communication",
        "Materials Science and Engineering","Mathematics","Mechanical & Aerospace Engineering",
        "Media Production, Management, and Technology","Medicine",
        "Medieval and Early Modern Studies","Microbiology & Cell Science",
        "Military Science","Music","Nuclear and Radiological Engineering",
        "Nursing","Occupational Therapy","Packaging Science","Pest Management | Plant Protection",
        "Pharmacy","Philosophy","Physics","Plant Pathology",
        "Polish | Languages, Literatures, and Cultures",
        "Political Science","Portuguese | Spanish and Portuguese Studies",
        "Psychology","Public Health","Public Relations","Quest","Rehabilitative Services",
        "Religion","Russian | Languages, Literatures, and Cultures","Sociology",
        "Soil and Water Sciences","Spanish and Portuguese Studies",
        "Spanish | Spanish and Portuguese Studies","Speech, Language and Hearing Sciences",
        "Sport Management","Statistics","Sustainability and the Built Environment",
        "Swahili | Languages, Literatures, and Cultures","Theatre + Dance",
        "Tourism, Hospitality and Event Management","Turkish | European Studies",
        "Urban and Regional Planning","Veterinary Medical Sciences",
        "Vietnamese | Languages, Literatures, and Cultures","Wildlife Ecology and Conservation",
        "Wolof | Languages, Literatures, and Cultures",
        "Xhosa | Languages, Literatures, and Cultures",
        "Yoruba | Languages, Literatures, and Cultures",
        "Zoology"])


def newCourse():
    insCourse([
        #cname
        className(),
        #cdesc
        "And a random description",
        #cnum
        random.randrange(10000,99999),
        #hours
        random.randrange(1,4),
        #level
        random.randrange(1,4) * 1000,
        #dept
        "Department %d" % random.randrange(000,100)
    ])

def newDept():
    insDept([
        #dname
        "Department %d"%random.randrange(000,100),
        #dcode
        random.randrange(10000,99999),
        #onum
        random.randrange(000,999),
        #ophone
        ranPhone(),
        #college
        random.choice(["Math","Engineering","Liberal Arts"])
    ])

def newSect():
    insSect([
        #instructor
        names.get_full_name(),
        #sem
        random.choice(["Fall","Spring","Summer"]),
        #year
        str(random.randrange(2000,2030)),
        #course
        className(),
        #snum
        str(random.randrange(000,999))
    ])

def newStudent():
    insStudent([
        #fname
        str(names.get_first_name()),
        #lname
        str(names.get_last_name()),
        #nnum
        str(random.randrange(00000000,99999999)),
        #sssn
        str(random.randrange(100000000,999999999)),
        #bday
        datetime.strptime('09-19-2018', '%m-%d-%Y').date(),
        #sex
        str(random.choice(['M','F'])),
        #class
        str(random.choice(["Freshman","Sophmore","Junior","Senior"])),
        #major
        className(),
        #minor,
        className(),
        #caddr
        "An address",
        #ccity
        "Jacksonville",
        #cstate
        str(ranState()),
        #czip
        str(random.randrange(00000,99999)),
        #cphone
        str(ranPhone()),
        #paddr
        "An address",
        #pcity
        "Somewhere",
        #pstate
        str(ranState()),
        # pzip
        str(random.randrange(00000,99999)),
        #pphone
        str(ranPhone())
        ])
createStudent()
createSect()
createDept()
newStudent()
newCourse()
newDept()
newSect()
