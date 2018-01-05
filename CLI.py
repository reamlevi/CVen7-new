import argparse
import textwrap
import Candidate
import HR
import Users

parser = argparse.ArgumentParser(
    prog='PROG',
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''\
         -------------------------------
         Login and Registerion Function:
         -------------------------------
         1) RegistrationC- Needed username and password and registerion (c)
         2) RegistrationHR- Needed username and password and registerion (hr)
         3) Login- Needed username and password and type (can be c or hr)
         --------------------------------------
         HR Function (permissions only for HR):
         --------------------------------------
         4) Search- Needed Search value (can be ID,Education or Experience)
         5) UpdateStatus- Needed ID and Status
         6) AddNotes- Nedded Id and Notes
         ---------------------------------------------------
         Candidate Functions (permissions only for Candidate)
         ---------------------------------------------------
         7) CreateCV- Needed Name,ID,Education,Experience,URL and Status
         8) UploadPic- Nedded Picture name and ID
         9) CheckMyStatus- Needed ID 
         10)EditCV-Needed Id, Value and Option
        '''))

parser.add_argument('-u', action="store",dest='username',help='Enter a username')
parser.add_argument('-p', action="store",dest='password', type=int, help='Enter a password (only numbers!)')
parser.add_argument('-r',dest='register', help='Enter a type of users for registration (c/hr)')
parser.add_argument('-t',dest='type', help='Enter type to login user (c/hr)')
parser.add_argument('-n',dest='name' ,help='Enter a name to fiil the CV file')
parser.add_argument('-id',dest='id' ,help='Enter your ID to fiil the CV file')
parser.add_argument('-e',dest='education' ,help='Enter a education to fiil the CV file')
parser.add_argument('-exp',dest='exp' ,help='Enter your experience to fiil the CV file')
parser.add_argument('-url',dest='url' ,help='Enter a url to your picture to fiil the CV file')
parser.add_argument('-st',dest='status' ,help='Enter new status for candidate')
parser.add_argument('-s',dest='search' ,help='Enter a value to search candidate ')
parser.add_argument('-note',dest='note',help='Add note to candidate')
parser.add_argument('-pic',dest='pic',help='Add a picture')
parser.add_argument('-v',dest='value',help='Enter a value to edit your CV')
parser.add_argument('-o',dest='option',help='Enter a type of values to edit your CV (n-name,e-education,exp-experience)')
result=parser.parse_args()

if (result.username and result.password and (result.register)=='c'):
    Users.RegistrationC(result.username,result.password)
elif (result.username and result.password and (result.register)=='hr'):
    Users.RegistrationHR(result.username,result.password)
elif (result.username and result.password and result.type):
    Users.Login(result.username,result.password,result.type)

elif (Users.CheckIfLoginHR(result.username)):
    if (result.search):
        HR.Serach(result.search)
    elif (result.id and result.status):
        HR.UpdateStatus(result.id, result.status)
    elif (result.id and result.note):
        HR.AddNotes(result.id, result.note)

elif (Users.CheckIfLoginC(result.username)):
    if (result.name and result.education and result.pic and result.id and result.exp):
        Candidate.CreateCV(result.name,result.education,result.pic,result.id,result.exp)
    elif (result.id and result.value and result.option):
        Candidate.EditCV(result.id, result.value, result.option)
    elif (result.id):
        Candidate.CheckMyStatus(result.id)