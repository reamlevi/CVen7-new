import Json
import CloudinaryP
"""CreateCv--------------------------------------------------------------------------------------------------------------------------------------------"""
def CreateCV(name, edu, pic, id, exp):
    data=Json.FetchJson()
    D = {'Notes':"",'Status': "Under review",'Picture': CloudinaryP.upload(pic, id),'Experience': exp, 'Education': edu,'ID': id,'Name': name}
    data.append(D)
    Json.SaveJason(data)

"""UploadPic----------------------------------------------------------------------------------------------------------------------------------------------"""
def UploadPic(pic, id):
    CloudinaryP.upload(pic, id)

"""CheckMyStatus------------------------------------------------------------------------------------------------------------------------------------------"""
def CheckMyStatus(id):

    """
    >>> CheckMyStatus(123456789)
    Name: TestName
    ID: 123456789
    Education: TestEducation
    Experience: TestExp
    Picture: TestPic
    Status: TestStatus
    <BLANKLINE>
    """

    data=Json.FetchJson()
    for c in data:
        if (str(id) == str(c['ID'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience: {}\nPicture: {}\nStatus: {}\n'.format(c['Name'], str(c['ID']),c['Education'], c['Experience'],c['Picture'], c['Status']))

"""EditCV-------------------------------------------------------------------------------------------------------------------------------------------------"""
def EditCV(id,value,type='n'):

    """"
    >>> EditCV(123456789,"TestName",'n')
    The Name is update
    >>> EditCV(123456789,"TestEducation",'e')
    The Education is update
    >>> EditCV(123456789,"TestExp",'exp')
    The Experience is update
    """

    data = Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            if (type.lower()=='n'):
                c['Name']=value
                print ("The Name is update")
            elif (type.lower()=='e'):
                c['Education']=value
                print ("The Education is update")
            elif (type.lower()=='exp'):
                c['Experience']=value
                print ("The Experience is update")
    Json.SaveJason(data)


